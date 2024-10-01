# ui file:
```
pyuic5 -x "/mnt/c/Users/noelu/Python Projects/PyQt GUI practice/QtDesigner_practice/dataset_gen_tool_GUI/dataset_gen_tool_v10.ui" -o guiskin_DEV2.py
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