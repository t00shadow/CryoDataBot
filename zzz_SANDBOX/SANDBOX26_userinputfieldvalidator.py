from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import re  # For regex validation

class SearchValidatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Search Query Validator")
        self.resize(400, 200)

        # Layout and widgets
        self.layout = QVBoxLayout()
        
        # Input field
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Enter your search query")
        self.layout.addWidget(self.search_input)
        
        # Warning label
        self.warning_label = QLabel("", self)
        self.warning_label.setStyleSheet("color: red; font-size: 12px;")
        self.layout.addWidget(self.warning_label)

        # Connect signals
        self.search_input.textChanged.connect(self.validate_search_query)

        self.setLayout(self.layout)

    def validate_search_query(self, text):
        # Define your validation logic (example: simple regex for allowed characters)
        if not re.match(r"^[a-zA-Z0-9\s]*$", text):
            self.warning_label.setText("Warning: Search query contains invalid characters!")
        # # Check if parentheses are balanced for complex queries
        # if text.count('(') != text.count(')'):
        #     self.warning_label.setText("Warning: Unbalanced parentheses detected.")
        #     return        
        # # Check if brackets are balanced for complex queries
        # if text.count('[') != text.count(']'):
        #     self.warning_label.setText("Warning: Unbalanced brackets detected.")
        #     return
        else:
            self.warning_label.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = SearchValidatorApp()
    window.show()
    app.exec_()
