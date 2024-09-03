'''
THIS FILE IS COMPLETELY UNNEEDED NOW.

QT designer (for pyqt5) has this builtin for spinboxes. Just look for the suffix property. Even the docs list this property.
'''

from PyQt5.QtWidgets import QApplication, QSpinBox, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt


#1  (use super for initilization instead? this is from pyqt4, buttt works here so shrug)
class MySpinBox(QSpinBox):
    def __init__(self, *args):
        QSpinBox.__init__(self, *args)

        # self.setRange(0,9999)
        self.setRange(0,100)
        self.setSuffix("%") 

    def textFromValue(self, value):
        # return "%04d" % value
        return f"{value}"


#2
class PercentageSpinBox(QSpinBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSuffix("%")  # Add percentage symbol
        self.setValue(20)     # Set initial value
        self.setAlignment(Qt.AlignCenter)  # Align the text to the center

    # Optionally, you can override how the text is displayed
    def textFromValue(self, value):
        return f"{value}"  # Customize the display text with a percentage sign

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        
        # Create and add the PercentageSpinBox to the layout
        self.spin_box = PercentageSpinBox()
        layout.addWidget(self.spin_box)
        # Create and add the MySpinBox to the layout
        self.spin_box2 = MySpinBox()
        layout.addWidget(self.spin_box2)

        self.setLayout(layout)
        self.setWindowTitle("Percentage SpinBox Example")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
