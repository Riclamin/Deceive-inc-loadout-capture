import pyautogui, time, keyboard, pandas, os, random

pyautogui.FAILSAFE = True

localDirectory = os.getcwd()
AgentStatsDF = pandas.read_csv(f'{localDirectory}\Stats\AgentLoadoutStats.csv', index_col=0, names=["Agent","w1","w2","w3","e1","e2","e3","p1","p2","p3"], sep=';')
GadgetStatsDF = pandas.read_csv(f'{localDirectory}\Stats\GadgetStats.csv', index_col=0, names=["Gadget","Stats"], sep = ';')
UpgradeChipStatsDF = pandas.read_csv(f'{localDirectory}\Stats\\UpgradeChipStats.csv', index_col=0,names=["Type","Grey", "Green", "Blue", "Purple", "Gold"], sep=';')
DictionaryDF = pandas.read_csv(f'{localDirectory}\Stats\\Dictionary.csv', index_col=0,names=["Term","Explanation"], sep=';')



Agents = ["Ace","Cavaliere", "Chavez", "Hans", "Larcin", "Madame Xiu", "Octo", "Red", "Sasori", "Squire", "Yu-Mi"]
Weapons = ["w1", "w2", "w3"]
Expertises = ["e1", "e2", "e3"]
Passives = ["p1", "p2", "p3"]
Gadgets = ["BounceMat", "GooPod", "HackTrap", "Holo-Mimic", "ReconDrone", "Scrambler", "Shield-Brella", "Spyglass", "Tripwire", "Turret"]
UpgradeTiers = ["Grey", "Green", "Blue", "Purple", "Gold"]
UpgradeChips = ["Cover Accelerator", "Extended Ammo Pouch", "External Hard-Drive", "Overclock Chip", "Bulletproof Fabric", "Field Agent Kit", "Social Battery", "Nutritional Supplement", "Exfiltration Scanner"]
Dictionary = ["Wx", "Ex", "Px", "Chip","Perk", "Upgrade", "Scan", "Wallhacks", "Vulnerable", "Traced", "Revealed", "Broadcast", "Exposed", "Neutralized", "Charmed", "Heartbroken", "Invisible", "AmpedUp", "Invulnerable", "Resistant", "Extract", "Secret Exits"]


def on_ctrl_u():
    screenshot = pyautogui.screenshot()
    loadout = {"Agent": None, "Weapon": None, "Expertise": None, "Passive": None, 
           "Gadget1": None, "Gadget2": None, 
           "UpgradeGrey": None, "UpgradeGreen": None, "UpgradeBlue": None, "UpgradePurple": None, "UpgradeGold": None}

    loadout = lookup_gadgets(screenshot, loadout)
    loadout = lookup_chips(screenshot, loadout)
    loadout = lookup_agent_loadout(screenshot, loadout)
    export_loadout_to_text_file(loadout)
    #TODO: Notify user?

def on_ctrl_i():
    with open(f'{localDirectory}\\randomLoadout.txt', "w+") as randomFile:
        randomFile.write(f'{random.choice(Agents)} w{random.randint(1,3)} e{random.randint(1,3)} p{random.randint(1,3)}, g: {random.sample(Gadgets,2)}, chips grey-gold: {random.sample(UpgradeChips,5)}')
        randomFile.flush

def on_ctrl_l():
    args = []
    with open(f'{localDirectory}\\DeceiveLookup.txt', "r") as lookupFile:
        args = lookupFile.readline().split()
    
    result = ''
    if args[0] == 'Agents':
        result = f'Agents available are: {Agents}'
    elif args[0] == 'Gadgets':
        result = f'Gadgets available are: {Gadgets}'
    elif args[0] == 'Chips':
        result = f'Chip names are: {UpgradeChips}'
    elif args[0] == 'Dictionary':
        result = f'Dictionary terms are: {Dictionary}'

    elif args[0] in Agents:
        if args[1] in Weapons or args[1] in Expertises or args[1] in Passives: 
            result = f"{args[0]}'s {args[1]} has the following info: {AgentStatsDF.at[args[0], args[1]]}"

    elif args[0] in Gadgets:
        result = f"{args[0]} has the following info: {GadgetStatsDF.at[args[0], 'Stats']}"

    elif args[0] in UpgradeTiers:
        if args[1] in UpgradeChips:
            result = f"A {args[0]} {args[1]} chip has the following info: {UpgradeChipStatsDF.at[args[1], args[0]]}"

    elif args[0] in Dictionary:
        result = f'Definition for {args[0]}: {DictionaryDF.at[args[0], "Explanation"]}'
    
    elif result == '':
        result = 'Did not recognise argument. Make sure to capitalise names. For a list of options use !DeceiveLookup Agents / !DeceiveLookup Gadgets / !DeceiveLookup Chips / !DeceiveLookup Dictionary'

    with open(f'{localDirectory}\\DeceiveLookup.txt', "w+") as lookupFile:
        lookupFile.writelines([result])




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
            print(f'Did not find {gadget}')
            pass

        #If we found 2 gadgets we can stop looking.
        if (loadout["Gadget1"] is not None ) and (loadout["Gadget2"] is not None):
            break
    
    #Debugging:
    print(f'Current gadget loadout: {loadout["Gadget1"]} and {loadout["Gadget2"]}')
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
                print (f'chip found at {x}, {y}')
                loadout[f"Upgrade{tier}"] = chip
                print(f'updated {tier} to be {chip}')
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
            print(f'testing {agent}, {weapon}')
            try: 
                (x, y, w, h) = pyautogui.locate(needleImage=f'{localDirectory}\Assets\Agents\{agent}\{weapon}.png',
                                        haystackImage=screenshot,
                                        confidence=0.95)
                print(f'{x} {y}, {agent} {weapon}') #Debugging
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
                print(f'{x} {y}, {expertise}') #Debugging
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
    print(f'Agent = {loadout["Agent"]}, weapon = {loadout["Weapon"]}, expertise = {loadout["Expertise"]}, passive = {loadout["Passive"]}')
    return loadout

def export_loadout_to_text_file(loadout: dict):
    print(loadout)
    for key in loadout:
        if loadout[key] is None:
            loadout[key] = 'BACKUP_IN_CASE_OF_ERROR'
    
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


keyboard.add_hotkey('ctrl+u', on_ctrl_u)
keyboard.add_hotkey('ctrl+esc', exit)
keyboard.add_hotkey('ctrl+i', on_ctrl_i)
keyboard.add_hotkey('ctrl+l', on_ctrl_l)

while True:
    keyboard.wait()