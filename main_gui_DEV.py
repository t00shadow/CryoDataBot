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
from pathlib import Path
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtCore import QTextCodec
codec = QTextCodec.codecForName("UTF-8")

from guiskin_DEV import Ui_MainWindow    # need the "Ui_" prefix
#from guiskin import Ui_MainWindow

import GUI_custom_widgets.z_Tag_main_alt_allcode as TTEwidget2

import main_new_myversion


class MainWindow(qtw.QMainWindow):    # Make sure the root widget/class is the right type (can check in designer or the .ui file)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(700, 1050)        # HOTFIX, functionally same as changing the size in the pyuic5 generated .py file but you aren't meant to edit that (can also just change size in designer, butttt it looks fine in designer). prob should involve screensize or smth, vanilla size is different than qt designer preview. prob cuz of screen resolution and/or dpi settings or smth. high dpi scaling can affect how pixels are rendered

        # ======== VARIABLES ========
        self.download_path = ""


        # ======== SIGNALS AND SLOTS ========
        # TODO: CONSIDER organizing them by page? tho just added pages to the names so mb not
        # NVM i like the current setup better, organize by type then page. cuz each page has dif widgets so might miss one if go by page then type


        ### lineedits
        # self.ui.lineEdit.createStandardContextMenu()
        # self.ui.lineEdit.setClearButtonEnabled(True)
        # self.ui.lineEdit.setPlaceholderText("overwrote placeholder text via code")


        ## buttons
        # page 1
        self.ui.pushButton_p1.clicked.connect(self.browse_folder)
        self.ui.pushButton_p1_2.clicked.connect(lambda: self.ui.statusbar.showMessage("query (preview): " + self.parseQuery(mode="quick")))    # intentionally didnt add time limit for this message so users can take their time to read it
        self.ui.pushButton_p1_3.clicked.connect(self.gen_dataset_quick)
        # page 2
        self.ui.pushButton_p2_2.clicked.connect(self.make_csv)
        # page 3
        # page 4
        self.ui.pushButton_p4_2.clicked.connect(self.gen_dataset)


        ## custom query TextEdit widget
        # page 1
        self.querywidget = TTEwidget2.TagTextEdit()
        self.ui.A4_queryBox.layout().addWidget(self.querywidget)
        self.querywidget.setMaximumHeight(200)
        # page 2
        self.querywidget2 = TTEwidget2.TagTextEdit()
        self.ui.B2_queryBox.layout().addWidget(self.querywidget2)
        self.querywidget2.setMaximumHeight(200)

        ## status bar      (page numbers refer to the signals here. status bar is almost always the slot)
        # page 1
        self.ui.lineEdit_p1.textEdited['QString'].connect(self.ui.statusbar.showMessage)
        self.querywidget.tagTextEdited.connect(self.ui.statusbar.showMessage)
        #self.ui.lineEdit_p1.textEdited.connect(self.ui.statusbar.showMessage)     # works without the ['QString'], look into why
        #self.querywidget.tagTextEdited.connect(print)
        # page 2
        self.ui.lineEdit_p2.textEdited['QString'].connect(self.ui.statusbar.showMessage)
        self.querywidget2.tagTextEdited.connect(self.ui.statusbar.showMessage)

        # Your code ends here
        self.show()

    # functions, for bigger gui could put these in separate files and import them
    # Edit: ehh havent needed it so far
    
    # junk fxn for testing signals and slots, can delete/comment out later
    def run_naive(self):
        userinput = self.ui.lineEdit.text()
        print("Running " + userinput)

    # def updateStatusBar(self, string):
    #     self.ui.statusBar.showMessage(string)

    # this fxn needs to be updated
    def make_csv(self):
        query = self.ui.lineEdit_p2.text()    # change this to the custom widget like in gen_dataset_quick()
        #processedstring = stringutil.process_string(query)   # TODO, concatenate array of keywords into a string (not sure how to implement and and or logic with keywords)
        processed_query = query     # placeholder
        # print(processed_query)
        main_new_myversion.search_emdb(processed_query)   # combine the results into a single csv and delete individual csvs or create a folder, should be handled in the util function

    def gen_dataset(self):
        # self.ui.groups_of_labels is an array of string arrays
        # for each group, generate a labeled dataset
        pass

    def gen_dataset_quick(self):
        # print(self.querywidget.junk_val)
        # print(self.querywidget.junk_arr)
        # print(self.querywidget.keywords)
        # print("main_new.QUERY:", main_new.QUERY)    # in this order to check initial hardcoded value, click button again to see updated value
        main_new_myversion.QUERY = self.parseQuery(mode="quick")       # will likely need a simple parsing fxn here later
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

    def parseQuery(self, mode="normal"):
        if mode == "quick":
            return " AND ".join(self.querywidget.keywords)    # dont need to this cuz can directly access, basically global. instead just pass a string or int to distinguish which to use. tho maybe have 2 separate fxn is better cuz dont have to run an if statement each time u press the button
        elif mode == "normal":
            return " AND ".join(self.querywidget2.keywords)
        else:
            return ""     # spit out an error, this is only for the developer, not a runtime thing

    # need to rewrite this fxn later for better reusability, esp with updating lineedits (might want to return the value so can use it to set dif save path variables)
    # either need to pass in names of the fxn that's signaling or jsut have dif functions for each browse button (only need like 3 total)
    def browse_folder(self):
        self.download_path = qtw.QFileDialog.getExistingDirectory(self, 'Select Folder')
        print("download destination:", self.download_path)
        self.ui.statusbar.showMessage(f"selected folder: {self.download_path}", 2000)    # if use textChanged instead of textEdited signal in lineEdit_22 to statusbar connection, can remove this line, since textChanged is emitted the text is change by users OR programmatically (textEdited is only emited when text is changed by users)
        self.ui.lineEdit_p1.setText(self.download_path)

    def summary(self):
        pass

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())