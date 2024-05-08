## 0.7.3.16 08 May 2024

### Balance changes
- updated values according to the hotfix patch notes of 7 may 2024: https://forums.tripwireinteractive.com/index.php?threads/post-jatimania-update.2340266/



## 0.7.3.15 22 April 2024

### Balance changes
- updated values according to the hotfix patch notes of 22 April 2024: https://forums.tripwireinteractive.com/index.php?threads/jatimania-hotfix.2340245/



## 0.7.3.14 13 April 2024

### Balance changes
- updated values according to the patch notes of 11 April 2024: https://forums.tripwireinteractive.com/index.php?threads/jatimania-is-here.2340232/



## 0.7.3.13 3 April 2024
- Updated art for Ace's p1 and p3.
- Some assets got updated during this update, so it's important to also update these if you were having trouble capturing some assets.


### Balance changes
- Updated all balance changes following from the hotfix patch on march 15th.
- Added health vial / consumable to dictionary
- added damage falloff explanation to dictionary



## 0.7.2.12 29 Feb 2024

### Balance changes
- Updated all relevant numbers and effects based on the patch notes that were released on the tripwire forums.
- Added damage falloff findings to the agent stats as well as the dictionary for an explanation.



## 0.7.2.11 13 Feb 2024
- Reduced the theshold for capturing various assets, as it seemed to be too high of a threshold. This caused failures in the comparing logic, making the plugin think that the asset was not on screen, even when it was.
- Some 1440p assets got updated during this update, so it's important to also update these if you were having trouble capturing the assets.

### Balance changes
- Added missing numbers to various characters, including but not limited to Chavez, Octo, Xiu.
- Added extra numbers and extra terms to dictionary


## 0.7.1.10 20 Dec 2023

### Balance Changes
- Included the term spypack, with synonym spycache into the dictionary.


## 0.7.1.9 20 Dec 2023

### Balance Changes
- Updated an incorrect number for squire e3.
- Updated grammar in a sentence for squire p2


## 0.7.1.8 15 Dec 2023
- Added a minor optimisation to capture agent loadout.


## 0.7.0.8 15 Dec 2023 
- Updated the loadout capture logic so that future lobby changes should not affect capture accuracy
- Added support for 1440p capturing (Make sure to update your config file).
    - included all assets for 1440p, and moved the 1080p assets to a different folder.




## 0.6.2.8 15 Dec 2023
- Fixed an error in the update command where it would update all chips to be of 'grey' tier, even though ti did show the correct values.


### Balance Changes
- Added cooldown for tripwires and shieldbrella.
- Added the fact that technicians can now open drawers.
- Added Ace p3 to list of abilities that can neutralize.
- included updated bounce pad cooldown from hotfix patch on 14 dec 2023

## 0.6.1.7 12 Dec 2023
### Balance Changes
- Updated all stats to reflect the patch notes.


## 0.6.1.6 05 Dec 2023
- There was a bug in config.py that prevented the file from being executed; and therefore none of the scripts would work either.
- Updated the readme to reflect some part of the setup that is not automatically updated for some reason. 


## 0.6.0.6 21 Nov 2023
- added a config file so that users can insert their own name for the lookup command. There are some more options included in the config file that are currently not used, but may be used in the future.
- Update the firebot setup file to reflect above change. 
- commented out more of the debugging functions that are now not visible during normal use anyways. 


### Balance changes
- In cooperation with Steam user Aevian Milotic333 we timed and tested most expertises to find missing numbers. As a result the AgentLoadout text for expertises and passives have been updated.
- Added some missing text to GadgetStats sheet.

___

## 0.5.2.5 17 Nov 2023
- When an agent was changed, the respective weapon expertise, and passives weren't correctly updated. This should now be resolved.
- Updated the Readme to give examples of the !UpdateLoadout command.


## 0.5.1.5 17 Nov 2023
- As per usual, forgot to include the firebot setup to include the commands..


## 0.5.0.5 16 Nov 2023
- Added the "UpdateCurrentLoadout.py" script to update a currentloadout file using a command. 
- removed unnecessary imports from CaptureLoadout.py
- moved determine_likeness function to LoadData.py to reuse the logic instead of implementing it twice in different locations.


### Balance changes
- Added descriptions for each tier of the npcs to the Dictionary. 
- Added descriptions for catgirl-tech as well as shield-juggling.

___

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

___

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