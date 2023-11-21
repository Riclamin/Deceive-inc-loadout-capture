from LoadData import localDirectory


configLines = []
with open ('{localDirectory}\\config.txt', 'r+') as config:
    configLines = config.readlines()



# loadoutCommand = '!Loadout'             # How your current loadout is called in your chatbot.
# updateLoadoutCommand = '!UpdateLoadout' # How your update command is called to update your current loadout in your chatbot.
lookupCommand = '!DeceiveLookup'        # How your lookup command is called to lookup some term / agent / stats. 
resolution = '1080p'                    # The resolution you play the game in. Different resolutions will require different assets. Currently resolutions other than 1080p are not supported.
captureDisguise = True                  # Whether the plugin should capture your current disguise tier. Currently not supported but included for possible future releases. Options: [True, False]
colourBlindMode = 'Off'                 # type of colourblindness. Currently not supported but included for possible future releasees. Options: ['Off', 'Deuteranopia', 'Protanopia', 'Tritanopia']
colourBlindIntensity = 0                # Intensity of colourblind filter. Currently not supported but included for possible future releases. Options: [0, 1, ..., 100]

if len(configLines) == 5:
    # loadoutCommand = configLines[0].split('#')[0].split('=')[1].strip()
    # updateLoadoutCommand = configLines[1].split('#')[0].split('=')[1].strip()
    lookupCommand = configLines[0].split('#')[0].split('=')[1].strip()
    resolution = configLines[1].split('#')[0].split('=')[1].strip()
    captureDisguise = configLines[2].split('#')[0].split('=')[1].strip() == 'True'
    colourBlindMode = configLines[3].split('#')[0].split('=')[1].strip()
    colourBlindIntensity = int(configLines[4].split('#')[0].split('=')[1].strip())