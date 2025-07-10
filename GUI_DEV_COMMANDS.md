# Table of Contents

- [Installing Packages](#installing-packages)
- [UI Files](#ui-file)
- [Resources](#resources)
- [Delete this section?](#for-the-other-dialog-window-wip)
- [Which files to run?](#which-files-to-run)
- [Building Executables](#building-executables)
- [Git](#git)
<!-- square brackets are the name of the table of contents entry, hashtags are the anchors to the sections below, all lowercase and replace spaces (and special charas like parens and question mark) with hyphens -->
<!-- https://stackoverflow.com/questions/2822089/how-to-link-to-part-of-the-same-document-in-markdown -->

All commands assume you're in the root directory btw (.../CryoDataBot). CryoDataBot with caps, not the lowercase cryodatabot folder.

# Installing Packages
```
pip install -r requirements.txt
```
In the future, use pipreqs instead of pip freeze to generate the requirements.txt.

# UI File:
```
pyuic5 -x "cryodatabot/src/frontend/ui_files/dataset_gen_tool_v12.ui" -o "cryodatabot/src/frontend/ui_files/guiskin_DEV3_1.py"
```

# Resources:
note: the newer stuff is done in main_gui.py directly (don't need resources_rc.py), but some svgs were missing when tested on other machines.

TODO: Some svgs are still missing on certain machines, not sure why. But figure out whether it's the code approach or the resources file appraoch and use the same appraoch for all.

# For the other dialog window (WIP):
```
pyuic5 -x "/mnt/c/Users/noelu/CryoDataBot/label_manager_popup_EXP/label_manager_popup.ui" -o label_manager_popup_EXP/label_manager_popup.py
```
Dont think this exists anymore, **delete**.

# Which files to run?
Run `run_gui.py`. It's the access point into main_gui.py. Since main_gui.py is in the cryodatabot folder now (ie a directory down from the root directory), running it gives some path errors (unless you load it as a module, but thats kinda annoying).





# BUILDING EXECUTABLES
(use a venv with only the necessary python modules. see requirements.txt. only need those 9)
## Windows version (.exe)
delete the empty __init__.py file in the root directory of the main gui file. Edit: nvm that wasn't the issue. Try adding __init__.py files back to every directory (besides the non code ones).

New command (run in powershell. INSIDE THE "cleanvenv" VIRTUAL ENVIRONMENT): 
```
pyinstaller.exe --onefile --windowed --name "CryoDataBot" --add-data="cryodatabot/src/frontend/svgs/*;cryodatabot/src/frontend/svgs/" .\run_gui.py
```
Pyinstaller only packs code files by default i think, so need to explicitly tell it to add the svg files.

[//]: # (Comment syntax, can replace parens with double quotes)
[//]: # (Same thing but with console. THe --windowed option disables console.)
[//]: # (pyinstaller.exe --onefile --name "CryoDataBot" --add-data="cryodatabot/src/frontend/svgs/*;cryodatabot/src/frontend/svgs/" .\run_gui.py)


[//]: # (This one's outdated, --add-data works while those other spec file hacks dont)
[//]: # (pyinstaller.exe --onefile --windowed --name "CryoDataBot" .\run_gui.py)


<!-- Other comment style, html comments -->
<!-- (rlyyyy OLD) run this command in powershell (windows version of pyinstaller gives exe, linux version of pyinstaller gives linix executable): ```pyinstaller.exe --onefile --windowed --paths="C:\\Users\\noelu\\CryoDataBot\\.venv\\Lib\\site-packages" --name "CryoDataBot" --icon "C:\\Users\\noelu\\Python Projects\\PyQt GUI practice\\QtDesigner_practice\\dataset_gen_tool_GUI\\app_icon2.ico" .\main_gui_DEV4.py``` -->

Once you run it once, you'll have .spec file. So can use the .spec file for future builds. Can also edit the .spec file and build from it instead. Make sure to backup the spec file if you manually edit it tho. Running the pyinstaller command while targeting a python file will overwrite the existing spec file.

The app icon .ico files are from PyQt GUI practice folder. Feel free to change the icon. Just download a new one or make one. Add the --icon option to the pyinstaller command.

### Edit: making a clean venv
pip install all the necessary packages and run the main gui file after importing one at a time. also check sys.modules.keys() or this approach: https://stackoverflow.com/questions/4858100/how-to-list-imported-modules

## Linux version (linux executable)
New command (run in wsl terminal. INSIDE THE "cleanvenv_linux" VIRTUAL ENVIRONMENT. ALSO, pip install pyinstaller in the venv. 

(My global pyinstaller version is only 6.11.1 and it uses my global python which is only 3.8.10. The venv is 3.10.16 and pyinstaller in the venv is 6.13.0. For the windows venv, i can just use the same pyinstaller.exe everywhere; it's version 6.13.0 too, but my windows python venv is 3.10.11)
```
pyinstaller --onefile --windowed --name "CryoDataBot" --add-data "cryodatabot/src/frontend/svgs/*:cryodatabot/src/frontend/svgs/" run_gui.py
```
Differences vs the windows version: 1) run in wsl terminal instead of powershell, 2) change pyinstaller.exe to pyinstaller, 3) change semi-colon to colon, 4) drop the .\ at the front of the file name

<!-- (rly OLD) ```pyinstaller --onefile --windowed --paths="C:\\Users\\noelu\\CryoDataBot\\.venv\\Lib\\site-packages" --name "CryoDataBot_LINUX" --icon "C:\\Users\\noelu\\Python Projects\\PyQt GUI practice\\QtDesigner_practice\\dataset_gen_tool_GUI\\app_icon2.ico" main_gui_DEV4.py``` -->

## Mac version (uhh TODO)



# Git
**IGNORE this if working on main branch OR if your branch is not behind the main branch (a branch can be both ahead and behind), which would ideally be the case.**

**Use the following ONLY IF NEEDED**

Copy file contents of temp branch but not the commit history (would clutter main branch's history) onto main branch.

Make sure on main branch

1. `git checkout main`

Delete current files (ignores untracked files)

2. `git rm -rf .`

Copy files from feature branch

3. `git checkout temp -- .`

Add all files to staging area (*this command might be unneeded* since prev command might just stage it for you)

4. `git add .`

New commit (only adds 1 commit to main instead of like 80)

5. `git commit -m "fixed last commit, make main branch match temp branch snapshot"`

Push to origin

6. push to origin using whatever is convenient (command line, github desktop, ...)
