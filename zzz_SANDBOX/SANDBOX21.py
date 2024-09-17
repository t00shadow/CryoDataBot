import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtCore import QEvent, QPoint

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.button = QPushButton('Click me', self)
        self.button.move(50, 50)
        self.button.resize(100, 30)

        self.button.clicked.connect(self.show_tooltip_on_click)

    def show_tooltip_on_click(self):
        QToolTip.showText(self.button.mapToGlobal(QPoint(0, self.button.height())), "This is a tooltip", self.button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.resize(200, 150)
    window.show()
    sys.exit(app.exec_())
