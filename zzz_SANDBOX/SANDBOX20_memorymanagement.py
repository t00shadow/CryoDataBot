# stack post: https://stackoverflow.com/a/20167458

import sys
from PyQt5 import QtCore, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('stack post: https://stackoverflow.com/a/20167458')
        self.checkbox = QtWidgets.QCheckBox('Delete')
        self.button = QtWidgets.QPushButton('Open', self)
        self.button.clicked.connect(self.openDialog)
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.button)

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

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 300, 100, 50)
    window.show()
    sys.exit(app.exec_())