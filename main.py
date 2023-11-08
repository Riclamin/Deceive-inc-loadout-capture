import pyautogui, keyboard, pandas, os, random
from urllib.request import urlretrieve

pyautogui.FAILSAFE = True

with open("checkForUpdates.py") as f:
    exec(f.read())


localDirectory = os.getcwd()
AgentStatsDF = pandas.read_csv(f'{localDirectory}\Stats\AgentLoadoutStats.csv', index_col=0, names=["Agent","w1","w2","w3","e1","e2","e3","p1","p2","p3", "x"], sep=';')
GadgetStatsDF = pandas.read_csv(f'{localDirectory}\Stats\GadgetStats.csv', index_col=0, names=["Gadget","Stats","x"], sep = ';')
UpgradeChipStatsDF = pandas.read_csv(f'{localDirectory}\Stats\\UpgradeChipStats.csv', index_col=0, names=["Type","Grey", "Green", "Blue", "Purple", "Gold","x"], sep=';')
DictionaryDF = pandas.read_csv(f'{localDirectory}\Stats\\Dictionary.csv', index_col=0, names=["Term","Explanation"], sep=';')



Agents = AgentStatsDF.index.values.tolist()[1:] 
Weapons = ["w1", "w2", "w3"]
Expertises = ["e1", "e2", "e3"]
Passives = ["p1", "p2", "p3"]
Gadgets = GadgetStatsDF.index.values.tolist()[1:] 
UpgradeTiers = ["Grey", "Green", "Blue", "Purple", "Gold"]
UpgradeChips = UpgradeChipStatsDF.index.values.tolist()[1:] 
Dictionary = DictionaryDF.index.values.tolist()[1:] 


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
    print('ctrl+l')
    args = []
    with open(f'{localDirectory}\\DeceiveLookup.txt', "r") as lookupFile:
        args = lookupFile.readline().split()


    Agent = None
    Weapon = None
    Expertise = None
    Passive = None
    Gadget = None
    chipTier = None
    chipName = None
    Term = None

    if len(args)>= 1:
        Agent = determine_likeness(args[0], Agents)
        Gadget = determine_likeness(args[0], Gadgets) 
        chipTier = determine_likeness(args[0], UpgradeTiers)
        Term = determine_likeness(args[0], Dictionary)
    
    if len(args)>= 2:
        Weapon = determine_likeness(args[1], Weapons)
        Expertise = determine_likeness(args[1], Expertises)
        Passive = determine_likeness(args[1], Passives)
        chipName = determine_likeness(args[1], UpgradeChips)

    print(f'{Agent}, {Gadget}, {chipTier}, {Term}, {Weapon}, {Expertise}, {Passive}, {chipName}')

    result = ''
    if len(args) == 0:
        result = 'For a list of options use !DeceiveLookup Agents / !DeceiveLookup Gadgets / !DeceiveLookup Chips / !DeceiveLookup Dictionary'
    elif len(args) >= 1:
        #Single arguments
        if args[0] == 'Agents':
            result = f'Agents available are: {Agents}'
        elif args[0] == 'Gadgets':
            result = f'Gadgets available are: {Gadgets}'
        elif args[0] == 'Chips':
            result = f'Chip names are: {UpgradeChips}'
        elif args[0] == 'Dictionary':
            result = f'Dictionary terms are: {Dictionary}'
        elif Term is not None:
            result = f'Definition for {Term}: {DictionaryDF.at[Term, "Explanation"]}'
        elif Gadget is not None:
            result = f"{Gadget} has the following info: {GadgetStatsDF.at[Gadget, 'Stats']}"
        
        if result != '':
            write_lookup_to_file(result)
            return

        # possbile more than one argument

        if Agent is not None and ((Weapon is not None) or (Expertise is not None) or (Passive is not None)):
            arg1 =''
            if Weapon is not None:
                arg1 = Weapon
            elif Expertise is not None:
                arg1 = Expertise
            else:
                arg1 = Passive
            result = f"{Agent}'s {arg1} has the following info: {AgentStatsDF.at[Agent, arg1]}"



        elif chipTier is not None and chipName is not None:
            result = f"A {chipTier} {chipName} chip has the following info: {UpgradeChipStatsDF.at[chipName, chipTier]}"


    if result == '':
        result = 'Did not recognise argument. Make sure to capitalise names. For a list of options use !DeceiveLookup Agents / !DeceiveLookup Gadgets / !DeceiveLookup Chips / !DeceiveLookup Dictionary'
    write_lookup_to_file(result)


def write_lookup_to_file(result):            
    with open(f'{localDirectory}\\DeceiveLookup.txt', "w+") as lookupFile:
        lookupFile.writelines([result])


def determine_likeness(name, options):
    for option in options:
        if minimise_name(name) in minimise_name(option): 
            return option
    return None


def minimise_name(name: str):
    name = name.replace(' ', '')
    name = name.replace('-', '')
    name = name.lower()
    return name



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
    print(loadout) #Debugging
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


keyboard.add_hotkey('ctrl+u', on_ctrl_u)
keyboard.add_hotkey('ctrl+i', on_ctrl_i)
keyboard.add_hotkey('ctrl+l', on_ctrl_l)

while True:
    keyboard.wait()