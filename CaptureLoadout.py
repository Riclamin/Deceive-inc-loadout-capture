import pyautogui
import cv2
import numpy as np
import os
from checkForUpdates import check_for_updates
from config import resolution
from LoadData import localDirectory, AgentStatsDF, GadgetStatsDF, UpgradeChipStatsDF, Agents, Weapons, Expertises, Passives, Gadgets, UpgradeTiers, UpgradeChips


def export_loadout_to_text_file(loadout: dict):
    # print(loadout) #Debugging
    for key in loadout:
        if loadout[key] is None:
            loadout[key] = 'x'

    
    loadoutLines = []
    loadoutLines.append(f'{loadout["Agent"]}: {loadout["Weapon"]} {loadout["Expertise"]} {loadout["Passive"]}, g1={loadout["Gadget1"]}, g2={loadout["Gadget2"]}, grey={loadout["UpgradeGrey"]}, green={loadout["UpgradeGreen"]}, blue={loadout["UpgradeBlue"]}, purple={loadout["UpgradePurple"]}, gold={loadout["UpgradeGold"]}\n') 
    loadoutLines.append(f'{loadout["Agent"]}: {loadout["Weapon"]} {loadout["Expertise"]} {loadout["Passive"]}, g1={loadout["Gadget1"]}, g2={loadout["Gadget2"]}\n') 
    loadoutLines.append(f'grey={loadout["UpgradeGrey"]}, green={loadout["UpgradeGreen"]}, blue={loadout["UpgradeBlue"]}, purple={loadout["UpgradePurple"]}, gold={loadout["UpgradeGold"]}\n')
    loadoutLines.append(f'{loadout["Agent"]}\n')


    loadoutLines.append(f'{AgentStatsDF.at[loadout["Agent"], loadout["Weapon"]]}\n')
    loadoutLines.append(f'{AgentStatsDF.at[loadout["Agent"], loadout["Expertise"]]}\n')
    loadoutLines.append(f'{AgentStatsDF.at[loadout["Agent"], loadout["Passive"]]}\n')
    loadoutLines.append(f'{GadgetStatsDF.at[loadout["Gadget1"], "Stats"]}\n')
    loadoutLines.append(f'{GadgetStatsDF.at[loadout["Gadget2"], "Stats"]}\n')
    loadoutLines.append(f'{UpgradeChipStatsDF.at[loadout["UpgradeGrey"], "Grey"]}\n')
    loadoutLines.append(f'{UpgradeChipStatsDF.at[loadout["UpgradeGreen"], "Green"]}\n')
    loadoutLines.append(f'{UpgradeChipStatsDF.at[loadout["UpgradeBlue"], "Blue"]}\n')
    loadoutLines.append(f'{UpgradeChipStatsDF.at[loadout["UpgradePurple"], "Purple"]}\n')
    loadoutLines.append(f'{UpgradeChipStatsDF.at[loadout["UpgradeGold"], "Gold"]}\n')

    with open(f'{localDirectory}\\CurrentLoadout.txt', "w+") as loadoutFile:
        loadoutFile.writelines(loadoutLines)




def lookup_agent_loadout(screenshot, loadout):
    screenshot = cv2.imread(screenshot)
    for agent in Agents:
        weaponFound = False
        for weapon in Weapons:
            print(f'testing {agent} {weapon}')
            template = cv2.imread(f'{localDirectory}\Assets\{resolution}\Agents\{agent}\{weapon}.png', cv2.IMREAD_UNCHANGED)
            base = template[:,:,0:3]
            alpha = template[:,:,3]
            alpha = cv2.merge([alpha,alpha,alpha])

            correlation = cv2.matchTemplate(screenshot, base, cv2.TM_CCORR_NORMED, mask=alpha)
            threshhold =1
            loc = np.where(correlation >= threshhold)
            if len(loc) >0:
                for pt in zip(*loc[::-1]):
                    print(f'found in {len(loc)} place(s)')
                    loadout["Weapon"] = weapon
                    loadout["Agent"] = agent
                    weaponFound = True
                    break
            
            if weaponFound:
                break
        
        if loadout["Agent"] == None: # Means we didn't find a weapon for the current agent, so we also won't find expertise and passive.
            continue
        
        expertiseFound = False
        for expertise in Expertises:
            print(f'testing {agent} {expertise}')
            template = cv2.imread(f'{localDirectory}\Assets\{resolution}\Agents\{agent}\{expertise}.png', cv2.IMREAD_UNCHANGED)
            base = template[:,:,0:3]
            alpha = template[:,:,3]
            alpha = cv2.merge([alpha,alpha,alpha])

            correlation = cv2.matchTemplate(screenshot, base, cv2.TM_CCORR_NORMED, mask=alpha)
            threshhold =0.999
            loc = np.where(correlation >= threshhold)
            if len(loc) >0:
                for pt in zip(*loc[::-1]):
                    loadout["Expertise"] = expertise
                    expertiseFound = True
                    break

            if expertiseFound:
                break
        
        passiveFound = False
        for passive in Passives:
            print(f'testing {agent} {passive}')
            template = cv2.imread(f'{localDirectory}\Assets\{resolution}\Agents\{agent}\{passive}.png', cv2.IMREAD_UNCHANGED)
            base = template[:,:,0:3]
            alpha = template[:,:,3]
            alpha = cv2.merge([alpha,alpha,alpha])

            correlation = cv2.matchTemplate(screenshot, base, cv2.TM_CCORR_NORMED, mask=alpha)
            threshhold =0.999
            loc = np.where(correlation >= threshhold)
            if len(loc) >0:
                for pt in zip(*loc[::-1]):
                    loadout["Passive"] = passive
                    passiveFound = True
                    break
            
            if passiveFound:
                break
        
        if loadout["Agent"] is not None:
            break

    return loadout


def lookup_gadgets(screenshot, loadout):
    #lookup gadgets.
    screenshot = cv2.imread(screenshot)
    for gadget in Gadgets:

        #1080p: Left gadget is around (89, 492), Right gadget is around (189, 492) --> if x < 139 = left gadget (2) else: right gadget (3)
        if (resolution == '1080p'):
            template = cv2.imread(f'{localDirectory}\Assets\{resolution}\Gadgets\{gadget}.png', cv2.IMREAD_UNCHANGED)
            base = template[:,:,0:3]
            alpha = template[:,:,3]
            alpha = cv2.merge([alpha,alpha,alpha])

            correlation = cv2.matchTemplate(screenshot, base, cv2.TM_CCORR_NORMED, mask=alpha)
            threshhold = 1
            loc = np.where(correlation >= threshhold)
            
            if len(loc) >0:
                for pt in zip(*loc[::-1]):
                    if pt[0] < 139:
                        loadout["Gadget1"] = gadget
                    else:
                        loadout["Gadget2"] = gadget
                    break
        
        #1440p: middle between gadgets is: (179,643)
        elif (resolution == '1440p'):
            template = cv2.imread(f'{localDirectory}\Assets\{resolution}\Gadgets\{gadget}.png', cv2.IMREAD_UNCHANGED)
            base = template[:,:,0:3]
            alpha = template[:,:,3]
            alpha = cv2.merge([alpha,alpha,alpha])

            correlation = cv2.matchTemplate(screenshot, base, cv2.TM_CCORR_NORMED, mask=alpha)
            threshhold =1
            loc = np.where(correlation >= threshhold)
            
            if len(loc) >0:
                for pt in zip(*loc[::-1]):
                    if pt[0] < 139:
                        loadout["Gadget1"] = gadget
                    else:
                        loadout["Gadget2"] = gadget
                    break

        #If we found 2 gadgets we can stop looking.
        if (loadout["Gadget1"] is not None ) and (loadout["Gadget2"] is not None):
            break
    
    #Debugging:
    # print(f'Current gadget loadout: {loadout["Gadget1"]} and {loadout["Gadget2"]}')
    return loadout

def lookup_chips(screenshot, loadout):
    #Lookup chips
    screenshot = cv2.imread(screenshot)
    for tier in UpgradeTiers:
        chipFound = False
        for chip in UpgradeChips:
            print(f'testing {tier}, {chip}')
            template = cv2.imread(f'{localDirectory}\Assets\{resolution}\\Upgrades Folder\{tier}\{chip}.png', cv2.IMREAD_UNCHANGED)
            # hh, ww = template.shape[:2]
            base = template[:,:,0:3]
            alpha = template[:,:,3]
            alpha = cv2.merge([alpha,alpha,alpha])

            correlation = cv2.matchTemplate(screenshot, base, cv2.TM_CCORR_NORMED, mask=alpha)
            threshhold =1
            loc = np.where(correlation >= threshhold)
            # result = screenshot.copy()
            
            if len(loc) >0:
                for pt in zip(*loc[::-1]):
                    loadout[f"Upgrade{tier}"] = chip
                    chipFound = True
            
            if chipFound:
                break    
    
    # Debugging:
    # print(f'Grey = {loadout["UpgradeGrey"]}, Green = {loadout["UpgradeGreen"]}, Blue = {loadout["UpgradeBlue"]}, Purple = {loadout["UpgradePurple"]}, Gold = {loadout["UpgradeGold"]}') 
    return loadout



def main():
    check_for_updates()
    screenshot = 'loadout.png'
    pyautogui.screenshot(screenshot)
    loadout = {"Agent": None, "Weapon": None, "Expertise": None, "Passive": None, 
           "Gadget1": None, "Gadget2": None, 
           "UpgradeGrey": None, "UpgradeGreen": None, "UpgradeBlue": None, "UpgradePurple": None, "UpgradeGold": None}

    loadout = lookup_gadgets(screenshot, loadout)
    loadout = lookup_chips(screenshot, loadout)
    loadout = lookup_agent_loadout(screenshot, loadout)
    print(f'loadout = {loadout}')
    export_loadout_to_text_file(loadout)
    os.remove('loadout.png')


main()

