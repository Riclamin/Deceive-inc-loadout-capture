import os
from urllib.request import urlretrieve

def check_for_updates():
    githubURL = 'https://github.com/Riclamin/Deceive-inc-loadout-capture'

    AgentLoadoutStats = 'Stats/AgentLoadoutStats.csv'
    GadgetStats = 'Stats/GadgetStats.csv'
    UpgradeChipStats = 'Stats/UpgradeChipStats.csv'
    Dictionary = 'Stats/Dictionary.csv'

    rawgithubBase = 'https://raw.githubusercontent.com/Riclamin/Deceive-inc-loadout-capture/main/'
    githubVersionFileURL = 'https://raw.githubusercontent.com/Riclamin/Deceive-inc-loadout-capture/main/versionfile.txt'
    githubURL = 'https://github.com/Riclamin/Deceive-inc-loadout-capture'
    onlineVersionfile = 'onlineVersionfile.txt'
    versionfile = 'versionfile.txt'
    path, _ = urlretrieve(githubVersionFileURL,onlineVersionfile)


    onlineVersion = ''
    localVersion = ''
    with open(path) as githubVersionFile:
        onlineVersion = githubVersionFile.readline()

    with open(versionfile) as localversionFile:
        localVersion = localversionFile.readline()

    [onlineMajor,onlineMinor,onlineBuild,onlineBalance] = onlineVersion.split('.')
    [localMajor,localMinor,localBuild,localBalance] = localVersion.split('.')

    if onlineMajor > localMajor:
        print(f'a new major release is available on the github page: {githubURL}')
    elif onlineMinor > localMinor:
        print(f'a new minor release is available on the github page: {githubURL}')
    elif onlineBuild > localBuild:
        print(f'a new build is available on the github page: {githubURL}')

    if onlineBalance > localBalance:
        print(f'balance changes available online. Downloading them now.')
        urlretrieve(rawgithubBase + AgentLoadoutStats, './' + AgentLoadoutStats)
        urlretrieve(rawgithubBase + GadgetStats, './' + GadgetStats)
        urlretrieve(rawgithubBase + UpgradeChipStats, './' + UpgradeChipStats)
        urlretrieve(rawgithubBase + Dictionary, './' + Dictionary)
        with open(versionfile, 'w+') as localversionFile:
            localversionFile.writelines([f'{localMajor}.{localMinor}.{localBuild}.{onlineBalance}'])
            
    os.remove(onlineVersionfile)