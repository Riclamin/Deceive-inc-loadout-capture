## 0.5.1.5 17 Nov 2023
- As per usual, forgot to include the firebot setup to include the commands..


## 0.5.0.5 16 Nov 2023
- Added the "UpdateCurrentLoadout.py" script to update a currentloadout file using a command. 
- removed unnecessary imports from CaptureLoadout.py
- moved determine_likeness function to LoadData.py to reuse the logic instead of implementing it twice in different locations.


### Balance changes
- Added descriptions for each tier of the npcs to the Dictionary. 
- Added descriptions for catgirl-tech as well as shield-juggling.

## 0.4.2.4 12 Nov 2023
- Resolved a bug in DeceiveLookup.py, where an import was missing from the minor release build, resulting in nothing being looked up. 


## 0.4.1.4: 11 Nov 2023
- Updated the firebot setup to actually reflect the changes in this minor release.

## 0.4.0.4: 11 Nov 2023
- The Lookup command suffered from the fact that the script did not take a consistent amount of time to retrieve the answer in time for firebot. This sometimes led to the situation where firebot would assume an answer was ready and replied with the query instead. Twitch user @Nescauzitos suggested to change the setup so that a program is run instead. Another issue with the previous setup was that the keybinds required ctrl. Since this is the standard keybind for most gamers to crouch, this could cause the lookup to randomly make you crouch. This is resolved through the following changes:
    - LoadoutRandom.bat and GenerateRandomLoadout.py now generate a random loadout
    - Loadout.bat and CaptureLoadout.py now handle the capturing of the current loadout and write to file.
    - Lookup.bat and DeceiveLookup.py now handle the lookup. 

### Balance changes
- Courtesy of Discord user @1stGlitch, the agent section of the balance sheet have been updated with a lot of information.


## 0.3.3.3: 08 Nov 2023
- Fixed a bug where the dynamically read lists would include the backup values. Upon analysing the current loadout, this would result in the script trying to read files that did not exist.
- optimised a small section of code that minimised the names for easier comparison.

## 0.3.2.3: 08 Nov 2023
- made it so that the options list is dynamically read from the stats files instead of keeping track of the options in two separate places.

### Balance changes:
- Added Snapshot (from hacktrap) and Echo (Xiu p3) to the Dictionary.


## 0.3.1: 07 Nov 2023
- Added functionality so that lookups do not need to be case sensitive anymore. Shorthand should also work, as long as it can uniquely identify one option from the list of agents/weapons/expertises/passives/gadgets/terms. examples:
    - yumi works instead of Yu-Mi
    - cav works instead of Cavaliere
    - dr works for ReconDrone
    - q works for Squire 


## 0.3: 07 Nov 2023
- Added version numbers
- Added a second script to automatically check for Balance updates (and download them if they exist) on startup. This script is automatically run on startup of `main.py`. This will also notify the user of a Major, Minor, Build, and Balance updates in the terminal window.
    - A Major update means a significant change or large feature that was added. e.g. once the twitch overlay is working the version would probably switch to 1.x
    - a Minor update means a small feature was added to the codebase. This number resets to 0 upon a major release.
    - a Build update means that no features were added, but a bugfix was performed. this number resets to 0 upon a minor or major release.
    - a Balance update means that the info in the database has been updated. It usually will follow shortly after a balance patch on the game, but can also be done more often when undocumented changes have been found, or when information is added or restructured. This number will not reset and keep counting up over releases.
- Added changelog
- removed streamfiles (temp files for bot) from directory and added to `.gitignore`.

___

## 0.2: 05 Nov 2023
- Added option to lookup information on loadouts that are not in use right now, as well as status effects, and other terms.
- Collapsed Loadout commands from 0.1 into a single firebot command called !loadout.
- Added option !loadout command to generate random loadouts, which can be used for challenge runs.
- Readme has been made more clear.
- Updated Firebot setup file to be much easier to install.
- Many bug fixes.

___

## 0.1: 27 Oct 2023
This is the initial release of application on github.
- Can be used to capture loadout of deceive inc by using ctrl u while it is running.
- included firebot setup file as a chatbot to read the output from the python script since the overlay part is going to take a long time to do.
- Included assets that are used to analyse the screen for the loadout. 
- Added csv files based on the spreadsheet (https://docs.google.com/spreadsheets/d/1aYV99mVfnWHLFT20lRHOWC98bvjgi-s0FnHAea43L6E/edit#gid=1972426151) provided by discord user @azazel98x 