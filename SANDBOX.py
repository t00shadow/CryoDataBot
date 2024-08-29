import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QCheckBox
from PyQt5.QtCore import Qt, pyqtSignal, QPoint

class CheckBoxDropdown(QWidget):
    # Signal to emit when checkboxes are changed
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

class CustomComboBox(QWidget):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Custom ComboBox with Checkboxes")
        
        # Create a QLineEdit to act as the combo box
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Select Options")
        self.line_edit.setGeometry(100, 100, 200, 40)
        self.line_edit.setReadOnly(True)  # Make the line edit read-only
        
        # Create the custom dropdown widget
        self.custom_dropdown = CheckBoxDropdown(items, self)
        
        # Connect the custom dropdown's signal to update the QLineEdit
        self.custom_dropdown.checkboxChanged.connect(self.update_line_edit)
        
        # Connect the QLineEdit's clicked signal to show the dropdown
        self.line_edit.mousePressEvent = self.show_dropdown_on_click
        
        # Set the size of the dropdown to fit its content
        self.custom_dropdown.setFixedWidth(self.line_edit.width())
        
    def show_dropdown_on_click(self, event):
        """ Show the custom dropdown widget when the QLineEdit is clicked """
        self.show_dropdown()

    def show_dropdown(self):
        """ Show the custom dropdown widget """
        # Position the dropdown below the QLineEdit
        pos = self.line_edit.mapToGlobal(QPoint(0, self.line_edit.height()))
        self.custom_dropdown.move(pos)
        self.custom_dropdown.show()
        
    def update_line_edit(self, checked_items):
        """ Update the QLineEdit with the list of checked items """
        self.line_edit.setText(", ".join(checked_items))

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