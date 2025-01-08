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
from guiskin_DEV2_alt_TEMP_DEMO_VERSION import Ui_MainWindow    # need the "Ui_" prefix
#from guiskin import Ui_MainWindow

import GUI_custom_widgets.z_Tag_main_alt_allcode_v2 as TTEwidget2
from GUI_custom_widgets.LabelComboBox import LabelComboBox
from GUI_custom_widgets.LabelComboBox_v2 import LabelComboBox_v2
import GUI_custom_widgets.commaLineEdit as LabelLineEdit
from GUI_custom_widgets.animated_toggle import AnimatedToggle
from GUI_custom_widgets.popupDialog_alt import PopupDialog
from GUI_custom_widgets.easyCloseDialog import EasyCloseDialog
from my_logger import Handler


# import main_new_myversion

# from z_fetch_sample_info import search_emdb
# from z_refine_sample_info_DEBUGGING import refine_csv

from backend_core import fetch_sample_info, redundancy_filter, downloading_and_preprocessing, generate_dataset




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
        self.default_folder = ""      # set this using os.join, etc. OR force users to pick smth idk
        self.default_metadata_filepath = r"C:\Users\noelu\CryoDataBot\JUNK_TEST_FOLDER\...\metadata"
        self.labels = [[]]     # list of list of dicts, initialize as list of empty list
        self.label_dict_template = {'secondary_type': '', 'residue_type': '', 'atom_type': '', 'label': ''}
        self.main_dir_selection_locked = False
        self.main_dir_path = ""
        self.leftpanel_buttons = {}    # key, value = QPushButton, text().  Alternatively just use two lists


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
        # self.ui.lineEdit_p2.setText(r"C:\Users\noelu\CryoDataBot\JUNK_TEST_FOLDER")
        # TODO: enable elide for all filepath text fields
        self.ui.lineEdit_p3.setText(self.default_metadata_filepath)


        ## buttons
        # page 0
        self.ui.main_save_path_btn.clicked.connect(lambda: self.browse_folder(page="home"))
        # page 1
        # self.ui.pushButton_p1.clicked.connect(lambda: self.browse_folder(page="quick"))
        # self.ui.pushButton_p1_2.clicked.connect(lambda: self.ui.statusbar.showMessage("query (preview): " + self.parseQuery(page="quick")))    # intentionally didnt add time limit for this message so users can take their time to read it
        self.ui.pushButton_p1_3.clicked.connect(self.gen_dataset_quick)
        # page 2
        self.ui.pushButton_p2.clicked.connect(lambda: self.browse_folder(page="step1"))
        self.ui.pushButton_p2_2.clicked.connect(self.fetch_sample_info)

        self.lockBtn = qtw.QPushButton()
        self.lockBtn.setCursor(qtc.Qt.PointingHandCursor)
        self.lockBtn.setIcon(qtg.QIcon(r"GUI_custom_widgets/svgs/lock-open-svgrepo-com.svg"))
        # self.lockBtn.clicked.connect(lambda: self.lockBtn.setIcon(qtg.QIcon(r"GUI_custom_widgets/svgs/lock-open-svgrepo-com.svg")))
        self.lockBtn.clicked.connect(self.lock_main_dir_selection)
        self.ui.B1_csvFilepath.layout().insertWidget(0, self.lockBtn)
        self.ui.pushButton_p3_4.clicked.connect(self.redund_filter)
        # page 3
        self.ui.pushButton_p3.clicked.connect(lambda: self.browse_folder(page="step2"))
        self.ui.resetDefaultVal_btn.clicked.connect(lambda: self.ui.lineEdit_p3.setText(self.default_metadata_filepath))
        
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
        self.ui.clearSim_btn.clicked.connect(lambda: self.ui.similaritySpinBox.setValue(100))
        # page 4
        self.ui.pushButton_p4_2.clicked.connect(self.gen_dataset)


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
        # self.ui.lineEdit_p1_2.setText(r"C:\Users\noelu\CryoDataBot\JUNK_TEST_FOLDER\Labels")
        self.ui.lineEdit_p3_2.setText(r"C:\Users\noelu\CryoDataBot\JUNK_TEST_FOLDER\Labels")
        self.ui.statusbar.showMessage("example status bar message")

        # self.ui.lineEdit_p1_2.findChild(qtw.QToolButton).setIcon(qtg.QIcon(r"GUI_custom_widgets/svgs/clear_small-svgrepo-com.svg"))
        self.ui.lineEdit_p3_2.findChild(qtw.QToolButton).setIcon(qtg.QIcon(r"GUI_custom_widgets/svgs/clear_small-svgrepo-com.svg"))
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

        self.setup_logger()

        # Your code ends here
        self.show()




    # functions, for bigger gui could put these in separate files and import them
    # Edit: ehh havent needed it so far

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


    
    def show_tooltip_on_click(self, message: str):
        button = self.sender()
        qtw.QToolTip.showText(button.mapToGlobal(qtc.QPoint(15, -10)), message, button)

    # makes the CryoDataBot main directory at user specified location
    # lowkey this is unneeded if u use os.makedirs in the other steps
    # ideas for helping visually clue viewers in that it's only needs to be set once, is having it greyed out, and then clicking a gear button to trigger a dialog window to edit it. or having a dropdown and then gear icon again idk
    # OR make an inital page (like vscodes home page thing or chimeras, that asks users to select a home save folder upon first launch (stores it some json or smth))
    
    # TODO: small bug, if no folder is selected, it becomes just "CryoDataBot. like as the absolute path lol. just use os.getcwd or wtv
    def make_main_dir(self, dir_path):
        print("make_main_dir fxn triggered")
        try:
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
        except Exception as error:
            print("An exception occurred:", error)    # TODO: switch to a logger statement

    def lock_main_dir_selection(self):
        if self.ui.lineEdit_p2.text() == "":
            self.ui.statusbar.showMessage("select a folder", 1000)
            return

        if not self.main_dir_selection_locked:
            self.lockBtn.setIcon(qtg.QIcon(r"GUI_custom_widgets/svgs/lock-closed-svgrepo-com.svg"))
            self.ui.lineEdit_p2.setStyleSheet("background-color: white")
            self.ui.pushButton_p2.setDisabled(True)
            self.main_dir_selection_locked = True
        else:
            self.lockBtn.setIcon(qtg.QIcon(r"GUI_custom_widgets/svgs/lock-open-svgrepo-com.svg"))
            self.ui.lineEdit_p2.setStyleSheet("background-color: white; color: black")
            self.ui.pushButton_p2.setDisabled(False)
            self.main_dir_selection_locked = False

        # this code looks kinda gross
    def browse_folder(self, page="quick"):
        filepath = qtw.QFileDialog.getExistingDirectory(self, 'Select Folder')
        print("selected path:", filepath)
        self.ui.statusbar.showMessage(f"selected folder: {filepath}", 2000)    # if use textChanged instead of textEdited signal in lineEdit_22 to statusbar connection, can remove this line, since textChanged is emitted the text is change by users OR programmatically (textEdited is only emited when text is changed by users)
        if page == "home":
            self.main_dir_path = os.path.join(filepath, "CryoDataBot")
            self.ui.main_save_path_lineedit.setText(self.main_dir_path.replace("\\", "/"))
        elif page == "quick":
            self.ui.lineEdit_p1.setText(filepath)
        elif page == "step1" and not self.main_dir_selection_locked:
            self.main_dir_path = os.path.join(filepath, "CryoDataBot")
            self.ui.lineEdit_p2.setText(self.main_dir_path.replace("\\", "/"))    # doesnt modify self.main_dir_path btw
            # self.make_main_dir(main_dir_path)
            self.lock_main_dir_selection()
        elif page == "step2":
            self.ui.lineEdit_p3.setText(filepath)



    # junk fxn for testing signals and slots, can delete/comment out later
    def run_naive(self):
        userinput = self.ui.lineEdit.text()
        print("Running " + userinput)

    # def updateStatusBar(self, string):
    #     self.ui.statusBar.showMessage(string)


    # STEP 1: fetch_sample_info

    # this fxn needs to be updated
    def fetch_sample_info(self) -> None:
        """
        Return value is ... Creates new files.

        Parameters
        ----------
        None
        """
        # mm kinda debatable if this should be here, cuz you could skip this step
        # so nah this shouldnt be here, instead the first button that gets clicked should trigger this (how to do that elegantly without shoving if statements everywhere)
        self.make_main_dir(self.main_dir_path)

        query = self.userInputQuery.text()    # change this to the custom widget like in gen_dataset_quick()
        #processedstring = stringutil.process_string(query)   # TODO, concatenate array of keywords into a string (not sure how to implement and and or logic with keywords)
        processed_query = query     # placeholder
        # print(processed_query)
        save_path = self.ui.lineEdit_p2.text()
        #TODO: put a try block here or some if statements to catch if btn is clicked with no parameters set
        output_path = fetch_sample_info.search_emdb(processed_query, save_path)
        print(f"path of metadata file: {output_path}")     # needs to return path of folder where shit is saved
        self.ui.lineEdit_p3.setText("placeholder generated path")

    def gen_dataset(self):
        # self.ui.groups_of_labels is an array of string arrays
        # for each group, generate a labeled dataset
        pass

    # Helper function for gen_dataset_quick
    def parseQuery(self, page="quick"):
        if page == "quick":
            # return " AND ".join(self.querywidget.keywords)    # dont need to this cuz can directly access, basically global. instead just pass a string or int to distinguish which to use. tho maybe have 2 separate fxn is better cuz dont have to run an if statement each time u press the button
            return self.ui.lineEdit.text()
        elif page == "step1":
            # return " AND ".join(self.querywidget2.keywords)
            return self.userInputQuery.text()
        else:
            return ""     # spit out an error, this is only for the developer, not a runtime thing

    # ignore this for now
    # EDOT: do NOT do it like this, new approach just manually set shit, but still call all 4 fxns
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

    # STEP 2: redundancy_filter (this is abstracted away for the user)
    def redund_filter(self):
        # replaced everything here with a dumbed down version for testing purposes:
        redundancy_filter.main()

    # Move this to the very bottom
    def summary(self):
        pass

    # STEP 3: downloading & preprocessing

    # STEP 4: generate dataset

    #QTreeWidget stuff --> TODO: move to its own file, need to slightly rewrite cuz accessing ui widgets, like pass in the tree widget
    def add_group(self):
        """Add a new group to the tree widget (top-level item, editable)."""
        group_name = f"Group {self.ui.treeWidget_p4.topLevelItemCount() + 1}"
        group_item = qtw.QTreeWidgetItem([group_name, "", ""])
        group_item.setFlags(group_item.flags() | qtc.Qt.ItemIsEditable)  # Make the group item editable
        self.ui.treeWidget_p4.addTopLevelItem(group_item)

        # Automatically select the newly added group
        self.ui.treeWidget_p4.setCurrentItem(group_item)

    def add_group_w_del_btn(self):
        """Add a new group to the tree widget (top-level item, editable)."""
        group_name = f"Group {self.ui.treeWidget_p4.topLevelItemCount() + 1}"
        group_item = qtw.QTreeWidgetItem([group_name, "", ""])
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
        group_delbtn.clicked.connect(self.delete_group)
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
            label_item = qtw.QTreeWidgetItem([label_name, "", ""])
            label_item.setFlags(label_item.flags() | qtc.Qt.ItemIsEditable)  # Allow editing of the label item
            group_item.addChild(label_item)
            group_item.setExpanded(True)  # Automatically expand the group when a label is added

    # label here refers to a label item in the labels tree not a QLabel
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
        # label_item = qtw.QTreeWidgetItem([label_name, "", ""])
        # label_item.setFlags(label_item.flags() | qtc.Qt.ItemIsEditable)  # Allow editing of the label item
        child_item = qtw.QTreeWidgetItem(group_item)
        child_item.setFlags(child_item.flags() | qtc.Qt.ItemIsEditable)  # DISABLE this and add a custom line edit with a completer
        group_item.addChild(child_item)

        self.ui.treeWidget_p4.setItemWidget(child_item, 0, qtw.QLabel(label_name))
        secondary_struct_combo = LabelComboBox_v2()
        secondary_struct_combo.addItems(['', 'protein - all', 'protein - helix', 'protein - sheet', 'protein - loop', 'RNA', 'DNA'])
        secondary_struct_combo.currentTextChanged.connect(lambda: print("item changed"))
        self.ui.treeWidget_p4.setItemWidget(child_item, 1, secondary_struct_combo)
        # residues_combo = LabelComboBox(placeholder_text="Choose residue(s)")
        residues_combo = LabelComboBox_v2()
        residues_combo.addItems(['', 'All', 'A', 'T', 'C', 'G', 'U', 'alanine', 'arginine', 'asparagine', 'aspartic acid', 'cysteine', 'glutamic acid', 'glutamine', 'glycine', 'histidine', 'isoleucine', 'leucine', 'lysine', 'methionine', 'phenylalanine', 'proline', 'serine', 'threonine', 'tryptophan', 'tyrosine', 'valine'])
        self.ui.treeWidget_p4.setItemWidget(child_item, 2, residues_combo)
        atoms_lineedit = LabelLineEdit.CustomLineEdit(['All', 'C', 'N', 'P', 'O', 'H', 'Metals?'])
        atoms_lineedit.setPlaceholderText("Type in atoms")    # TODO: consider adding this to the customlineedit constructor
        self.ui.treeWidget_p4.setItemWidget(child_item, 3, atoms_lineedit)
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
        label_delbtn.clicked.connect(self.on_click)
        self.ui.treeWidget_p4.setItemWidget(child_item, 4, label_delbtn)
        
        # group_item.addChild(label_item)
        group_item.setExpanded(True)  # Automatically expand the group when a label is added
        self.ui.treeWidget_p4.setCurrentItem(child_item)

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
            label_item = qtw.QTreeWidgetItem([label_name, "", ""])
            label_item.setFlags(label_item.flags() | qtc.Qt.ItemIsEditable)  # Allow editing of the label item
            group_item.addChild(label_item)
            group_item.setExpanded(True)  # Automatically expand the group when a label is added


##### discord style delete button, should move these into a separate file (not just the popup dialog but the delete button too. Literally just have to modify SANDBOX_temp.py's mainwindow to just a button)
    def on_click(self):
        # Detect if Shift key is held
        if qtw.QApplication.keyboardModifiers() == qtc.Qt.ShiftModifier:
            self.delete_without_confirmation()
        else:
            self.open_popup()

    def open_popup(self):
        """Show the popup dialog."""
        dialog = PopupDialog(self, self.delete_label)    # passing fxn as a parameter. Also, changed self.dialog to dialog since not accessed outside of this method.
        dialog.setWindowModality(False)  # Non-modal, allowing interaction with the main window
        dialog.show()

    def delete_without_confirmation(self):      # need to distinguish between gorups and labels (idea: check sender with self.sender?). Easy fix is making 2 dif fxns but thats kinda stupid
        # Bypass confirmation dialog and delete directly
        del_button = self.sender()
        print(del_button)
        print(type(del_button))
        print(del_button.parent())

        print("Deleted without confirmation!")
        self.delete_label()



# Spin box dependency
# TLDR: spinbox1 funnels into spinbox3
#       spinbox2 funnels into spinbox3
#       total always stays at 100%
#       spinbox3 funnels back into spinbox1   (to keep total consant)

#       funny behavior: spinbox1 and spinbox2 consider each others values to keep total constant, BUT do not affect each other, sooo you can set both values to create a total above 100%
#       TODO: fix this tmrw after asking qibo which he wants to have prio
#       currently: 1 -> 3
#                  2 -> 3
#                  1 + 2 + 3 = 100%
#                  3 -> 1
#       possible fix: 1 and 2 funnel into 3 if possible. if not, then funnel into each other
#       other possible fix: just block changes, so they have to manually tweak the other spinbox (could be annoying tho...)
    def on_spin_box1_changed(self, value):   #TODO: rename so widgets and fxn names are consistent
        # When spin_box1 changes, adjust spin_box3
        total = value + self.ui.spinBox_2.value()      # total = spinbox1 + spinbox2
        remaining = max(0, 100 - total)
        self.ui.spinBox_2.blockSignals(True)  # Temporarily block signals to avoid recursion
        self.ui.spinBox_3.blockSignals(True)

        self.ui.spinBox_3.setValue(remaining)

        self.ui.spinBox_2.blockSignals(False)  # Unblock signals
        self.ui.spinBox_3.blockSignals(False)

    def on_spin_box2_changed(self, value):
        # When spin_box2 changes, adjust spin_box3 based on the sum of spin_box1 and spin_box2
        total = self.ui.spinBox.value() + value      # total = spinbox1 + spinbox2
        remaining = max(0, 100 - total)

        self.ui.spinBox.blockSignals(True)  # Temporarily block signals to avoid recursion
        self.ui.spinBox_3.blockSignals(True)

        self.ui.spinBox_3.setValue(remaining)

        self.ui.spinBox.blockSignals(False)  # Unblock signals
        self.ui.spinBox_3.blockSignals(False)

    def on_spin_box3_changed(self, value):
        # When spin_box3 changes, adjust spin_box3 based on the sum of spin_box1 and spin_box2
        total = self.ui.spinBox_2.value() + value      # total = spinbox2 + spinbox3
        remaining = max(0, 100 - total)

        self.ui.spinBox.blockSignals(True)  # Temporarily block signals to avoid recursion
        self.ui.spinBox_3.blockSignals(True)

        self.ui.spinBox.setValue(remaining)

        self.ui.spinBox.blockSignals(False)  # Unblock signals
        self.ui.spinBox_3.blockSignals(False)


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