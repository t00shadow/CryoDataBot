# what is this?
#    took popupDialog.py and split the easy to close dialog code (the event filter) into its own file for better reusability in other parts of the gui
#    SO then popupDialog is just an implementation of that custom easy to close dialog, saves having to copy the event filter every time

from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QWidget
from GUI_custom_widgets.easyCloseDialog import EasyCloseDialog


class PopupDialog(EasyCloseDialog):
    def __init__(self, parent=None, fxn=None):
        super(PopupDialog, self).__init__(parent)
        self.setWindowTitle("Delete Label")
        # self.setGeometry(150, 150, 300, 200)

        # Basic layout and button in the popup
        layout = QVBoxLayout(self)
        text_blurb = QLabel("Are you sure you want to delete this label? Deletion is permanent.\n\nTip:\nHold down shift when clicking \"x\" to bypass this confirmation")
        layout.addWidget(text_blurb)

        layout2 = QHBoxLayout()
        buttons_widget = QWidget()
        buttons_widget.setLayout(layout2)
        confirm_button = QPushButton("Confirm")
        layout2.addWidget(confirm_button)
        if fxn != None:
            confirm_button.clicked.connect(fxn)        # passing fxns as parameters. pros: can pass wtv and handle logic for choosing which fxn to pass outside this file
        # confirm_button.clicked.connect(parent.delete_label)       # accessing via parent. cons: need to know the name of the fxn (also have to change it if changed in main file), and have to handle the logic for choosing which fxn to run in this file, which is prob out of the scope of what this file should do
        confirm_button.clicked.connect(lambda: print("deleted"))
        confirm_button.clicked.connect(self.close)
        cancel_button = QPushButton("Cancel")
        layout2.addWidget(cancel_button)
        cancel_button.clicked.connect(self.close)

        layout.addWidget(buttons_widget)

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