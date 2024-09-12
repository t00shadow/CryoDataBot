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

from guiskin_DEV2 import Ui_MainWindow    # need the "Ui_" prefix
#from guiskin import Ui_MainWindow

import GUI_custom_widgets.z_Tag_main_alt_allcode as TTEwidget2

# import main_new_myversion

from z_fetch_sample_info import search_emdb



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
        # self.resize(1000, 700)        # HOTFIX, functionally same as changing the size in the pyuic5 generated .py file but you aren't meant to edit that (can also just change size in designer, butttt it looks fine in designer). prob should involve screensize or smth, vanilla size is different than qt designer preview. prob cuz of screen resolution and/or dpi settings or smth. high dpi scaling can affect how pixels are rendered

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
        self.ui.pushButton_p1.clicked.connect(lambda: self.browse_folder(page="quick"))
        self.ui.pushButton_p1_2.clicked.connect(lambda: self.ui.statusbar.showMessage("query (preview): " + self.parseQuery(page="quick")))    # intentionally didnt add time limit for this message so users can take their time to read it
        self.ui.pushButton_p1_3.clicked.connect(self.gen_dataset_quick)
        # page 2
        self.ui.pushButton_p2.clicked.connect(lambda: self.browse_folder(page="step1"))
        self.ui.pushButton_p2_2.clicked.connect(self.fetch_sample_info)
        # page 3
        self.ui.pushButton_p3.clicked.connect(lambda: self.browse_folder(page="step2"))
        # page 4
        self.ui.pushButton_p4_2.clicked.connect(self.gen_dataset)


        ### QTreeWidget
        self.ui.addgroup_btn.clicked.connect(self.add_group)
        self.ui.addlabel_btn.clicked.connect(self.add_label)
        #  clear the initial junk from the qtreewidget
        self.ui.treeWidget_p4.clear()


        ### Spinboxes
        self.ui.spinBox.valueChanged.connect(self.on_spin_box1_changed)
        self.ui.spinBox_2.valueChanged.connect(self.on_spin_box2_changed)
        self.ui.spinBox_3.valueChanged.connect(self.on_spin_box3_changed)



        # ## custom query TextEdit widget
        # # page 1
        # self.querywidget = TTEwidget2.TagTextEdit()
        # self.ui.A4_queryBox.layout().addWidget(self.querywidget)
        # self.querywidget.setMaximumHeight(200)
        # # page 2
        # self.querywidget2 = TTEwidget2.TagTextEdit()
        # self.ui.B2_queryBox.layout().addWidget(self.querywidget2)
        # self.querywidget2.setMaximumHeight(200)

        ## status bar      (page numbers refer to the signals here. status bar is almost always the slot)
        # page 1
        self.ui.lineEdit_p1.textEdited['QString'].connect(self.ui.statusbar.showMessage)
        # self.querywidget.tagTextEdited.connect(self.ui.statusbar.showMessage)
        #self.ui.lineEdit_p1.textEdited.connect(self.ui.statusbar.showMessage)     # works without the ['QString'], look into why
        #self.querywidget.tagTextEdited.connect(print)
        # page 2
        self.ui.lineEdit_p2.textEdited['QString'].connect(self.ui.statusbar.showMessage)
        # self.querywidget2.tagTextEdited.connect(self.ui.statusbar.showMessage)



        ### logging shenanigans
        logTextBox = QTextEditLogger(self)
        # You can format what is printed to text box
        logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(logTextBox)
        # You can control the logging level
        logging.getLogger().setLevel(logging.DEBUG)
        self.ui.sidebar.layout().addWidget(logTextBox.widget)

        # Remove the placeholder widget via code (prob better to manually remove this in the ui file to reduce startup time)
        self.ui.sidebar.layout().removeWidget(self.ui.logViewBox)
        self.ui.logViewBox.deleteLater()
        self.ui.logViewBox = None


        ### tabbar tab colors
        # self.ui.tabWidget.tabBar().setTabTextColor(1, qtg.QColor(255, 0, 0, 127))    # mid solution, gets overwritten by the QSS. could do the styling with pure code but dont think u can set bg color

        ### reorder this code later btw (move all formatting stuff to top and signal/slots after)
        ### default user input values
        self.ui.lineEdit_p1.setText(r"C:\Users\noelu\CryoDataBot\JUNK_TEST_FOLDER")
        self.ui.lineEdit_p2.setText(r"C:\Users\noelu\CryoDataBot\JUNK_TEST_FOLDER")
        # TODO: fix the first column's name in label manager (space chara doesnt work, try an invisible chara)


        ### NoEditDelegate (for label manager)
        # Set the delegate for specific cells
        self.ui.treeWidget_p4.setItemDelegateForColumn(0, NoEditDelegate(self))


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
    def fetch_sample_info(self) -> None:
        """
        Return value is ... Creates new files.

        Parameters
        ----------
        None
        """

        query = self.ui.lineEdit_2.text()    # change this to the custom widget like in gen_dataset_quick()
        #processedstring = stringutil.process_string(query)   # TODO, concatenate array of keywords into a string (not sure how to implement and and or logic with keywords)
        processed_query = query     # placeholder
        # print(processed_query)
        save_path = self.ui.lineEdit_p2.text()
        #TODO: put a try block here or some if statements to catch if btn is clicked with no parameters set
        output_path = search_emdb(processed_query, save_path)
        print(f"yooo this is the return value of search_emdb: {output_path}")     # needs to return path of folder where shit is saved
        self.ui.lineEdit_p3.setText("placeholder generated path")

    def gen_dataset(self):
        # self.ui.groups_of_labels is an array of string arrays
        # for each group, generate a labeled dataset
        pass

    # ignore this for now
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

    def parseQuery(self, page="quick"):
        if page == "quick":
            # return " AND ".join(self.querywidget.keywords)    # dont need to this cuz can directly access, basically global. instead just pass a string or int to distinguish which to use. tho maybe have 2 separate fxn is better cuz dont have to run an if statement each time u press the button
            return self.ui.lineEdit.text()
        elif page == "step1":
            # return " AND ".join(self.querywidget2.keywords)
            return self.ui.lineEdit_2.text()
        else:
            return ""     # spit out an error, this is only for the developer, not a runtime thing

    # need to rewrite this fxn later for better reusability, esp with updating lineedits (might want to return the value so can use it to set dif save path variables)
    # either need to pass in names of the fxn that's signaling or jsut have dif functions for each browse button (only need like 3 total)
    def browse_folder(self, page="quick"):
        self.download_path = qtw.QFileDialog.getExistingDirectory(self, 'Select Folder')
        print("download destination:", self.download_path)
        self.ui.statusbar.showMessage(f"selected folder: {self.download_path}", 2000)    # if use textChanged instead of textEdited signal in lineEdit_22 to statusbar connection, can remove this line, since textChanged is emitted the text is change by users OR programmatically (textEdited is only emited when text is changed by users)
        if page == "quick":
            self.ui.lineEdit_p1.setText(self.download_path)
        elif page == "step1":
            self.ui.lineEdit_p2.setText(self.download_path)
        elif page =="step2":
            self.ui.lineEdit_p3.setText(self.download_path)

    def summary(self):
        pass





    #QTreeWidget stuff
    def add_group(self):
        """Add a new group to the tree widget (top-level item, editable)."""
        group_name = f"Group {self.ui.treeWidget_p4.topLevelItemCount() + 1}"
        group_item = qtw.QTreeWidgetItem([group_name, "", ""])
        group_item.setFlags(group_item.flags() | qtc.Qt.ItemIsEditable)  # Make the group item editable
        self.ui.treeWidget_p4.addTopLevelItem(group_item)

        # Automatically select the newly added group
        self.ui.treeWidget_p4.setCurrentItem(group_item)

    def add_label(self):
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




if __name__ == '__main__':
    # os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"                          # choose one
    os.environ["QT_SCALE_FACTOR"] = "1.5"                          # choose one
    # qtw.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling)            # choose one
    app = qtw.QApplication(sys.argv)
    # app.setStyle(qtw.QStyleFactory.create("Fusion"))
    w = MainWindow()
    sys.exit(app.exec_())