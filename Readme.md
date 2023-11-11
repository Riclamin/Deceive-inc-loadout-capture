## Preparation:
1. Make sure to have python installed on your pc. Can be downloaded from: https://www.python.org/downloads/
2. Install the required libraries using command:
    - `pip install pyautogui pandas keyboard opencv-python`
    - pyautogui is used to capture the screen.
    - pandas is used to easily read the csv files that contain the information.
    - keyboard is to listen to keybinds.
    - opencv-python is used to make sure the locating is done with a certain confidence score.
3. Setup a chatbot to read the output file. 
    - A setup file is included for firebot (https://firebot.app): "Deceive loadout extension - firebot integration", which can be imported through `settings > setups > import setup`. During the import of the setup file, you will be asked to give the filepath to the directory where this file is located as well. e.g. C:\Users\User\Documents\Deceive-Inc-Loadout-Capture. If you've already imported a previous version of the setup, I advise to first remove this setup through `settings > setups > remove setup` before importing the new one. 
    - If you're not using Firebot, there is a templateLoadoutFile included that explains shortly on which line of the "CurrentLoadout.txt" file each of the information will be exported.
4. Update the python location in the .bat files: loadout.bat, loadoutRandom.bat, and lookup.bat, as well as the location of the current folder
    - The standard location for python is already included in the files (C:/Python39/python.exe )

## How to use:
### versions 0.4 and after:
1. Run a Firebot instance on the pc where you play deceive inc
    - The firebot commands trigger the correct script to run for loadout capture, as well as performing lookups. To reduce stress on the gaming pc in a dual-pc setup, one could do a small optimisation by disabling the lookup command on the gaming pc and enable the command on the streaming pc. 
    - Scripts automatically check for Balance updates, and terminate afterwards, minimising the usage of cpu. The results are written back to file, which the chatbot will then read. 
    - To capture the current loadout, a hotkey can be selected in firebot to read the Loadout.bat program. ctrl u is included in the setup. 


### versions 0.3 and before:
1. Open Windows powershell or Commandprompt in the current directory, which can be done by shift-rightclicking the background in the directory and run:
    - `& python main.py`
    - Since version 0.3 balance updates are automatically downloaded whenever an update is pushed. The script will also inform you if there is a new major, minor or build release, but you'll have to download it from the github page yourself.
2. Run a Firebot instance on the pc where you play deceive inc. 
3. Use any of the following keybinds:
    - ctrl+u During agent select, whenever you use a new build, make sure that you select the agent's class before (vanguard/tracker/disruptor/scoundrel) pressing ctrl+u to have the plugin analyse it. Otherwise it might not detect your weapon/expertise/passive. It will screenshot your current screen and determine your loadout. This can take up to about 10 seconds, but the process isn't blocking, so you can do other stuff in the mean time. It will then export this loadout to the file "CurrentLoadout.txt". A bot can read from this file so that the information can be exported in chat through a chatbot for example.
    - ctrl+i will export a random loadout to the "randomLoadout.txt" file. This could be used for a challenge run for example. It will randomise all aspects of a loadout including agent, weapon, expertise, passive, gadgets, chips. 
    - ctrl+l (lowercase L) to do a lookup for a specific ability. The Firebot setup has a command !DeceiveLookup that uses this keybind to read from the "DeceiveLookup.txt" file. It will try to determine what is being asked and output the result back into the file. The same file can then be read again by the chatbot to output the response into chat. 
4. To stop the script, go to the powershell / commandprompt window and press ctrl+c to stop the script.

___

## known limitations:
Current loadout capture has some limitations. Most of these can be circumvented by using the lookup feature instead. However known limitations are:
- Currently assumes the game is being played at 1080p. Higher or lower resolutions may fail the loadout to be captured as the pixels are different than what is currently analysed in "assets".
- Assumes the game is being played without colourblind settings, or other settings that changes the colour of pixels. This will reduce the similarity between the assets and what is captured and likely result in the assets not being recognised. 

If there are any accessability issues currently not being considered, please let me know! Contact information is down below.

___

## Future additions:
- Add twitch overlay support such that viewers can just hover over your abilities to show the tooltips instead of having to use chat commands.
- add customisable hotkeys for capture.

### Considering:
- Add support for disguise tier + extra info. 
- Replacing the screen capture with API calls, so that everything can be run in the cloud instead. Requires help from the game developer. 

If you have any other features that you would love to see, please let me know! Contact information is down below.
___

## Contact information
If you want to get in touch with me the easiest way to do that is through the issues board here on github (https://github.com/Riclamin/Deceive-inc-loadout-capture/issues) or by letting me known on discord (@Riclamin). It may not be possible to send me a direct message on Discord if we don't share a server such as the official deceive inc discord (https://discord.com/invite/YfYGgjtsYc). 

___

## Versionfile(1.2.3.4) works as follows: 
1. Major release. A Major update means a significant change or large feature that was added. e.g. once the twitch overlay is working the version would probably switch to 1.x
2. Minor release. A Minor update means a small feature was added to the codebase. This number resets to 0 upon a major release.
3. Build version of minor release. A Build update means that no features were added, but a bugfix was performed. this number resets to 0 upon a minor or major release.
4. Balance version. During development will be updated regularly until everything is up to date with the current patch. Afterward should update once per patch unless undocumented changes are found, or when information is restructured. This number will not reset and keep counting up over releases.
