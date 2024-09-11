import sys
from PyQt5 import QtCore, QtGui, QtWidgets

# MyStream class to handle emitting print output to a QTextEdit
class MyStream(QtCore.QObject):
    message = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyStream, self).__init__(parent)

    def write(self, message):
        self.message.emit(str(message))

# Main window class
class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        # Create a push button and a text edit
        self.pushButtonPrint = QtWidgets.QPushButton(self)
        self.pushButtonPrint.setText("Click Me!")
        self.pushButtonPrint.clicked.connect(self.on_pushButtonPrint_clicked)

        self.textEdit = QtWidgets.QTextEdit(self)

        # Set up the vertical layout
        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.pushButtonPrint)
        self.layoutVertical.addWidget(self.textEdit)

    @QtCore.pyqtSlot()
    def on_pushButtonPrint_clicked(self):
        # Use Python 3's print function
        print("Button Clicked!")
        print("woahh print statement")

    @QtCore.pyqtSlot(str)
    def on_myStream_message(self, message):
        # Ensure new text is inserted at the end of the QTextEdit
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.textEdit.insertPlainText(message)

# Main entry point of the application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.show()

    # Create a custom stream object
    myStream = MyStream()
    myStream.message.connect(main.on_myStream_message)

    # Redirect stdout to the custom stream
    sys.stdout = myStream

    sys.exit(app.exec_())