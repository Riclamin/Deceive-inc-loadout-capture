from checkForUpdates import check_for_updates
from LoadData import localDirectory, AgentStatsDF, GadgetStatsDF, UpgradeChipStatsDF, Agents, Weapons, Expertises, Passives, Gadgets, UpgradeTiers, UpgradeChips, determine_likeness


def main():
    check_for_updates()
    currentLoadout = []
    # 0 = fully generated
    # 1 = fully generated
    # 2 = Fully generated
    # 3 = agent
    # 4 = weapon
    # 5 = expertise
    # 6 = passive
    # 7 = g1
    # 8 = g2
    # 9 = grey
    # 10= green
    # 11= blue
    # 12= purple
    # 13= gold


    with open(f'{localDirectory}\\CurrentLoadout.txt', "r+") as loadoutFile:
        currentLoadout = loadoutFile.readlines()

    command = ''
    with open(f'{localDirectory}\\UpdateLoadout.txt', 'r') as commandFile:
        command = commandFile.readline()

    # !UpdateLoadout "tobeUpdated"="WhatItShouldBe" ... ... 
    updates = command.split()

    Agent = currentLoadout[3].strip('\n')
    Weapon = None
    Expertise = None
    Passive = None
    Gadget1 = None
    Gadget2 = None
    greyName = None
    greenName = None
    blueName = None
    purpleName = None
    goldName = None

    for update in updates:
        key, value = update.split('=')

        #Debugging:
        print(f'{key}, {value}')

        AgentValue = determine_likeness(value, Agents)
        GadgetValue = determine_likeness(value, Gadgets) 
        chipTierValue = determine_likeness(key, UpgradeTiers)
        WeaponValue = determine_likeness(value, Weapons)
        ExpertiseValue = determine_likeness(value, Expertises)
        PassiveValue = determine_likeness(value, Passives)
        chipNameValue = determine_likeness(value, UpgradeChips)

        #Debugging:
        # print( f'{AgentValue}, {GadgetValue}, {chipTierValue}, {WeaponValue}, {ExpertiseValue}, {PassiveValue}, {chipNameValue}')

        if AgentValue is not None:
            Agent = AgentValue
        elif GadgetValue is not None:
            keyValue = determine_likeness(key, ['g1', 'g2'])
            if keyValue == 'g1':
                Gadget1 = GadgetValue
            elif keyValue == 'g2':
                Gadget2 = GadgetValue
        elif chipTierValue is not None:
            chipTier = chipTierValue
            if chipTier == 'Grey':
                if chipNameValue is not None:
                    greyName = chipNameValue
            elif chipTier == 'Green':
                if chipNameValue is not None:
                    greenName = chipNameValue
            elif chipTier == 'Blue':
                if chipNameValue is not None:
                    blueName = chipNameValue
            elif chipTier == 'Purple':
                if chipNameValue is not None:
                    purpleName = chipNameValue
            elif chipTier == 'Gold':
                if chipNameValue is not None:
                    goldName = chipNameValue
            
        elif WeaponValue is not None:
            Weapon = WeaponValue
        elif ExpertiseValue is not None:
            Expertise = ExpertiseValue
        elif PassiveValue is not None:
            Passive = PassiveValue
    
    #Know complete new build: Now write to file.
    # 0 = fully generated
    # 1 = fully generated
    # 2 = Fully generated
    # 3 = agent
    # 4 = weapon
    # 5 = expertise
    # 6 = passive
    # 7 = g1
    # 8 = g2
    # 9 = grey
    # 10= green
    # 11= blue
    # 12= purple
    # 13= gold

    if Agent is not None:
        currentLoadout[3]= (f'{Agent}\n')
    
    if Weapon is not None:
        currentLoadout[4]= (f'{AgentStatsDF.at[Agent, Weapon]}\n')
    
    if Expertise is not None:
        currentLoadout[5]= (f'{AgentStatsDF.at[Agent, Expertise]}\n')
    
    if Passive is not None:
        currentLoadout[6]= (f'{AgentStatsDF.at[Agent, Passive]}\n')

    if Gadget1 is not None:
        currentLoadout[7]= (f'{GadgetStatsDF.at[Gadget1, "Stats"]}\n')

    if Gadget2 is not None:
        currentLoadout[8]= (f'{GadgetStatsDF.at[Gadget2, "Stats"]}\n')
    
    if greyName is not None:
        currentLoadout[9]= (f'{UpgradeChipStatsDF.at[greyName, "Grey"]}\n')
    
    if greenName is not None:
        currentLoadout[10]= (f'{UpgradeChipStatsDF.at[greenName, "Green"]}\n')

    if blueName is not None:
        currentLoadout[11]= (f'{UpgradeChipStatsDF.at[blueName, "Blue"]}\n')
    
    if purpleName is not None:
        currentLoadout[12]= (f'{UpgradeChipStatsDF.at[purpleName, "Purple"]}\n')

    if goldName is not None:
        currentLoadout[13]= (f'{UpgradeChipStatsDF.at[goldName, "Gold"]}\n')


        
    
    # example: Cavaliere: w3 e1 p3, g1=BounceMat, g2=Turret, grey=Cover Accelerator, green=External Hard-Drive, blue=Bulletproof Fabric, purple=Nutritional Supplement, gold=Overclock Chip
    fullLoadout = currentLoadout[0].split(', ')
    AgentLoadout = fullLoadout[0].split()
    
    if Agent is not None:
        AgentLoadout[0] = Agent + ':'
    if Weapon is not None:
        AgentLoadout[1] = Weapon
    if Expertise is not None:
        AgentLoadout[2] = Expertise
    if Passive is not None:
        AgentLoadout[3] = Passive
    fullLoadout[0] = ' '.join(AgentLoadout)

    if Gadget1 is not None:
        fullLoadout[1] = f'g1={Gadget1}'

    if Gadget2 is not None:
        fullLoadout[2] = f'g2={Gadget2}'
    
    if greyName is not None:
        fullLoadout[3] = f'grey={greyName}'

    if greenName is not None:
        fullLoadout[4] = f'grey={greenName}'

    if blueName is not None:
        fullLoadout[5] = f'grey={blueName}'

    if purpleName is not None:
        fullLoadout[6] = f'grey={purpleName}'
        
    if goldName is not None:
        fullLoadout[7] = f'grey={goldName}'

    fullLoadoutString = ", ".join(fullLoadout).strip('\n') + '\n'
    NoChipsString = ", ".join(fullLoadout[0:3]).strip('\n') + '\n'
    OnlyChipsString =", ".join(fullLoadout[3:]).strip('\n') + '\n'
    
    #Debugging: 
    # print(localDirectory)
    # print(fullLoadoutString)
    # print(NoChipsString)
    # print(OnlyChipsString)

    currentLoadout[0]= fullLoadoutString
    currentLoadout[1]= NoChipsString
    currentLoadout[2]= OnlyChipsString

    with open(f'{localDirectory}\\CurrentLoadout.txt', "w+") as loadoutFile:
        loadoutFile.writelines(currentLoadout)




main()