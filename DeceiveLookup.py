import os, pandas, sys
from checkForUpdates import check_for_updates
from LoadData import localDirectory, AgentStatsDF, DictionaryDF, GadgetStatsDF, UpgradeChipStatsDF, Agents, Weapons, Expertises, Passives, Gadgets, UpgradeTiers, UpgradeChips, Dictionary

check_for_updates()


def write_lookup_to_file(result):            
    with open(f'{localDirectory}\\DeceiveLookupResult.txt', "w+") as lookupFile:
        lookupFile.writelines([result])


def determine_likeness(name, options):
    for option in options:
        minimised_name = minimise_name(name)
        minimised_option = minimise_name(option)
        if minimised_name in minimised_option or minimised_option == minimised_name: 
            return option
    return None


def minimise_name(name: str):
    return name.replace(' ', '').replace('-', '').replace('\n','').lower()


def lookup(args: [str]):
    with open(f'{localDirectory}\\DeceiveLookupLog.txt', "a+") as log:
        log.write(f'{args}')
        log.write('\n')
        log.flush


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

        # possibly more than one argument

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
        result = 'Did not recognise argument. For a list of options use !DeceiveLookup Agents / !DeceiveLookup Gadgets / !DeceiveLookup Chips / !DeceiveLookup Dictionary'
    write_lookup_to_file(result)


def main():
    # sys.argv[1:]
    args = []
    with open(f'{localDirectory}\\DeceiveLookup.txt', "r") as lookupFile:
        args = lookupFile.readline().split()

    with open(f'{localDirectory}\\DeceiveLookupLog.txt', "a+") as log:
        log.write(f'{args}')
        log.write('\n')

    lookup(args)


print(minimise_name("Yu-Mi"))
print(minimise_name('yumi'))
print(determine_likeness('yumi', ["Yu-Mi"]))


main()