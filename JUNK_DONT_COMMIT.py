import sys
from PyQt5 import QtWidgets, QtCore

class Example(QtWidgets.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QtWidgets.QHBoxLayout(self)
        left = QtWidgets.QFrame(self)
        left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        right = QtWidgets.QFrame(self)
        right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(left)
        splitter.addWidget(right)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([125, 150])
        hbox.addWidget(splitter)
        self.setLayout(hbox)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Cleanlooks'))
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QtWidgets.QSplitter')
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()