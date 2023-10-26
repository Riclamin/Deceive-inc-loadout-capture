Preparation:
Make sure to have python installed on your pc. 
Install the required libraries using command:
- pip install pyautogui pandas keyboard

Setup a chatbot to read the output file. A setup file is included for firebot: "Deceive loadout extension - firebot integration", which can be imported through settings > setups > import setup.
Make sure to update the path to the CurrentLoadout.txt file in the readfile effects for all of the commands. You can do this easily by opening the file with notepad or any other text edit program and replace all instances of "{Location of the Deceive Inc Local Screen Capture Folder}" with the actual path to the folder e.g. "C:\User\Documents\SomeFolder\Deceive inc loadout capture\".

How to use:

Run the script "main.py". During agent select, whenever you use a new build, make sure that you select the agent's class before (vanguard/tracker/disruptor/scoundrel) pressing ctrl+u to have the plugin analyse it. Otherwise it might not detect your weapon/expertise/passvie. It will screenshot your current screen and determine your loadout. This can take up to about 10 seconds, but you can do other stuff in the mean time. It will then export this loadout to the file "CurrentLoadout.txt". A bot can read from this file so that the information can be exported in chat through a chatbot for example.

Future additions:
- Add twitch overlay support such that viewers can just hover over your abilities to show the tooltips instead of having to use chat commands.
- add customisable hotkeys for capture.

Considering:
- Add support for disguise tier + extra info. 
- Replacing the screen capture with API calls, so that everything can be run in the cloud instead. Requires help from the game developer. 

