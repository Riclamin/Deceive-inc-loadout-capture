
##0.3: 07 Nov 2023
- Added version numbers
- Added a second script to automatically check for Balance updates (and download them if they exist) on startup. This script is automatically run on startup of `main.py`. This will also notify the user of a Major, Minor, Build, and Balance updates in the terminal window.
    - A Major update means a significant change or large feature that was added. e.g. once the twitch overlay is working the version would probably switch to 1.x
    - a Minor update means a small feature was added to the codebase. This number resets to 0 upon a major release.
    - a Build update means that no features were added, but a bugfix was performed. this number resets to 0 upon a minor or major release.
    - a Balance update means that the info in the database has been updated. It usually will follow shortly after a balance patch on the game, but can also be done more often when undocumented changes have been found, or when information is added or restructured. This number will not reset and keep counting up over releases.
- Added changelog
- removed streamfiles (temp files for bot) from directory and added to `.gitignore`.


##0.2: 05 Nov 2023
- Added option to lookup information on loadouts that are not in use right now, as well as status effects, and other terms.
- Collapsed Loadout commands from 0.1 into a single firebot command called !loadout.
- Added option !loadout command to generate random loadouts, which can be used for challenge runs.
- Readme has been made more clear.
- Updated Firebot setup file to be much easier to install.
- Many bug fixes.


##0.1: 27 Oct 2023
This is the initial release of application on github.
- Can be used to capture loadout of deceive inc by using ctrl u while it is running.
- included firebot setup file as a chatbot to read the output from the python script since the overlay part is going to take a long time to do.
- Included assets that are used to analyse the screen for the loadout. 
- Added csv files based on the spreadsheet (https://docs.google.com/spreadsheets/d/1aYV99mVfnWHLFT20lRHOWC98bvjgi-s0FnHAea43L6E/edit#gid=1972426151) provided by discord user @azazel98x 