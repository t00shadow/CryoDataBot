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

from guiskin_OUTDATED import Ui_MainWindow    # need the "Ui_" prefix
#from guiskin import Ui_MainWindow


class MainWindow(qtw.QMainWindow):    # Make sure the root widget/class is the right type (can check in designer or the .ui file)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(700, 1050)        # HOTFIX, functionally same as changing the size in the pyuic5 generated .py file but you aren't meant to edit that (can also just change size in designer, butttt it looks fine in designer). prob should involve screensize or smth, vanilla size is different than qt designer preview. prob cuz of screen resolution and/or dpi settings or smth. high dpi scaling can affect how pixels are rendered

        #lineedit
        self.ui.lineEdit.createStandardContextMenu()
        self.ui.lineEdit.setClearButtonEnabled(True)
        self.ui.lineEdit.setPlaceholderText("overwrote placeholder text via code")

        # Your code ends here
        self.show()

    # functions, for bigger gui could put these in separate files and import them
    def run_naive(self):
        userinput = self.ui.lineEdit.text()
        print("Running " + userinput)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())