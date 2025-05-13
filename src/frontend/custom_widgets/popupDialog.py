from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QLabel


class PopupDialog(QDialog):
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

    def eventFilter(self, watched, event):
        # Check if a mouse button is pressed outside the dialog
        if event.type() == QEvent.MouseButtonPress:
            if not self.rect().contains(self.mapFromGlobal(event.globalPos())):
                self.close()
        return super().eventFilter(watched, event)