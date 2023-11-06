Preparation:
1. Make sure to have python installed on your pc. Can be downloaded from: https://www.python.org/downloads/
2. Install the required libraries using command:
    - `pip install pyautogui pandas keyboard`
    - pyautogui is used to capture the screen.
    - pandas is used to easily read the csv files that contain the information.
    - keyboard is to listen to keybinds.
3. Setup a chatbot to read the output file. 
    - A setup file is included for firebot (https://firebot.app): "Deceive loadout extension - firebot integration", which can be imported through `settings > setups > import setup`. During the import of the setup file, you will be asked to give the filepath to the directory where this file is located as well. e.g. C:\Users\User\Documents\Deceive-Inc-Loadout-Capture. If you've already imported a previous version of the setup, I advise to first remove this setup through `settings > setups > remove setup` before importing the new one. 
    - If you're not using Firebot, there is a templateLoadoutFile included that explains shortly on which line of the "CurrentLoadout.txt" file each of the information will be exported.

How to use:

1. Open Windows powershell or Commandprompt in the current directory, which can be done by shift-rightclicking the background in the directory and run:
    - `& python main.py`
2. Run a Firebot instance on the pc where you play deceive inc. 
3. Use any of the following keybinds:
    - ctrl+u During agent select, whenever you use a new build, make sure that you select the agent's class before (vanguard/tracker/disruptor/scoundrel) pressing ctrl+u to have the plugin analyse it. Otherwise it might not detect your weapon/expertise/passive. It will screenshot your current screen and determine your loadout. This can take up to about 10 seconds, but the process isn't blocking, so you can do other stuff in the mean time. It will then export this loadout to the file "CurrentLoadout.txt". A bot can read from this file so that the information can be exported in chat through a chatbot for example.
    - ctrl+i will export a random loadout to the "randomLoadout.txt" file. This could be used for a challenge run for example. It will randomise all aspects of a loadout including agent, weapon, expertise, passive, gadgets, chips. 
    - ctrl+l (lowercase L) to do a lookup for a specific ability. The Firebot setup has a command !DeceiveLookup that uses this keybind to read from the "DeceiveLookup.txt" file. It will try to determine what is being asked and output the result back into the file. The same file can then be read again by the chatbot to output the response into chat. 
4. To stop the script, go to the powershell / commandprompt window and press ctrl+c to stop the script.



Future additions:
- Add twitch overlay support such that viewers can just hover over your abilities to show the tooltips instead of having to use chat commands.
- add customisable hotkeys for capture.

Considering:
- Add support for disguise tier + extra info. 
- Replacing the screen capture with API calls, so that everything can be run in the cloud instead. Requires help from the game developer. 

