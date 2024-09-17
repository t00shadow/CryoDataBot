from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
from PyQt5 import QtWidgets, QtCore
import sys

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Widget Tracker')

        # Create a layout and add widgets
        layout = QVBoxLayout()
        self.label = QLabel("Enter something:")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Submit")
        
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        self.setLayout(layout)

        # Connect button to print current widgets
        self.button.clicked.connect(self.print_widgets)

        # added the stuff from the stack post: https://stackoverflow.com/a/20167458
        self.checkbox = QtWidgets.QCheckBox('Delete')
        self.button2 = QtWidgets.QPushButton('Open', self)
        self.button2.clicked.connect(self.openDialog)
        self.button2.clicked.connect(self.print_widgets)
        # layout = QtWidgets.QHBoxLayout(self) # already have layout
        layout.addWidget(self.checkbox)
        layout.addWidget(self.button2)

    def print_widgets(self):
        # Print all currently existing widgets
        print("Currently existing widgets:")
        count = 0
        for widget in QApplication.allWidgets():
            count += 1
            print(f"Widget: {widget}, Type: {type(widget)}")
        print(f"widget count: {count}")
    
    def openDialog(self):
        widget = QtWidgets.QDialog(self)
        if (self.checkbox.isChecked() and
            not widget.testAttribute(QtCore.Qt.WA_DeleteOnClose)):
            widget.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            for child in self.findChildren(QtWidgets.QDialog):
                if child is not widget:
                    child.deleteLater()
        label = QtWidgets.QLabel(widget)
        button = QtWidgets.QPushButton('Close', widget)
        button.clicked.connect(widget.close)
        layout = QtWidgets.QVBoxLayout(widget)
        layout.addWidget(label)
        layout.addWidget(button)
        objects = self.findChildren(QtCore.QObject)
        label.setText('Objects = %d' % len(objects))
        print(objects)
        widget.show()

# Main part of the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()

    sys.exit(app.exec_())
