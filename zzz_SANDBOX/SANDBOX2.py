import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget, QCheckBox, QTextEdit, QAbstractItemView
from PyQt5.QtCore import Qt, pyqtSignal, QPoint

class CheckBoxDropdown(QWidget):
    checkboxChanged = pyqtSignal(list)

    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.Popup)  # Make the widget act as a popup
        
        # Create a vertical layout for the checkboxes
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        
        # Create and add checkboxes to the layout
        self.checkboxes = []
        for item in items:
            checkbox = QCheckBox(item, self)
            checkbox.stateChanged.connect(self.update_checked_items)
            layout.addWidget(checkbox)
            self.checkboxes.append(checkbox)
        
        self.setLayout(layout)

    def update_checked_items(self):
        """ Update the list of checked items and emit signal """
        checked_items = [checkbox.text() for checkbox in self.checkboxes if checkbox.isChecked()]
        self.checkboxChanged.emit(checked_items)

class CustomComboBox(QComboBox):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.NoInsert)
        
        # Create and set the custom dropdown widget
        self.custom_dropdown = CheckBoxDropdown(items, self)
        self.custom_dropdown.checkboxChanged.connect(self.update_combobox)
        
        self.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view().setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.view().setMinimumWidth(self.custom_dropdown.sizeHint().width())

    def showPopup(self):
        """ Show the custom dropdown widget """
        self.custom_dropdown.setFixedWidth(self.view().size().width())
        self.custom_dropdown.move(self.mapToGlobal(QPoint(0, self.height())))
        self.custom_dropdown.show()

    def update_combobox(self, checked_items):
        """ Update the QComboBox with the list of checked items """
        self.setEditText(", ".join(checked_items))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 300)
        
        # Create an instance of CustomComboBox
        items = ["Option 1", "Option 2", "Option 3", "Option 4"]
        custom_combo_box = CustomComboBox(items)
        
        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(custom_combo_box)
        
        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())