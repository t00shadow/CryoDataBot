# GUI TODO: 1) multithreading, 2) some ui/ux polish (previewing query), 2.5) finish missing functionalities (see #7), 3) organizing code better (clean up & organize these imports holy shit), 4) writings tests..., 5) progress bars (add them for all long steps, even downloading the csv), 6) splashscreen, 7) custom widgets (tagging, labeling widgets)
# semi-important TODO: CHECK EDGE CASES (empty search queries, either disallow or properly handle)
# NOTE: to understand the names of widgets, open the .ui file (oops forgot to copy it to this directory)
#       ^ maybeee means should name things better...
# TODO: rename the gui skin file to gui_skin_DEV and main gui to gui_main_DEV
# NOTE: dont worry abt writing "perfect" code rn, just get some dirty messy functioning code out and then revise after
# TODO: add typehints
# TODO: SIZEPOLICIES holy shit such a pain
# TODO: link resources correctly (check saved stack posts)

import sys
import pandas as pd
import os
import subprocess
import logging
from pathlib import Path
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtCore import QTextCodec
codec = QTextCodec.codecForName("UTF-8")

# from guiskin_DEV2_alt import Ui_MainWindow    # need the "Ui_" prefix
from guiskin_DEV2_alt_TEMP_DEMO_VERSION import Ui_MainWindow
from guiskin_DEV3 import Ui_MainWindow
#from guiskin import Ui_MainWindow

import GUI_custom_widgets.z_Tag_main_alt_allcode_v2 as TTEwidget2
from GUI_custom_widgets.LabelComboBox import LabelComboBox
from GUI_custom_widgets.LabelComboBox_v2 import LabelComboBox_v2
import GUI_custom_widgets.commaLineEdit as LabelLineEdit
from GUI_custom_widgets.animated_toggle import AnimatedToggle
from GUI_custom_widgets.popupDialog_alt import PopupDialog
from GUI_custom_widgets.easyCloseDialog import EasyCloseDialog
from my_logger import Handler


# from backend_core import fetch_sample_info, redundancy_filter, downloading_and_preprocessing, downloading_and_preprocessing_NO_GPU, generate_dataset
from backend_core import fetch_sample_info, redundancy_filter, downloading_and_preprocessing_NO_GPU2, generate_dataset   #! deleted cupy, actually works
# from backend_core import fetch_sample_info, redundancy_filter, downloading_and_preprocessing_NO_GPU, generate_dataset
# from backend_core import fetch_sample_info, redundancy_filter, downloading_and_preprocessing_NO_GPU_newversion, generate_dataset    #ignore the naming scheme between ..._newversion and ...2

from src.frontend_gui_assets.threading.test1_v2 import Worker
# from src.frontend_gui_assets.threading.test2_v2 import Worker


class NoEditDelegate(qtw.QStyledItemDelegate):    # only import stuff i need (change this at end of development)
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def createEditor(self, parent, option, index):
        # Return None to prevent editing
        return None


class QTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = qtw.QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)


class MainWindow(qtw.QMainWindow):    # Make sure the root widget/class is the right type (can check in designer or the .ui file)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('CryoDataBot')
        # self.resize(1000, 700)        # HOTFIX, functionally same as changing the size in the pyuic5 generated .py file but you aren't meant to edit that (can also just change size in designer, butttt it looks fine in designer). prob should involve screensize or smth, vanilla size is different than qt designer preview. prob cuz of screen resolution and/or dpi settings or smth. high dpi scaling can affect how pixels are rendered

        # ======== VARIABLES ========
        self.save_location = Path.cwd().as_posix()      # default
        self.labels = [[]]     # list of list of dicts, initialize as list of empty list
        self.label_dict_template = {'secondary_type': '', 'residue_type': '', 'atom_type': '', 'label': ''}
        self.main_dir_path = ""
        self.leftpanel_buttons = {}    # key, value = QPushButton, text().  Alternatively just use two lists

        #& QoL feature: stores results of each step. Use case: selected a different file but want to restore the filepath of the results of your current sesion. Relevant buttons: self.ui.resetDefaultVal_btn and self.ui.resetDefaultVal_btn_2. Note: these variables are only relevant for these buttons.
        #! might delete this functionality tho. EDIT: found out abt selectAll() and then insert() which preserves undo/redo history unlike selectText(). so might actually delete this in the next commit
        self.step1_results_path = None
        self.step2_results_path = None
        self.step3_results_path = None
        self.step4_results_path = None     # THIS one is currently unused. Would only be used by a summary page/message.

        # ======== SIGNALS AND SLOTS ========
        # TODO: CONSIDER organizing them by page? tho just added pages to the names so mb not
        # NVM i like the current setup better, organize by type then page. cuz each page has dif widgets so might miss one if go by page then type


        ### lineedits
        # self.ui.lineEdit.createStandardContextMenu()
        # self.ui.lineEdit.setClearButtonEnabled(True)
        # self.ui.lineEdit.setPlaceholderText("overwrote placeholder text via code")
        # self.ui.lineEdit_p1.setText(r"C:\Users\noelu\CryoDataBot\JUNK_TEST_FOLDER")
        self.ui.lineEdit_12.setPlaceholderText("[sample] AND [range_keyword: x TO y] AND [keyword]")
        self.ui.lineEdit_12.setText("")
        self.ui.lineEdit_p2.setText(self.save_location)     # default save location for the whole thing
        # TODO: enable elide for all filepath text fields

        ### buttons
        #? Home (page 0)
        self.ui.main_save_path_btn.clicked.connect(lambda: self.browse_folder(page="home"))
        #? Quickstart (page 1)
        # self.ui.pushButton_p1.clicked.connect(lambda: self.browse_folder(page="quick"))
        # self.ui.pushButton_p1_2.clicked.connect(lambda: self.ui.statusbar.showMessage("query (preview): " + self.parseQuery(page="quick")))    # intentionally didnt add time limit for this message so users can take their time to read it
        self.ui.pushButton_p1_3.clicked.connect(self.gen_dataset_quick)
        #? Fetch Metadata (page 2) - Step 1
        self.ui.pushButton_p2.clicked.connect(lambda: self.browse_folder(page="step1"))
        self.ui.pushButton_p2_2.clicked.connect(self.fetch_sample_info)
        #? Download and Preprocess (page 3) - Step 2 (step 3 abstracted away)
        self.ui.pushButton_p3.clicked.connect(lambda: self.browse_folder(page="step2"))
        self.ui.resetDefaultVal_btn.clicked.connect(lambda: self.ui.lineEdit_p3.setText(self.step1_results_path))
        self.ui.pushButton_p3_4.clicked.connect(self.redund_filter)
        #? Generate Dataset (page 4) - Step 4
        self.ui.pushButton_p3_2.clicked.connect(lambda: self.browse_folder(page="step4"))
        self.ui.resetDefaultVal_btn_2.clicked.connect(lambda: self.ui.lineEdit_p3_2.setText(self.step3_results_path))

        
        # make these tool tips in designer in rich text on a testpage, and then copy paste them from the generated ui code, and then delete the test page at runtime
        self.ui.qScoreInfo_btn.clicked.connect(lambda: self.show_tooltip_on_click("QScore: \ndescrip... *consider using richtext (if possible) to have colors and bold, italics, etc"))
        self.ui.mmfInfo_btn.clicked.connect(lambda: self.show_tooltip_on_click("Our calculated metric: ...what this means..."))
        self.ui.simInfo_btn.clicked.connect(lambda: self.show_tooltip_on_click("Similarity: a measure of how similar _ are. 100 is most similar, 0 is least similar"))
        # rename these info buttons in designer. Use rich text if possible
        self.ui.qScoreInfo_btn_2.clicked.connect(lambda: self.show_tooltip_on_click("This step fetches metadata from EMDB. If you already have a .csv file with the columns: emdb_id, resolution, fitted_pdbs, you can skip this step."))
        self.ui.qScoreInfo_btn_3.clicked.connect(lambda: self.show_tooltip_on_click("This step preprocesses... NOTE: Maps and models are downloaded in this step."))
        self.ui.qScoreInfo_btn_6.clicked.connect(lambda: self.show_tooltip_on_click("Create labels for your dataset. Add groups to separate your labels. Select a cube size. Choose how to divide your dataset between testing, training, and validation"))
        self.ui.qScoreInfo_btn_5.clicked.connect(lambda: self.show_tooltip_on_click("Quickly generate datasets."))


        self.ui.clearQScore_btn.clicked.connect(lambda: self.ui.qScoreDoubleSpinBox.setValue(0))  # make these global vars above?, since may be used in 2 dif places
        self.ui.clearMMF_btn.clicked.connect(lambda: self.ui.mapModelFitnessSpinBox.setValue(0))
        self.ui.clearSim_btn.clicked.connect(lambda: self.ui.similaritySpinBox.setValue(0))
        # Generate Datasets (page 4)
        self.ui.pushButton_p4_2.clicked.connect(self.gen_ds)


        ### QTreeWidget
        self.ui.addgroup_btn.clicked.connect(self.add_group_w_del_btn)
        self.ui.addlabel_btn.clicked.connect(self.add_label_custom)
        #  clear the initial junk from the qtreewidget
        self.ui.treeWidget_p4.clear()
        # self.ui.treeWidget_p4.setHeaderLabel(None)    # makes only first column's header empty
        self.ui.treeWidget_p4.setHeaderLabels([None, "Secondary structure", "Residue(s)", "Atom(s)", None])
        self.ui.treeWidget_p4.setColumnWidth(1, 150)
        self.ui.treeWidget_p4.setColumnWidth(2, 150)
        self.ui.treeWidget_p4.setColumnWidth(3, 150)
        self.ui.treeWidget_p4.setColumnWidth(4, 50)
        self.ui.treeWidget_p4.header().setSectionResizeMode(qtw.QHeaderView.Stretch)   # TODO: figure out how to keep last column fixed width
        self.ui.addlabel_btn.setDisabled(True)
        self.add_group_w_del_btn()
        self.add_label_custom()


        ### Spinboxes
        # name aliases (less lines to change zzz)
        self.ui.spinBox = self.ui.training_spinBox
        self.ui.spinBox_2 = self.ui.testing_spinBox
        self.ui.spinBox_3 = self.ui.validation_spinBox

        self.ui.spinBox.valueChanged.connect(self.on_spin_box1_changed)
        self.ui.spinBox_2.valueChanged.connect(self.on_spin_box2_changed)
        self.ui.spinBox_3.valueChanged.connect(self.on_spin_box3_changed)



        ### custom query TextEdit widget
        # # page 1
        # self.querywidget = TTEwidget2.TagTextEdit()
        # self.ui.A4_queryBox.layout().addWidget(self.querywidget)
        # self.querywidget.setMaximumHeight(200)
        # # page 2
        self.querywidget2 = TTEwidget2.TagTextEdit()
        # self.ui.B2_queryBox.layout().addWidget(self.querywidget2)
        self.ui.B_enterQuery.layout().insertWidget(3, self.querywidget2)
        self.querywidget2.setMaximumHeight(200)

        ## status bar      (page numbers refer to the signals here. status bar is almost always the slot)
        # page 1
        # self.ui.lineEdit_p1.textEdited['QString'].connect(self.ui.statusbar.showMessage)
        # self.querywidget.tagTextEdited.connect(self.ui.statusbar.showMessage)
        #self.ui.lineEdit_p1.textEdited.connect(self.ui.statusbar.showMessage)     # works without the ['QString'], look into why
        #self.querywidget.tagTextEdited.connect(print)
        # page 2
        self.ui.lineEdit_p2.textEdited['QString'].connect(self.ui.statusbar.showMessage)
        self.querywidget2.tagTextEdited.connect(self.ui.statusbar.showMessage)
        # self.userInputQuery = self.ui.lineEdit_2       # alias for easier swtching btwn dif search bars
        self.userInputQuery = self.ui.lineEdit_12
        self.ui.lineEdit_12.setClearButtonEnabled(True)
        self.userInputQuery.textEdited.connect(self.ui.statusbar.showMessage)
        # self.ui.lineEdit_12.textEdited.connect(self.ui.statusbar.showMessage)
        # self.previewQueryBtn = self.ui.validateQuery_btn
        self.previewQueryBtn = self.ui.pushButton_16
        self.previewQueryBtn.clicked.connect(lambda: self.ui.statusbar.showMessage("query (preview): " + self.parseQuery(page="step1")))


        ### left panel buttons (for splitter behavior)
        # add buttons and names to the dictr
        self.leftpanel_buttons[self.ui.sidebtn_0] = self.ui.sidebtn_0.text()
        self.leftpanel_buttons[self.ui.sidebtn_1] = self.ui.sidebtn_1.text()
        self.leftpanel_buttons[self.ui.sidebtn_2] = self.ui.sidebtn_2.text()
        self.leftpanel_buttons[self.ui.sidebtn_3] = self.ui.sidebtn_3.text()
        self.leftpanel_buttons[self.ui.sidebtn_4] = self.ui.sidebtn_4.text()
        self.leftpanel_buttons[self.ui.sidebtn_5] = self.ui.sidebtn_5.text()
        self.leftpanel_buttons[self.ui.sidebtn_6] = self.ui.sidebtn_6.text()
        print("dict:\n", self.leftpanel_buttons)
        print("keys:\n", self.leftpanel_buttons.keys())
        print("values:\n", self.leftpanel_buttons.values())
        self.ui.splitter.splitterMoved.connect(print)
        self.ui.sidebtn_5.clicked.connect(self.toggle_sidebar)
        self.ui.splitter.setCollapsible(0, False)
        self.ui.splitter.setCollapsible(1, False)



        '''
        ### logging shenanigans
        logTextBox = QTextEditLogger(self)
        # You can format what is printed to text box
        logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(logTextBox)
        # You can control the logging level
        logging.getLogger().setLevel(logging.DEBUG)
        self.ui.sidebar.layout().insertWidget(0, logTextBox.widget)
        # Remove the placeholder widget via code (prob better to manually remove this in the ui file to reduce startup time)
        self.ui.sidebar.layout().removeWidget(self.ui.logsWidget)
        self.ui.logsWidget.deleteLater()
        self.ui.logsWidget = None
        '''

        ### TEMPORARY, THESE ARE COSMETIC CHANGES FOR TAKING NICER PICTURES
        # =====================================================
        self.ui.label_18.setText("")
        self.ui.plainTextEdit_2.setPlainText("\nThis page is still a work in progress. Migrating some stuff here.\nLikely will add old sessions here (similar to ChimeraX)")
        self.ui.plainTextEdit_2.setStyleSheet("border:none")
        self.ui.textEdit.setText("query preview (temporarily disabled)")
        self.ui.sidebtn_5.setHidden(True)    # holy shit setHidden is so much more convenient
        self.ui.sidebtn_6.setHidden(True)
        self.ui.B2_queryBox.layout().removeWidget(self.ui.widget_7)
        try:
            self.ui.widget_7.deleteLater()
            self.ui.widget_7 = None
        except Exception as e:
            print("idk why there'd ever be one but here u go:", e)
        self.ui.B2_queryBox.layout().removeWidget(self.querywidget2)
        self.querywidget2.deleteLater()
        self.querywidget2 = None
        # self.ui.baseLayer_3.setTitle("Preprocessing")
        self.ui.B_refineCSV.setTitle("Filters")
        self.ui.pushButton_p3_4.setText("Preprocess")
        self.ui.pushButton_p2_2.setText("Search")
        self.ui.statusbar.showMessage("example status bar message")

        # self.ui.lineEdit_p1_2.findChild(qtw.QToolButton).setIcon(qtg.QIcon(r"GUI_custom_widgets/svgs/clear_small-svgrepo-com.svg"))
        self.ui.lineEdit_p3_2.findChild(qtw.QToolButton).setIcon(qtg.QIcon(r"GUI_custom_widgets/svgs/clear_small-svgrepo-com.svg"))

        self.ui.qScoreDoubleSpinBox.setDecimals(3)   #figured this out my making a new form in qtdesigner with just 2 spinboxes (one w/ the default 2 decimal places and one changed to 3, then looked at Form > View python code)
        # ...setMaximum(...) was done in the guiskin file, hence why it's not here
        self.ui.qScoreDoubleSpinBox.setMinimum(-1.0)   # qscores < 0 are bad, but giving users more flexibility in case they have some usecase
        self.ui.qScoreDoubleSpinBox.setSingleStep(0.001)
        self.ui.similaritySpinBox.setValue(0)    # new default value, equivalent to changing it in qt designer
        self.ui.training_spinBox.setValue(80)
        self.ui.testing_spinBox.setValue(10)
        self.ui.validation_spinBox.setValue(10)

        # hide progress bars initially
        self.ui.progressBar_p4_2.hide()    # name's backwards. This one is unnecessary in most cases, even long metadata queries take just a few seconds. Could delete it.     <-- fetch metadata page
        # add a progressbar to the preprocess page since will move downloading maps and models to that page
        self.ui.progressBar_p4.hide()      #   <--- gen dataset page
        # ===================================================== 


        # Fancy Checkbox/Togglebox
        mainToggle = AnimatedToggle()
        secondaryToggle = AnimatedToggle(
                checked_color="#FFB000",
                pulse_checked_color="#44FFB000"
        )
        mainToggle.setFixedSize(mainToggle.sizeHint())
        secondaryToggle.setFixedSize(mainToggle.sizeHint())

        self.ui.widget_9.layout().addWidget(qtw.QLabel("Main Toggle"))
        self.ui.widget_9.layout().addWidget(mainToggle)

        self.ui.widget_9.layout().addWidget(qtw.QLabel("Secondary Toggle"))
        self.ui.widget_9.layout().addWidget(secondaryToggle)

        mainToggle.stateChanged.connect(secondaryToggle.setChecked)    # lol its THAT easy



        ### tabbar tab colors
        # self.ui.tabWidget.tabBar().setTabTextColor(1, qtg.QColor(255, 0, 0, 127))    # mid solution, gets overwritten by the QSS. could do the styling with pure code but dont think u can set bg color

        ### reorder this code later btw (move all formatting stuff to top and signal/slots after)
        # TODO: fix the first column's name in label manager (space chara doesnt work, try an invisible chara)


        ### NoEditDelegate (for label manager)
        # # Set the delegate for specific cells
        # self.ui.treeWidget_p4.setItemDelegateForColumn(0, NoEditDelegate(self))


        # TODO: get fullsize to scale based on largest page (WIP)
        # self.ui.page2.layout().setSizeConstraint(1)
        # self.ui.page3.layout().setSizeConstraint(1)
        # self.ui.page4.layout().setSizeConstraint(1)
        # # self.ui.tab.layout().setSizeConstraint(1)   # theres's no layout set on the test page lol (intentional)

        self.ui.stackedWidget.setCurrentIndex(0)     # choose starting page

        # do this in designer, but currently just testing dif font sizes
        # self.ui.sidebtn_0.setFont(qtg.QFont("Times", 20))
        # self.ui.sidebtn_1.setFont(qtg.QFont("Times", 20))
        # self.ui.sidebtn_2.setFont(qtg.QFont("Times", 20))
        # self.ui.sidebtn_3.setFont(qtg.QFont("Times", 20))
        # self.ui.sidebtn_4.setFont(qtg.QFont("Times", 20))
        # self.ui.sidebtn_5.setFont(qtg.QFont("Times", 20))
        # self.ui.sidebtn_6.setFont(qtg.QFont("Times", 20))
        # self.ui.leftpanel.setMaximumWidth(180)

        self.ui.sidebtn_0.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.sidebtn_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.sidebtn_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.sidebtn_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.sidebtn_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.sidebtn_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))
        self.ui.sidebtn_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(6))

        self.ui.sidebtn_0.clicked.connect(self.uncheck_other_buttons)
        self.ui.sidebtn_0.setChecked(True)     # match starting page
        self.ui.sidebtn_1.clicked.connect(self.uncheck_other_buttons)
        # self.ui.sidebtn_1.setChecked(True)
        self.ui.sidebtn_2.clicked.connect(self.uncheck_other_buttons)
        self.ui.sidebtn_3.clicked.connect(self.uncheck_other_buttons)
        self.ui.sidebtn_4.clicked.connect(self.uncheck_other_buttons)
        self.ui.sidebtn_5.clicked.connect(self.uncheck_other_buttons)
        self.ui.sidebtn_6.clicked.connect(self.uncheck_other_buttons)

        # self.ui.statusbar.

        # Set the default cursor for all buttons (faster than manually doing in designer)
        self.set_cursor_for_buttons()

        self.setup_logger()

        # Your code ends here
        self.show()




    #& ===== Custom Functions ======================

    #? General functions
    def set_cursor_for_buttons(self):
        # Iterate through all children and set the cursor for buttons
        for btn in self.findChildren(qtw.QPushButton):
            btn.setCursor(qtc.Qt.PointingHandCursor)

    # TODO: consider switching to a popup menu. Have something like that already (the dialog box when deleting labels)
    def show_tooltip_on_click(self, message: str):
        button = self.sender()
        qtw.QToolTip.showText(button.mapToGlobal(qtc.QPoint(15, -10)), message, button)


    #? Sidebar functions
    def collapse_leftpanel(self):
        """Collapse sidebar by hiding button text, showing only icons."""
        self.ui.leftpanel.resize(self.ui.leftpanel.minimumWidth(), self.ui.leftpanel.height())
        for button in self.leftpanel_buttons.keys():
            button.setText("")  # Hide the text
        print("collapsed")
        print(self.ui.leftpanel.width(), self.ui.leftpanel.height())
    
    def expand_leftpanel(self):
        """Expand sidebar by showing button text along with icons."""
        self.ui.leftpanel.resize(self.ui.leftpanel.maximumWidth(), self.ui.leftpanel.height())
        for button in self.leftpanel_buttons.keys():
            button.setText(self.leftpanel_buttons[button])  # Show the text
        print("expanded")
        print(self.ui.leftpanel.width(), self.ui.leftpanel.height())

    def toggle_sidebar(self):
        """Toggle sidebar collapse/expand manually using the button."""
        print(self.ui.leftpanel.width())
        print(self.ui.leftpanel.baseSize)
        if self.ui.leftpanel.width() < self.ui.leftpanel.maximumWidth():   # seems like might be a sizepolicy issue
            self.expand_leftpanel()
        else:
            self.collapse_leftpanel()

    # for left panel. maybe store btns and pages in a lookup table/dictionary so can relate them easier
    def uncheck_other_buttons(self):
        # set all to false and then set the sender to true
        self.ui.sidebtn_0.setChecked(False)
        self.ui.sidebtn_1.setChecked(False)
        self.ui.sidebtn_2.setChecked(False)
        self.ui.sidebtn_3.setChecked(False)
        self.ui.sidebtn_4.setChecked(False)
        self.ui.sidebtn_5.setChecked(False)
        self.ui.sidebtn_6.setChecked(False)
        self.sender().setChecked(True)


    # makes the CryoDataBot main directory at user specified location
    # lowkey this is unneeded if u use os.makedirs in the other steps
    # ideas for helping visually clue viewers in that it's only needs to be set once, is having it greyed out, and then clicking a gear button to trigger a dialog window to edit it. or having a dropdown and then gear icon again idk
    # OR make an inital page (like vscodes home page thing or chimeras, that asks users to select a home save folder upon first launch (stores it some json or smth))
    
    #? File management functions
    # TODO: small bug, if no folder is selected, it becomes just "CryoDataBot. like as the absolute path lol. just use os.getcwd or wtv
    def make_main_dir(self, dir_path):
        print("make_main_dir fxn triggered")
        # https://stackoverflow.com/questions/273192/how-do-i-create-a-directory-and-any-missing-parent-directories
        # switch to pathlib
        # already tested it in the "temp.py" file
        try:
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
        except Exception as error:
            print("An exception occurred:", error)    # TODO: switch to a logger statement

        # this code looks kinda gross
    def browse_folder(self, page="home"):
        #? should adopt a more modular approach to mapping fxns to modules. create a dictionary of mappings are the start of the program? Or adopt the MVC design pattern
        if page == "home":
            filepath = qtw.QFileDialog.getExistingDirectory(self, caption='Select Folder')
            if not filepath:
                print("no directory selected")
                return
            self.ui.main_save_path_lineedit.setText(filepath)     # gui visual update
            self.save_location = filepath                            # store the value
            # reflect the change on the other page
            self.ui.lineEdit_p2.setText(filepath)        # should maybe update gui values differently, like listen for changes. Look at how MVC design pattern does it
        elif page == "quick":
            filepath = qtw.QFileDialog.getExistingDirectory(self, caption='Select Folder')
            if not filepath:
                print("no directory selected")
                return
            self.ui.lineEdit_p1.setText(filepath)   # seems the name of this widget changed or was deleted
        elif page == "step1":
            filepath = qtw.QFileDialog.getExistingDirectory(self, caption='Select Folder')
            if not filepath:
                print("no directory selected")
                return
            self.ui.lineEdit_p2.setText(filepath)     # gui visual update
            self.save_location = filepath                # store the value
            # reflect the change on the other page
            self.ui.main_save_path_lineedit.setText(filepath)     # should maybe update gui values differently, like listen for changes. Look at how MVC design pattern does it
        elif page == "step2":
            filepath = qtw.QFileDialog.getOpenFileName(self, caption='Select File', filter="(*.csv)")[0]    # returns a Tuple[str, str], keep first value
            if not filepath:
                print("no file selected")
                return
            #& This approach of selectAll() and then insert() preserves undo/redo history as compared to setText(). If make the folder selection lineedits editable too, adopt this approach for them too. For that u need a way to verify the folder exists, kinda like vscode select an interpreter typa thing.
            # self.ui.lineEdit_p3.setText(filepath)
            self.ui.lineEdit_p3.selectAll()
            self.ui.lineEdit_p3.insert(filepath)
        elif page == "step4":
            filepath = qtw.QFileDialog.getOpenFileName(self, caption='Select File', filter="(*.csv)")[0]
            if not filepath:
                print("no file selected")
                return
            # self.ui.lineEdit_p3_2.setText(filepath)
            self.ui.lineEdit_p3_2.selectAll()
            self.ui.lineEdit_p3_2.insert(filepath)
        
        print("selected path:", filepath)     # debugging, shows up in console. Could consider displaying in gui's log too.
        self.ui.statusbar.showMessage(f"selected folder: {filepath}", 2000)    # if use textChanged instead of textEdited signal in lineEdit_22 to statusbar connection, can remove this line, since textChanged is emitted the text is change by users OR programmatically (textEdited is only emited when text is changed by users)
        self.main_dir_path = filepath       # this is just to store this value so make_main_dir() can access it later



    #! DELETE THIS LATER
    # junk fxn for testing signals and slots, can delete/comment out later
    def run_naive(self):
        userinput = self.ui.lineEdit.text()
        print("Running " + userinput)

    # def updateStatusBar(self, string):
    #     self.ui.statusBar.showMessage(string)



    #! rewrite for better usuability, pass in self.step1_results_path as a parameter, also need to pass in the widgets to display too, etc. dif for each step
    #& so like def handle_result(self, result, storage_var)
    #~ general helper fxn
    # def handle_result(self, result):
    #     # Store the result (downloaded file path)
    #     self.step1_results_path = result
    #     print(f"Download finished. File saved at: {self.step1_results_path}")

    #~ STEP 1: fetch_sample_info
    def fetch_sample_info(self) -> None:
        """
        Return value is ... Creates new files.

        Parameters
        ----------
        None
        """
        
        # if the save location is empty, do nothing
        #^ changed from self.ui.lineEdit_p2.text() to self.save_location to migrate closer to MVC design pattern
        if not self.save_location or not self.userInputQuery.text():    # technically empty search query is a valid query, but that's the whole database. kinda annoying when u accidently download the whole database
            print("nothing happens")
            return

        # make the dir only when you decide to download anything. might need to move this elsewhere
        self.make_main_dir(self.main_dir_path)

        query = self.userInputQuery.text()    # change this to the custom widget like in gen_dataset_quick()
        #processedstring = stringutil.process_string(query)   # TODO, concatenate array of keywords into a string (not sure how to implement and and or logic with keywords)
        processed_query = query     # placeholder
        # print(processed_query)
        save_path = self.save_location
        #TODO: put a try block here or some if statements to catch if btn is clicked with no parameters set
        
        self.ui.pushButton_p2_2.setDisabled(True)
        self.worker = Worker(fetch_sample_info.search_emdb, processed_query, save_path)
        self.worker.result_signal.connect(self.handle_result)
        #? CONSIDER putting the rest in a fxn cuz this is async. UPDATE: did it
        self.worker.start()

    # Helper fxn
    def handle_result(self, result):
        output_path = Path(result).as_posix()     # fixes forward/backward slash consistency
        print(f"Download finished. File saved at: {output_path}")
        self.ui.statusbar.showMessage(f"Download finished: {output_path}")
        self.ui.pushButton_p2_2.setEnabled(True)
        self.display_metadata_results(output_path)
        self.ui.lineEdit_p3.setText(output_path)   # set the path of the next step/page
        self.step1_results_path = output_path         # save the value so it can be restored easily if needed

    # Helper fxn for helper fxn
    def display_metadata_results(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        self.ui.textEdit.setPlainText(content)

    #^ Dinosaur
    # Helper function for gen_dataset_quick
    # Edit no longer parsing query, just asking users to follow EMDB search syntax and letting them preview results b4 downloading
    # implementing a parser would be kinda difficult and a waste of time given the amt of combinations and dif syntax to check
    # EMDB search engine was built using  Apache Solr server so check the SOlr query parser tutorial if wanna make a parser (https://solr.apache.org/guide/8_4/the-standard-query-parser.html).
    # Full list of EMDB query fields: https://www.ebi.ac.uk/emdb/documentation/search/fields
    # TLDR: faster to just provide a link to documentation and have users preview their results instead of wasting time on a complicated text validator.
    def parseQuery(self, page="quick"):
        if page == "quick":
            # return " AND ".join(self.querywidget.keywords)    # dont need to this cuz can directly access, basically global. instead just pass a string or int to distinguish which to use. tho maybe have 2 separate fxn is better cuz dont have to run an if statement each time u press the button
            return self.ui.lineEdit.text()
        elif page == "step1":
            # return " AND ".join(self.querywidget2.keywords)
            return self.userInputQuery.text()
        else:
            return ""     # spit out an error, this is only for the developer, not a runtime thing

    #^ This fxn doesnt do shit rn (recycle this dinosaur)
    # ignore this for now, this function is OUTDATED bc some backend stuff changed
    def gen_dataset_quick(self):
        # print(self.querywidget.junk_val)
        # print(self.querywidget.junk_arr)
        # print(self.querywidget.keywords)
        # print("main_new.QUERY:", main_new.QUERY)    # in this order to check initial hardcoded value, click button again to see updated value
        main_new_myversion.QUERY = self.parseQuery(page="quick")       # will likely need a simple parsing fxn here later
        print("query:", main_new_myversion.QUERY)
        save_path = self.ui.lineEdit_p1.text()
        print("save path:", save_path)
        if not save_path:        # empty string is "falsy". tho [if self.ui.lineEdit_22.text() == ""] might be more readable
            print("no save path selected")
            self.ui.statusbar.showMessage("Specify a save destination", 2000)
            # perform some other checks like verifying its a legit path
        elif not os.path.exists(save_path):
            print("invalid file path")
            self.ui.statusbar.showMessage("Folder does not exist", 2000)
        else:
            main_new_myversion.main(save_path, save_path)

    # DEMO version. To switch to normal just fetch the user input from the appropriate qwidgets (mostly lineedits) and pass the user input to the backend fxn.
    #~ STEP 2: redundancy_filter
    def redund_filter(self):
        # if the save location is empty, do nothing
        if not self.ui.lineEdit_p3.text():
            print("nothing happens 2")
            return

        step1_csv_path = self.ui.lineEdit_p3.text()
        q_thresh = self.ui.qScoreDoubleSpinBox.value()
        uni_thresh = self.ui.similaritySpinBox.value()
                
        self.ui.pushButton_p3_4.setDisabled(True)
        self.worker = Worker(redundancy_filter.filter_csv, step1_csv_path, q_thresh, uni_thresh)
        self.worker.result_signal.connect(self.handle_result_step2)
        #? CONSIDER putting the rest in a fxn cuz this is async. UPDATE: did it
        self.worker.start()

    def handle_result_step2(self, result):
        # Finish handling redundancy_filter
        output_path = Path(result).as_posix()     # fixes forward/backward slash consistency
        print(f"Metadata filtering finished. File(s) saved at: {output_path}")
        self.ui.statusbar.showMessage(f"Metadata filtering finished: {output_path}")
        # self.ui.pushButton_p3_4.setEnabled(True)     #! SAVE TILL AFTER STEP 3
        # self.ui.lineEdit_p3_2.setText(output_path)   # set the path of the next step/page       #! SAVE TILL AFTER STEP 3
        self.step2_results_path = output_path           # save the value so it can be restored easily if needed
        self.dl_and_preproc(output_path)    # no args yet, still WIP w/ some hardcoded constants


    #~ STEP 3: downloading & preprocessing (this is abstracted away for the user, uses the same button as step 2)
    def dl_and_preproc(self, file):
                # Step 3 (downloading and preprocessing)
        metadata_path = file
        temp = self.save_location
        raw_dir = temp + "/Raw"        # rewrite this with pathlib library
        if not os.path.exists(raw_dir):
            os.makedirs(raw_dir)
        print(raw_dir)
        overwrite = False
        give_map = True
        protein_tag_dist = 1
        map_threashold = 0.15
        vof_threashold = 0.25
        dice_threashold = 0.4

        self.worker = Worker(downloading_and_preprocessing_NO_GPU2.downloading_and_preprocessing, metadata_path, raw_dir, overwrite, give_map, protein_tag_dist, map_threashold, vof_threashold, dice_threashold)
        self.worker.result_signal.connect(self.handle_result_step3)
        self.worker.start()

    def handle_result_step3(self, result):
        # Finish handling downloading_and_preprocessing
        output_path = Path(result).as_posix()     # fixes forward/backward slash consistency
        print(f"Downloading and Downloading finished. File(s) saved at: {output_path}")
        self.ui.statusbar.showMessage(f"Downloading and Preprocessing finished: {output_path}")
        self.ui.pushButton_p3_4.setEnabled(True)
        self.ui.lineEdit_p3_2.setText(output_path)   # set the path of the next step/page
        self.step3_results_path = output_path           # save the value so it can be restored easily if needed

    #~ STEP 4: generate dataset
    # def gen_ds(self):
    # #     downloading_and_preprocessing.main()
    #     downloading_and_preprocessing_NO_GPU.main()
    #     generate_dataset.main()

    def gen_ds(self):
        # Step 3 (downloading and preprocessing)
        metadata_path = self.ui.lineEdit_p3_2.text()
        temp = self.save_location
        raw_dir = temp + "/Raw"
        if not os.path.exists(raw_dir):
            os.makedirs(raw_dir)
        print(raw_dir)
        overwrite = False
        give_map = True
        protein_tag_dist = 1
        map_threashold = 0.15
        vof_threashold = 0.25
        dice_threashold = 0.4
        #! comment out this line since bound step 3 to step 2's button instead
        # downloading_and_preprocessing_NO_GPU2.downloading_and_preprocessing(metadata_path, raw_dir, overwrite, give_map, protein_tag_dist, map_threashold, vof_threashold, dice_threashold)
        
        #! Was testing stuff earlier, but should be able to comment out print statements now
        # Step 4 (actually generating the labeled datasets)
        print("SEE HERE!!!")   #^ comment out later
        label_groups = []  # list of list of dicts?
        group_names = []
        for i in range(self.ui.treeWidget_p4.topLevelItemCount()):
            group = self.ui.treeWidget_p4.topLevelItem(i)
            print(group.text(0))   #^ comment out later
            group_names.append(group.text(0))

            for j in range(group.childCount()):
                label = group.child(j)
                secondary_struct_combo = self.ui.treeWidget_p4.itemWidget(label, 1)
                residues_combo = self.ui.treeWidget_p4.itemWidget(label, 2)
                atoms_lineedit = self.ui.treeWidget_p4.itemWidget(label, 3)
                print([secondary_struct_combo.currentText(), residues_combo.currentText(), atoms_lineedit.text(), j+1])    #^ comment out later
                label_groups.append([{'secondary_type': secondary_struct_combo.currentText(), 'residue_type': residues_combo.currentText(), 'atom_type': atoms_lineedit.text(), 'label': j+1}])
        print("DIVIDER")      #^ comment out later
        print(group_names)    #^ comment out later
        print(label_groups)   #^ comment out later
        # assert(False)       #^ uncomment to stop execution here
        # raw_path already defined above as raw_dir
        temp_sample_path = temp + "/Temp"
        if not os.path.exists(temp_sample_path):
            os.makedirs(temp_sample_path)
        sample_path = temp + "/Training"
        if not os.path.exists(sample_path):
            os.makedirs(sample_path)
        ratio_training = self.ui.training_spinBox.value() / 100
        ratio_testing = self.ui.testing_spinBox.value() / 100
        ratio_validation = self.ui.validation_spinBox.value() / 100
        ratio_t_t_v = [ratio_training, ratio_testing, ratio_validation]
        npy_size = self.ui.spinBox_4.value()
        extract_stride = 32
        atom_grid_radius = 1.5
        n_workers = 4

        self.ui.pushButton_p4_2.setDisabled(True)
        self.worker = Worker(generate_dataset.label_maps, label_groups, group_names, metadata_path, raw_dir, temp_sample_path, sample_path, ratio_t_t_v, npy_size, extract_stride, atom_grid_radius, n_workers)
        self.worker.result_signal.connect(self.handle_result_step4)
        self.worker.start()

    def handle_result_step4(self, result):
        # Finish handling downloading_and_preprocessing
        output_path = Path(result).as_posix()     # fixes forward/backward slash consistency
        print(f"Generating datasets finished. File(s) saved in directory: {output_path}")
        self.ui.statusbar.showMessage(f"Generating datasets finished. File(s) saved in directory: {output_path}")
        self.ui.pushButton_p4_2.setEnabled(True)
        self.step4_results_path = output_path           # save the value so it can be restored easily if needed

    # could use this, might need another page for summary stats? or display below labels
    def summary(self):    # summary stats or smth
        pass




    # Labels stuff
    def add_group(self):
        """Add a new group to the tree widget (top-level item, editable)."""
        group_name = f"Group {self.ui.treeWidget_p4.topLevelItemCount() + 1}"
        group_item = qtw.QTreeWidgetItem([group_name])      # no need to do [group_name, "", "", "", ""] since the other columns are blank
        group_item.setFlags(group_item.flags() | qtc.Qt.ItemIsEditable)  # Make the group item editable
        self.ui.treeWidget_p4.addTopLevelItem(group_item)

        # Automatically select the newly added group
        self.ui.treeWidget_p4.setCurrentItem(group_item)

    def add_group_w_del_btn(self):
        """Add a new group to the tree widget (top-level item, editable)."""
        group_name = f"Group {self.ui.treeWidget_p4.topLevelItemCount() + 1}"
        group_item = qtw.QTreeWidgetItem([group_name])      # no need to do [group_name, "", "", "", ""] since the other columns are blank
        group_item.setFlags(group_item.flags() | qtc.Qt.ItemIsEditable)  # Make the group item editable
        for i in range (1, 4):                                                  # Make the other columns in group row uneditable
            self.ui.treeWidget_p4.setItemDelegateForColumn(i, NoEditDelegate(self))
        self.ui.treeWidget_p4.addTopLevelItem(group_item)

        # Automatically select the newly added group
        self.ui.treeWidget_p4.setCurrentItem(group_item)
        group_delbtn = qtw.QPushButton()
        # group_delbtn.setIcon(qtg.QIcon(r"GUI_custom_widgets/svgs/browsefilesicon.png"))
        group_delbtn.setIcon(qtg.QIcon(r"GUI_custom_widgets/svgs/clear_inverse-svgrepo-com.svg"))
        group_delbtn.setFixedWidth(16)
        group_delbtn.setFixedHeight(16)
        group_delbtn.setStyleSheet("QPushButton {\n"
        "    background: transparent;\n"       # used to be a light gray
        "    border-radius: 8px;\n"
        "    color: white;\n"
        "}\n"
        "\n"
        "QPushButton:hover, QPushButton:pressed {\n"
        "    background: rgb(255, 0, 0);\n"
        "    border-image: url(GUI_custom_widgets/svgs/clear_inverse-svgrepo-com.svg);\n"  # border-image vs image?
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border: 2px solid transparent;\n"
        "}")
        group_delbtn.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        # group_delbtn.clicked.connect(self.delete_group)
        group_delbtn.clicked.connect(lambda: self.delete_btn_clicked("group"))
        self.ui.treeWidget_p4.setItemWidget(group_item, 4, group_delbtn)
        self.ui.treeWidget_p4.itemClicked.connect(lambda: print("CASE\n    OH"))

        self.ui.addlabel_btn.setEnabled(True)

    def add_label(self):
        """Add a label (subitem, editable) to the selected group or the parent group of the selected label."""
        selected_item = self.ui.treeWidget_p4.currentItem()

        # Check if a group or label is selected
        if selected_item is not None:                           # TODO: consider refactoring by inverting this if statement, removes a layer of if nesting
            if selected_item.parent() is None:
                # If a group is selected, add a label to the group
                group_item = selected_item
            else:
                # If a label is selected, add a label to its parent group
                group_item = selected_item.parent()

            label_name = f"Label {group_item.childCount() + 1}"
            label_item = qtw.QTreeWidgetItem([label_name])     # no need to do [label_name, "", "", "", ""] since the other columns are blank
            label_item.setFlags(label_item.flags() | qtc.Qt.ItemIsEditable)  # Allow editing of the label item
            group_item.addChild(label_item)
            group_item.setExpanded(True)  # Automatically expand the group when a label is added


    # =============================
    # Hierarchy:
    # group_item
    #   label_item
    #     -label name
    #     -secondary struct
    #     -residues
    #     -atoms
    #     -delete button
    #  label_item
    #  ...
    # group_item
    # ...
    # =============================
    def add_label_custom(self):
        """Add a label (subitem, editable) to the selected group or the parent group of the selected label."""
        selected_item = self.ui.treeWidget_p4.currentItem()    # to make this code reusable (and possible to move into a separate file, get the parent or the current widget, however that;s related to perhaps have to pass in self.smth else. alternatively leave it here but break up fxns into mutiple fxns with helpers where possible)

        # Check if a group or label is selected
        if selected_item is None:
            self.ui.statusbar.showMessage("Create a group first", 250)
            
            return
        
        if selected_item.parent() is None:
            # If a group is selected, add a label to the group
            group_item = selected_item
        else:
            # If a label is selected, add a label to its parent group
            group_item = selected_item.parent()

        label_name = f"Label {group_item.childCount() + 1}"
        label_name_widget = qtw.QLabel(label_name)
        # label_name_widget.setFlags(label_name_widget.flags() | qtc.Qt.ItemIsEditable)  # Allow editing of the label item
        
        label_item = qtw.QTreeWidgetItem(group_item, [label_name])
        label_item.setFlags(label_item.flags() | qtc.Qt.ItemIsEditable)  # DISABLE this and add a custom line edit with a completer
        group_item.addChild(label_item)

        # self.ui.treeWidget_p4.setItemWidget(label_item, 0, label_name_widget)
        secondary_struct_combo = LabelComboBox_v2()
        secondary_struct_combo.addItems(['', 'protein - all', 'protein - helix', 'protein - sheet', 'protein - loop', 'RNA', 'DNA'])
        secondary_struct_combo.currentTextChanged.connect(lambda: print("item changed"))
        self.ui.treeWidget_p4.setItemWidget(label_item, 1, secondary_struct_combo)
        # residues_combo = LabelComboBox(placeholder_text="Choose residue(s)")
        residues_combo = LabelComboBox_v2()
        residues_combo.addItems(['', 'All', 'A', 'T', 'C', 'G', 'U', 'alanine', 'arginine', 'asparagine', 'aspartic acid', 'cysteine', 'glutamic acid', 'glutamine', 'glycine', 'histidine', 'isoleucine', 'leucine', 'lysine', 'methionine', 'phenylalanine', 'proline', 'serine', 'threonine', 'tryptophan', 'tyrosine', 'valine'])
        self.ui.treeWidget_p4.setItemWidget(label_item, 2, residues_combo)
        atoms_lineedit = LabelLineEdit.CustomLineEdit(['All', 'C', 'N', 'P', 'O', 'H', 'Metals?'])
        atoms_lineedit.setPlaceholderText("Type in atoms")    # TODO: consider adding this to the customlineedit constructor
        self.ui.treeWidget_p4.setItemWidget(label_item, 3, atoms_lineedit)
        label_delbtn = qtw.QPushButton()
        label_delbtn.setIcon(qtg.QIcon(r"GUI_custom_widgets/svgs/clear_inverse-svgrepo-com.svg"))
        label_delbtn.setFixedWidth(16)
        label_delbtn.setFixedHeight(16)
        label_delbtn.setStyleSheet("QPushButton {\n"
        "    background: transparent;\n"       # used to be a light gray
        "    border-radius: 8px;\n"
        "    color: white;\n"
        "}\n"
        "\n"
        "QPushButton:hover, QPushButton:pressed {\n"
        "    background: rgb(200, 0, 0);\n"
        "    border-image: url(GUI_custom_widgets/svgs/clear_inverse-svgrepo-com.svg);\n"   # border-image vs image?
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border: 2px solid transparent;\n"
        "}")
        label_delbtn.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        # label_delbtn.clicked.connect(self.delete_label)
        label_delbtn.clicked.connect(lambda: self.delete_btn_clicked("label"))
        self.ui.treeWidget_p4.setItemWidget(label_item, 4, label_delbtn)
        
        # group_item.addChild(label_name_widget)
        group_item.setExpanded(True)  # Automatically expand the group when a label is added
        self.ui.treeWidget_p4.setCurrentItem(label_item)

        label = self.label_dict_template.copy()   # delete this later and make a separate function. More optimal way is to retrieve only when ready to generate datasets. But maybe want some method to save sessions/history later idk
        label['secondary_type'] = "obunga"
        self.labels.append(label)    # lol its not even right
        print(self.labels)

    def showDeleteButton(self):
        pass

    def delete_label(self):
        selected_item = self.ui.treeWidget_p4.currentItem()
        if selected_item:          # functionally equivalent to if selection_item is not None:
            selected_item.parent().removeChild(selected_item)

    def delete_group(self):
        selected_item = self.ui.treeWidget_p4.currentItem()
        if selected_item:          # functionally equivalent to if selection_item is not None:
            self.ui.treeWidget_p4.takeTopLevelItem(self.ui.treeWidget_p4.indexOfTopLevelItem(selected_item))
        if self.ui.treeWidget_p4.topLevelItemCount() == 0:
            self.ui.addlabel_btn.setDisabled(True)

    def duplicate_label(self):
        """Add a label (subitem, editable) to the selected group or the parent group of the selected label."""
        selected_item = self.ui.treeWidget_p4.currentItem()

        # Check if a group or label is selected
        if selected_item is not None:
            if selected_item.parent() is None:
                # If a group is selected, add a label to the group
                group_item = selected_item
            else:
                # If a label is selected, add a label to its parent group
                group_item = selected_item.parent()

            label_name = f"Label {group_item.childCount() + 1}"
            label_item = qtw.QTreeWidgetItem([label_name])
            label_item.setFlags(label_item.flags() | qtc.Qt.ItemIsEditable)  # Allow editing of the label item
            group_item.addChild(label_item)
            group_item.setExpanded(True)  # Automatically expand the group when a label is added


##### discord style delete button, should move these into a separate file (not just the popup dialog but the delete button too. Literally just have to modify SANDBOX_temp.py's mainwindow to just a button)
    def delete_btn_clicked(self, sender_type):
        # Detect if Shift key is held
        if qtw.QApplication.keyboardModifiers() == qtc.Qt.ShiftModifier:
            self.delete_without_confirmation(sender_type)
        else:
            self.open_delete_popup(sender_type)

    # delete confirmation popup
    def open_delete_popup(self, sender_type):
        """Show the popup dialog."""
        if sender_type == "group":
            dialog = PopupDialog(self, self.delete_group)
        else:   # elif sender_type == "label":
            dialog = PopupDialog(self, self.delete_label)
        dialog.setWindowModality(False)  # Non-modal, allowing interaction with the main window
        dialog.show()

    # Bypass confirmation dialog and delete
    def delete_without_confirmation(self, sender_type):
        print("Deleted without confirmation!")
        if sender_type == "group":
            self.delete_group()
        else:   # elif sender_type == "label":        
            self.delete_label()






#! Dependent Spin Boxes
#  Spin Box rules:
#  I)    box1 + box2 + box3 = 100%
#  II)   0 <= box1 <= 100
#  III)  0 <= box2 <= 100
#  IV)   0 <= box3 <= 100
#
#  Funneling rules (i.e. which boxes to change first to main rule I):
#  A) When box1 changes, first adjust box3 until limit, and then box2
#  B) When box2 changes, first adjust box3 until limit, and then box1
#  C) When box3 changes, first adjust box1 until limit, and then box2
#
#  Translating to code:
#  We only know the new/changed value of a combo box, not it's initial. Instead think of having a pot of 100 percentage points, and then taking them out in a specific order. The combo box that got changed already took from the pot first.
#  i.e. A) When box1 changes, box1 takes that amount out of the pot (its new/changed value).
#          Then box2 takes from the remainder (as much of its original value as possible). 
#          Then box3 takes whatever's left.
#  ditto for B) and C):
#       B) 2 takes first, then 1, then 3
#       C) 3 takes first, then 1, then 2
#
#  In fact, all 3 cases are the same, it's just the the order of boxes that's different. So we can generalize it to:
#       X takes from the "pot" first, then Y, then Z. Where X, Y, Z can be box1, box2, box3 in whatever order.
#
#?  TLDR: put all percentage points in a "pot" and take them out in a specific order

    # Generalized helper fxn
    def new_spinbox_vals(self, X_f = 100, Y_i = 0):
        rem_X = 100 - X_f       # rem for remainder
        Y_f = min(rem_X, Y_i)
        rem_Y = max(rem_X - Y_f, 0)
        Z_f = rem_Y

        # assert(X_f + Y_f + Z_f == 100)
        # print(X_f, Y_f, Z_f)
        return Y_f, Z_f         # X_f is already an input

    # # When spinbox 1 changes, update spinbox 2 and 3 accordingly
    # def on_spin_box1_changed(self, value):   #TODO: rename widget or fxn names so the underscores are consistent, add the _1 suffix to spinBox (by default designer only adds suffixes starting with the second one)
    #     self.ui.spinBox_2.blockSignals(True)  # Temporarily block the other spinbox signals to avoid recursion
    #     self.ui.spinBox_3.blockSignals(True)

    #     Y_final, Z_final = self.new_spinbox_vals(value, self.ui.spinBox_2.value())   # 1, 2, 3
    #     self.ui.spinBox_2.setValue(Y_final)
    #     self.ui.spinBox_3.setValue(Z_final)

    #     self.ui.spinBox_2.blockSignals(False)  # Unblock signals
    #     self.ui.spinBox_3.blockSignals(False)

    # # When spinbox 2 changes, update spinbox 1 and 3 accordingly
    # def on_spin_box2_changed(self, value):
    #     self.ui.spinBox.blockSignals(True)  # Temporarily block the other spinbox signals to avoid recursion
    #     self.ui.spinBox_3.blockSignals(True)

    #     Y_final, Z_final = self.new_spinbox_vals(value, self.ui.spinBox.value())   # 2, 1, 3
    #     self.ui.spinBox.setValue(Y_final)
    #     self.ui.spinBox_3.setValue(Z_final)

    #     self.ui.spinBox.blockSignals(False)  # Unblock signals
    #     self.ui.spinBox_3.blockSignals(False)

    # # When spinbox 3 changes, update spinbox 1 and 2 accordingly
    # def on_spin_box3_changed(self, value):
    #     self.ui.spinBox.blockSignals(True)  # Temporarily block the other spinbox signals to avoid recursion
    #     self.ui.spinBox_2.blockSignals(True)

    #     Y_final, Z_final = self.new_spinbox_vals(value, self.ui.spinBox.value())  # 3, 1, 2
    #     self.ui.spinBox.setValue(Y_final)
    #     self.ui.spinBox_2.setValue(Z_final)

    #     self.ui.spinBox.blockSignals(False)  # Unblock signals
    #     self.ui.spinBox_2.blockSignals(False)


    # #^ REFACTORIZATION 1: ideally the same performance as refactorization 2. better loose coupling than refactorization 2 (prob makes no difference). So a little better IF the value of the spinbox changes unexpectedly after the signal is emitted.
    # When spinbox 1 changes, update spinbox 2 and 3 accordingly
    def spin_box_changed_generic(self, value, other_boxes):
        other_boxes[0].blockSignals(True)  # Temporarily block the other spinbox signals to avoid recursion
        other_boxes[1].blockSignals(True)

        Y_final, Z_final = self.new_spinbox_vals(value, other_boxes[0].value())
        other_boxes[0].setValue(Y_final)
        other_boxes[1].setValue(Z_final)

        other_boxes[0].blockSignals(False)  # Unblock signals
        other_boxes[1].blockSignals(False)
    # When spinbox 1 changes, update spinbox 2 and 3 accordingly
    def on_spin_box1_changed(self, value):
        self.spin_box_changed_generic(value, [self.ui.spinBox_2, self.ui.spinBox_3])    # 1, 2, 3

    # When spinbox 2 changes, update spinbox 1 and 3 accordingly
    def on_spin_box2_changed(self, value):
        self.spin_box_changed_generic(value, [self.ui.spinBox, self.ui.spinBox_3])      # 2, 1, 3

    # When spinbox 3 changes, update spinbox 1 and 2 accordingly
    def on_spin_box3_changed(self, value):
        self.spin_box_changed_generic(value, [self.ui.spinBox, self.ui.spinBox_2])      # 3, 1, 2


    #^ REFACTORIZATION 2: more readable code. ideally the same performance as refactorization 1. potentially slightly more responsive and more prone to unexpected changes in value. worse loose coupling. Rly only an issue IF the value of the spinbox changes unexpectedly after the signal is emitted (maybe value changed super fast, like with an infinite scroll scrollwheel?).
    # # When spinbox 1 changes, update spinbox 2 and 3 accordingly
    # def spin_box_changed_generic(self, order):
    #     order[1].blockSignals(True)  # Temporarily block the other spinbox signals to avoid recursion
    #     order[2].blockSignals(True)

    #     Y_final, Z_final = self.new_spinbox_vals(order[0].value(), order[1].value())
    #     order[1].setValue(Y_final)
    #     order[2].setValue(Z_final)

    #     order[1].blockSignals(False)  # Unblock signals
    #     order[2].blockSignals(False)
    # # When spinbox 1 changes, update spinbox 2 and 3 accordingly
    # def on_spin_box1_changed(self):
    #     self.spin_box_changed_generic([self.ui.spinBox, self.ui.spinBox_2, self.ui.spinBox_3])

    # # When spinbox 2 changes, update spinbox 1 and 3 accordingly
    # def on_spin_box2_changed(self):
    #     self.spin_box_changed_generic([self.ui.spinBox_2, self.ui.spinBox, self.ui.spinBox_3])

    # # When spinbox 3 changes, update spinbox 1 and 2 accordingly
    # def on_spin_box3_changed(self):
    #     self.spin_box_changed_generic([self.ui.spinBox_3, self.ui.spinBox, self.ui.spinBox_2])






    #! move this to the top for better readability
    def setup_logger(self):
        handler = Handler(self)
        log_text_box = qtw.QPlainTextEdit(self)
        self.ui.logsWidget.layout().addWidget(log_text_box)
        self.ui.logsViewBox.deleteLater()
        self.ui.logsViewBox = None
        logging.getLogger().addHandler(handler)
        logging.getLogger().setLevel(logging.INFO)
        handler.new_record.connect(log_text_box.appendPlainText) # <---- connect QPlainTextEdit.appendPlainText slot



if __name__ == '__main__':
    # os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"                          # choose one
    # os.environ["QT_SCREEN_SCALE_FACTORS"] = "1.2"    # can set individual scale factors for each screen (not sure how to implement into gui for users to choose, like can u change at runtime? test later and also with a 2nd monitor hooked up)
    os.environ["QT_SCALE_FACTOR"] = "1"
    if hasattr(qtc.Qt, 'AA_EnableHighDpiScaling'):     #https://stackoverflow.com/a/47723454,   not sure if need if guards, since gonna package my version of qt with the executable, but might as well keep it cuz it doesnt break anything
        qtw.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(qtc.Qt, 'AA_UseHighDpiPixmaps'):
        qtw.QApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps, True)
    # os.environ["QT_FONT_DPI"] = "96"    # scale font size (seems to be indepdent of UI elements)    <-- from pydracula tutorial

    app = qtw.QApplication(sys.argv)
    # app.setStyle("QWindowsStyle")
    # app.setStyle(qtw.QStyleFactory.create("Fusion"))
    w = MainWindow()
    # w.showFullScreen()   # no top bar
    sys.exit(app.exec_())