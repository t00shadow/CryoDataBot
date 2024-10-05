#!/usr/bin/python3
# Initialize PyQT
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# The fondamental for working with python
import sys, signal

from guiskin_DEV2_alt import Ui_MainWindow


class MainWindow ( QMainWindow , Ui_MainWindow):
    # Create settings for the software
    settings = QSettings('Your Name', 'Name of the software')
    settings.setFallbacksEnabled(False)
    version = 'Your version'

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        # Load the ui generated with makepyqt5.sh
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        # Set the MainWindow Title
        self.setWindowTitle('Name of the software - ' + self.version)
        # When the software are closed on console the software are closed
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        # Show the form
        widget1 = QWidget()
        widget2 = QWidget()
        widget3 = QWidget()

        splitter = QSplitter(self)
        splitter.addWidget(widget1)
        splitter.addWidget(widget2)
        splitter.addWidget(widget3)
        self.ui.B_enterQuery.addWidget(splitter)
        self.show()


def main():
    # Start the software
    app = QApplication(sys.argv)
    MainWindow_ = QMainWindow()
    ui = MainWindow()
    ui.setupUi(MainWindow_)
    # Add the close feature at the program with the X
    sys.exit(app.exec_())


# Execute the software
main()