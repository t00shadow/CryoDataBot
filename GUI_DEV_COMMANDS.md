# installing packages
```
cat requirements.txt | xargs -n 1 -I {} pip install {} || echo "Failed to install {}"
```
This command will continue installing from requirements.txt even if a package fails to install. (pip install -r requirements.txt stops as soon as one package fails to install)

Explanation:
1. ```cat``` reads in requirements.txt and spits out its contents to standard output

2. pipe (```|```) redirects cat's output and sends it as input to xargs

3. ```xargs -n 1 -I {} pip install {}```
    - xargs is a command used to build and execute command lines from standard input.
        - -n 1: This option tells xargs to use one argument at a time from the input for each command execution.
    - This means for each line in the requirements.txt file (which is a package name), it will execute pip install \<package\> once per line.
        - -I {}: This option allows you to specify a placeholder ({}) in the command. xargs will replace {} with the current item being processed (each package name in this case).
        -   For example, if the current line in requirements.txt is numpy, it will replace {} with numpy in the pip install {} command.
    - pip install {}: This is the command that gets executed for each package. The {} is a placeholder that gets replaced by the package name from requirements.txt.
        - For example, it would run pip install numpy for a line containing numpy.

4. ```|| echo "Failed to install {}"```
    - || is a logical OR. runs the command to the right only if the left command fails
    - {} is the same placeholder from the left side of the ||
    - echo is the bash equivalent of print()

# ui file:
```
pyuic5 -x "/mnt/c/Users/noelu/Python Projects/PyQt GUI practice/QtDesigner_practice/dataset_gen_tool_GUI/dataset_gen_tool_v10.ui" -o guiskin_DEV2.py
```
updated command:
```
pyuic5 -x "/mnt/c/Users/noelu/CryoDataBot/dataset_gen_tool_v11_experimental_copy.ui" -o guiskin_DEV3.py
```
even more updated command:
```
pyuic5 -x "/mnt/c/Users/noelu/CryoDataBot/dataset_gen_tool_v12.ui" -o guiskin_DEV3_1.py
```

# resources:
```
pyrcc5 "/mnt/c/Users/noelu/Python Projects/PyQt GUI practice/QtDesigner_practice/dataset_gen_tool_GUI/resources.qrc" -o resources_rc.py
```


# for the other dialog window (WIP):
```
pyuic5 -x "/mnt/c/Users/noelu/CryoDataBot/label_manager_popup_EXP/label_manager_popup.ui" -o label_manager_popup_EXP/label_manager_popup.py
```

# which files to run?
Run ```main_gui_DEV3.py``` (or ```main_gui_DEV3_alt.py``` for page buttons on the side). 

```main_gui_DEV3.py``` imports ```guiskin_DEV2.py```. Do NOT modify ```guiskin_DEV2.py``` because any changes will be overwritten.





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






<!-- # Aside: proof that Jaccard index (GOF, VOF, wtv u wanna rename it) and Dice* are not independent
$$
\text{Jaccard (GOF, VOF, doesnt matter what you call intersect/union)} = \frac{|A \cap B|}{|A \cup B|} \\
\text{Dice*} = \frac{|A \cap B|}{|A| + |B|} \\
\text{(*actual Dice has a scaling factor of 2)} \\

\text{Dice*} = \frac{|A \cap B|}{|A| + |B|} = \frac{|A \cap B|}{|A \cup B| + |A \cap B|} \\
\frac{1}{\text{Jaccard}} = \frac{|A \cup B|}{|A \cap B|} = \frac{|A \cup B|}{|A \cap B|} + 1 - 1 = \frac{|A \cup B|}{|A \cap B|} + \frac{|A \cap B|}{|A \cap B|} - 1 = \frac{|A \cup B| + |A \cap B|}{|A \cap B|} - 1 = \frac{1}{\text{Dice*}} - 1 \\
\frac{1}{\text{Jaccard}} = \frac{1}{\text{Dice*}} - 1 \\
$$

<br>

$$
\text{Jaccard} = \frac{\text{Dice*}}{1 - \text{Dice*}} \\
$$

<br>

$$
\text{Dice*} = \frac{\text{Jaccard}}{1 + \text{Jaccard}} \\
$$





Example) For some fixed A and B. Say A = 100 and B = 100.
| Overlap % | Dice   | IoU     |
| --------- | ------ | ------- |
| 10%       | \~0.18 | \~0.095 |
| 50%       | \~0.67 | \~0.33  |
| 90%       | \~0.95 | \~0.82  | -->
