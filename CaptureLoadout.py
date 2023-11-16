import pyautogui
from checkForUpdates import check_for_updates
from LoadData import localDirectory, AgentStatsDF, GadgetStatsDF, UpgradeChipStatsDF, Agents, Weapons, Expertises, Passives, Gadgets, UpgradeTiers, UpgradeChips


def main():
    check_for_updates()
    screenshot = pyautogui.screenshot()
    loadout = {"Agent": None, "Weapon": None, "Expertise": None, "Passive": None, 
           "Gadget1": None, "Gadget2": None, 
           "UpgradeGrey": None, "UpgradeGreen": None, "UpgradeBlue": None, "UpgradePurple": None, "UpgradeGold": None}

    loadout = lookup_gadgets(screenshot, loadout)
    loadout = lookup_chips(screenshot, loadout)
    loadout = lookup_agent_loadout(screenshot, loadout)
    export_loadout_to_text_file(loadout)
    #TODO: Notify user?



def lookup_gadgets(screenshot, loadout):
    #lookup gadgets.
    for gadget in Gadgets:
        try: 
            #Left gadget is around (89, 492), Right gadget is around (189, 492) --> if x < 139 = left gadget (2) else: right gadget (3)
            (x, y, w,h) = pyautogui.locate(needleImage=f'{localDirectory}\Assets\Gadgets\{gadget}.png', 
                                    haystackImage=screenshot,
                                    confidence=0.95)
            print(f'Found {gadget} on screen at {x}, {y}')
            if x < 139:
                loadout["Gadget1"] = gadget
            elif x > 139:
                loadout["Gadget2"] = gadget
            else:
                print("PANIC!")
        except:
            # print(f'Did not find {gadget}')
            pass

        #If we found 2 gadgets we can stop looking.
        if (loadout["Gadget1"] is not None ) and (loadout["Gadget2"] is not None):
            break
    
    #Debugging:
    # print(f'Current gadget loadout: {loadout["Gadget1"]} and {loadout["Gadget2"]}')
    return loadout

def lookup_chips(screenshot, loadout):
    #Lookup chips
    for tier in UpgradeTiers:
        for chip in UpgradeChips:
            try: 
                (x,y,w,h) = pyautogui.locate(needleImage=f'{localDirectory}\Assets\\Upgrades folder\{tier}\{chip}.png',
                                        haystackImage=screenshot,
                                        confidence=0.90)
                # If not found, it will produce ImageNotFoundException and exit this try block.
                # print (f'chip found at {x}, {y}')
                loadout[f"Upgrade{tier}"] = chip
                # print(f'updated {tier} to be {chip}')
                break
            except: 
                pass
    
    # Debugging:
    print(f'Grey = {loadout["UpgradeGrey"]}, Green = {loadout["UpgradeGreen"]}, Blue = {loadout["UpgradeBlue"]}, Purple = {loadout["UpgradePurple"]}, Gold = {loadout["UpgradeGold"]}') 
    return loadout

def lookup_agent_loadout(screenshot, loadout):
    #Lookup agent + loadout.
    for agent in Agents:
        for weapon in Weapons:
            # print(f'testing {agent}, {weapon}')
            try: 
                (x, y, w, h) = pyautogui.locate(needleImage=f'{localDirectory}\Assets\Agents\{agent}\{weapon}.png',
                                        haystackImage=screenshot,
                                        confidence=0.95)
                # print(f'{x} {y}, {agent} {weapon}') #Debugging
                # If not found, it will produce ImageNotFoundException and exit this try block.
                loadout["Weapon"] = weapon
                loadout["Agent"] = agent
            except: 
                pass
        
        #If we didn't find any of the weapons of this agent, then there is no use in continuing to look for their expertises/passives.
        if loadout["Weapon"] is None:
            continue

        for expertise in Expertises:
            try: 
                (x, y, w, h) = pyautogui.locate(needleImage=f'{localDirectory}\Assets\Agents\{agent}\{expertise}.png', 
                                        haystackImage=screenshot,
                                        confidence=0.95)
                # print(f'{x} {y}, {expertise}') #Debugging
                # If not found, it will produce ImageNotFoundException and exit this try block.
                loadout["Expertise"] = expertise
            except: 
                pass

        for passive in Passives:
            try: 
                (x, y, w, h) = pyautogui.locate(needleImage=f'{localDirectory}\Assets\Agents\{agent}\{passive}.png', 
                                 haystackImage=screenshot,
                                 confidence=0.95)

                print(f'{x} {y}, {passive}') #Debugging
                # If not found, it will produce ImageNotFoundException and exit this try block.
                loadout["Passive"] = passive
            except: 
                pass
        
        # Found weapon, expertise and passive, can stop looking at other agents:
        break

    #Debugging:
    # print(f'Agent = {loadout["Agent"]}, weapon = {loadout["Weapon"]}, expertise = {loadout["Expertise"]}, passive = {loadout["Passive"]}')
    return loadout

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



main()