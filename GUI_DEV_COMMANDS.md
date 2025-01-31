# ui file:
```
pyuic5 -x "/mnt/c/Users/noelu/Python Projects/PyQt GUI practice/QtDesigner_practice/dataset_gen_tool_GUI/dataset_gen_tool_v10.ui" -o guiskin_DEV2.py
```
updated command:
```
pyuic5 -x "/mnt/c/Users/noelu/CryoDataBot/dataset_gen_tool_v11_experimental_copy.ui" -o guiskin_DEV3.py
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





# FOR BUILDING EXE
delete the empty __init__.py file in the root directory of the main gui file.

run this command in powershell (windows version of pyinstaller gives exe, linux version of pyinstaller gives linix executable): ```pyinstaller.exe --onefile --windowed --paths="C:\\Users\\noelu\\CryoDataBot\\.venv\\Lib\\site-packages" --name "CryoDataBot" --icon "C:\\Users\\noelu\\Python Projects\\PyQt GUI practice\\QtDesigner_practice\\dataset_gen_tool_GUI\\app_icon2.ico" .\main_gui_DEV4.py```

Once you run it once, you'll have .spec file. So can use the .spec file for future builds.

The app icon .ico files are from PyQt GUI practice folder. Feel free to change the icon. Just download a new one or make one.

# linux version (linux executable)
```pyinstaller --onefile --windowed --paths="C:\\Users\\noelu\\CryoDataBot\\.venv\\Lib\\site-packages" --name "CryoDataBot_LINUX" --icon "C:\\Users\\noelu\\Python Projects\\PyQt GUI practice\\QtDesigner_practice\\dataset_gen_tool_GUI\\app_icon2.ico" main_gui_DEV4.py```