import os, pandas


localDirectory = os.getcwd()
AgentStatsDF = pandas.read_csv(f'{localDirectory}\Stats\AgentLoadoutStats.csv', index_col=0, names=["Agent","w1","w2","w3","e1","e2","e3","p1","p2","p3", "x"], sep=';')
GadgetStatsDF = pandas.read_csv(f'{localDirectory}\Stats\GadgetStats.csv', index_col=0, names=["Gadget","Stats","x"], sep = ';')
UpgradeChipStatsDF = pandas.read_csv(f'{localDirectory}\Stats\\UpgradeChipStats.csv', index_col=0, names=["Type","Grey", "Green", "Blue", "Purple", "Gold","x"], sep=';')
DictionaryDF = pandas.read_csv(f'{localDirectory}\Stats\\Dictionary.csv', index_col=0, names=["Term","Explanation"], sep=';')



Agents = AgentStatsDF.index.values.tolist()[1:-1] 
Weapons = ["w1", "w2", "w3"]
Expertises = ["e1", "e2", "e3"]
Passives = ["p1", "p2", "p3"]
Gadgets = GadgetStatsDF.index.values.tolist()[1:-1] 
UpgradeTiers = ["Grey", "Green", "Blue", "Purple", "Gold"]
UpgradeChips = UpgradeChipStatsDF.index.values.tolist()[1:-1] 
Dictionary = DictionaryDF.index.values.tolist()[1:] 


def determine_likeness(name, options):
    for option in options:
        minimised_name = minimise_name(name)
        minimised_option = minimise_name(option)
        if minimised_name in minimised_option or minimised_option == minimised_name: 
            return option
    return None


def minimise_name(name: str):
    return name.replace(' ', '').replace('-', '').replace('\n','').replace('"', '').lower()