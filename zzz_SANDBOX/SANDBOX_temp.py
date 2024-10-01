import sys
from PyQt5.QtCore import QEvent, QPoint, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QVBoxLayout, QLabel


#start: put this shit in a separate file (with the necessary imports)
class PopupDialog(QDialog):
    def __init__(self, parent=None):
        super(PopupDialog, self).__init__(parent)
        self.setWindowTitle("Popup Dialog")
        self.setGeometry(150, 150, 300, 200)

        # Basic layout and button in the popup
        layout = QVBoxLayout(self)
        text_blurb = QLabel("You sure u wanna delete?")
        layout.addWidget(text_blurb)
        close_button = QPushButton("Confirm")
        layout.addWidget(close_button)
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
#end: put this shit in a separate file (with the necessary imports)



# TODO: CONVERT THIS CLASS TO JUST A QPUSHBUTTON. the example usage is also literally in here
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 300)

        # Button to open the popup dialog
        self.button = QPushButton("Delete", self)
        self.button.setGeometry(150, 100, 100, 50)
        self.button.clicked.connect(self.on_click)              # this is rly all u need besides the 3 fxns below

    # start: move these to a separate file too, call it deleteButton? or like popupDeleteButton?
    def on_click(self):
        # Detect if Shift key is held
        if QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.delete_without_confirmation()
        else:
            self.open_popup()

    def open_popup(self):
        """Show the popup dialog."""
        self.dialog = PopupDialog(self)
        self.dialog.setWindowModality(False)  # Non-modal, allowing interaction with the main window
        self.dialog.show()

    def delete_without_confirmation(self):
        # Bypass confirmation dialog and delete directly
        print("Deleted without confirmation!")
    # end: move these to a separate file too, call it deleteButton? or like popupDeleteButton?


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
