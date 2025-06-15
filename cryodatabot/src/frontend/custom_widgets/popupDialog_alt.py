# what is this?
#    took popupDialog.py and split the easy to close dialog code (the event filter) into its own file for better reusability in other parts of the gui
#    SO then popupDialog is just an implementation of that custom easy to close dialog, saves having to copy the event filter every time

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QWidget
from cryodatabot.src.frontend.custom_widgets.easyCloseDialog import EasyCloseDialog


class PopupDialog(EasyCloseDialog):
    def __init__(self, parent=None, fxn=None, widget_type=""):
        super(PopupDialog, self).__init__(parent)
        # self.setWindowTitle(f"Delete {widget_type.capitalize()}")    # gets hidden by next line anyways
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)    # hide the entire top bar
        # self.setGeometry(150, 150, 300, 200)

        layout = QVBoxLayout(self)    # vertical layout for text and button group
        title = QLabel(f"Delete {widget_type.capitalize()}")
        # title.setStyleSheet("font-family: 'Comic Sans MS'; font-size: 18pt;")    # can tweak font family and size thru style sheet
        title.setStyleSheet("font-size: 18pt;")
        layout.addWidget(title)
        text_blurb = QLabel(f"Are you sure you want to delete this {widget_type}? This can't be undone.\n\nTip:\nHold down shift when clicking \"x\" to bypass this confirmation")
        layout.addWidget(text_blurb)

        layout2 = QHBoxLayout()    # horizonal layout for buttons
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
        cancel_button.setObjectName("cancel_button")    # give it a name so can target it in style sheet easier
        layout2.addWidget(cancel_button)
        cancel_button.clicked.connect(self.close)

        layout.addWidget(buttons_widget)

        self.setStyleSheet("""
            QDialog {
                background-color: #f0f0f0;
                border: 1px solid #555;
                border-radius: 8px;
            }
            QLabel {
                color: #333;
                font-size: 14px;
            }
            QPushButton {
                background-color: #b0b0b0;
                color: white;
                border-radius: 4px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #909090;
            }
            QPushButton#cancel_button {
                background-color: #ad2f2f;
            }
            QPushButton#cancel_button:hover {
                background-color: #7d2020;
            }
        """)

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