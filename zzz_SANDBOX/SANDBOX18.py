import sys
import logging
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QHBoxLayout
from PyQt5.QtCore import Qt

# Custom logging handler to send logs to QTextEdit
class QTextEditLogger(logging.Handler):
    def __init__(self, text_edit):
        super().__init__()
        self.text_edit = text_edit

    def emit(self, record):
        msg = self.format(record)
        self.text_edit.append(msg)

# Function that performs random math operations and logs them
def perform_random_math_operations():
    logger.info("Starting math operations...")
    for i in range(5):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        operation = random.choice(['+', '-', '*', '/'])
        
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            # Handle division by zero
            result = a / (b if b != 0 else 1)

        logger.info(f"Operation {i+1}: {a} {operation} {b} = {result}")
    logger.info("Finished math operations.")

# Main window
class LogWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the QTextEdit widget for logging
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        # Set up the Run button
        self.run_button = QPushButton("Run", self)
        self.run_button.clicked.connect(self.run_operations)

        # Set up the Clear button
        self.clear_button = QPushButton("Clear", self)
        self.clear_button.clicked.connect(self.clear_logs)

        # Layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.run_button)
        button_layout.addWidget(self.clear_button)

        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        layout.addLayout(button_layout)
        self.setLayout(layout)

        # Configure logging
        self.configure_logging()

    def configure_logging(self):
        # Set up logging to QTextEdit
        text_edit_handler = QTextEditLogger(self.text_edit)
        text_edit_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))

        # Set up logging to file
        file_handler = logging.FileHandler('zzz_SANDBOX/log.txt', mode='a')
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))

        # Add both handlers to the logger
        logger.addHandler(text_edit_handler)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)

    def run_operations(self):
        perform_random_math_operations()

    def clear_logs(self):
        self.text_edit.clear()

# Initialize logger
logger = logging.getLogger(__name__)

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LogWindow()
    window.setWindowTitle("Logging Example with Random Math Operations")
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec_())
