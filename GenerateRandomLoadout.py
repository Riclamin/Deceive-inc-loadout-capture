import random, pandas, os, datetime
from checkForUpdates import check_for_updates
from LoadData import localDirectory, Agents, Gadgets, UpgradeChips

random.seed(datetime.datetime.now())

check_for_updates()

with open(f'{localDirectory}\\RandomLoadout.txt', "w+") as randomFile:
        randomFile.write(f'{random.choice(Agents)} w{random.randint(1,3)} e{random.randint(1,3)} p{random.randint(1,3)}, g: {random.sample(Gadgets,2)}, chips grey-gold: {random.sample(UpgradeChips,5)}')
        randomFile.flush