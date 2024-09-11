# this is actually not too good b/c it the lineedit can continue underneath the button (and label) just get clever with a parent widget and qstylesheets. That approach is actually better cuz obeys boundaries.


from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumWidth(1000)

        # Create the layout
        pSearchLayout = QHBoxLayout()
        
        # Add stretchable space
        pSearchLayout.addStretch()
        
        # Create and add the button
        self.pushButton = QPushButton("Search")
        pSearchLayout.addWidget(self.pushButton)

        self.label1 = QLabel("Label 1")
        self.label1.setStyleSheet("""
            QLabel {
                border: 2px solid darkkhaki;
                padding: 5px;
                border-radius: 3px;
                opacity: 200;
                margin: 2px;
            }
        """)
        self.label1.setTextInteractionFlags(Qt.TextEditable | Qt.TextSelectableByMouse)
        pSearchLayout.addWidget(self.label1)
        
        # Set spacing and margins
        pSearchLayout.setSpacing(0)
        pSearchLayout.setContentsMargins(0, 0, 0, 0)
        
        # Create the line edit and set its layout
        self.lineEditSearch = QLineEdit()
        self.lineEditSearch.setLayout(pSearchLayout)
        
        # Set up the main window
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.lineEditSearch)
        self.setLayout(mainLayout)
        
        self.setWindowTitle("Search Example")

app = QApplication([])
window = Example()
window.show()
app.exec_()
