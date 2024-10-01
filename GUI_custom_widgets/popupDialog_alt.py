# what is this?
#    took popupDialog.py and split the easy to close dialog code (the event filter) into its own file for better reusability in other parts of the gui
#    SO then popupDialog is just an implementation of that custom easy to close dialog, saves having to copy the event filter every time

from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QLabel
from GUI_custom_widgets.easyCloseDialog import EasyCloseDialog


class PopupDialog(EasyCloseDialog):
    def __init__(self, parent=None, fxn=None):
        super(PopupDialog, self).__init__(parent)
        self.setWindowTitle("Popup Dialog")
        self.setGeometry(150, 150, 300, 200)

        # Basic layout and button in the popup
        layout = QVBoxLayout(self)
        text_blurb = QLabel("You sure u wanna delete?")
        layout.addWidget(text_blurb)
        close_button = QPushButton("Confirm")
        layout.addWidget(close_button)
        if fxn != None:
            close_button.clicked.connect(fxn)        # passing fxns as parameters. pros: can pass wtv and handle logic for choosing which fxn to pass outside this file
        # close_button.clicked.connect(parent.delete_label)       # accessing via parent. cons: need to know the name of the fxn (also have to change it if changed in main file), and have to handle the logic for choosing which fxn to run in this file, which is prob out of the scope of what this file should do
        close_button.clicked.connect(lambda: print("deleted"))
        close_button.clicked.connect(self.close)

    def showEvent(self, event):
        # Install a global event filter when the dialog is shown
        QApplication.instance().installEventFilter(self)
        super().showEvent(event)

    def hideEvent(self, event):
        # Remove the event filter when the dialog is closed
        QApplication.instance().removeEventFilter(self)
        super().hideEvent(event)

    def close(self):
        print("dialog closed")
        return super().close()