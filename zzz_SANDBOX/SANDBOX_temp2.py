import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QDesktopWidget, QVBoxLayout, QWidget, 
    QLabel, QPushButton, QTextEdit
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Add some widgets to test the layout and resizing
        self.label = QLabel("This is a test label.", self)
        self.button = QPushButton("Click Me!", self)
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Write something here...")

        # Add widgets to layout
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.text_edit)

        # Get screen size
        screen = QDesktopWidget().availableGeometry()
        screen_width = screen.width()
        screen_height = screen.height()

        # Set initial window size
        self.setGeometry(100, 100, 800, 600)  # Some default size

        # Adjust max height or max width depending on which runs out first
        self.adjustSizeToScreen(screen_width, screen_height)

    def adjustSizeToScreen(self, screen_width, screen_height):
        # Get current window size
        window_width = self.width()
        window_height = self.height()

        # Determine which dimension to prioritize
        if window_width > screen_width or window_height > screen_height:
            # Fit window to either width or height
            if screen_width / window_width < screen_height / window_height:
                # Limit by width
                self.setMaximumSize(screen_width, screen_height)
                self.resize(screen_width, int(window_height * (screen_width / window_width)))
            else:
                # Limit by height
                self.setMaximumSize(screen_width, screen_height)
                self.resize(int(window_width * (screen_height / window_height)), screen_height)
    
    # Optional: Override resize event for dynamic resizing
    def resizeEvent(self, event):
        screen = QDesktopWidget().availableGeometry()
        self.adjustSizeToScreen(screen.width(), screen.height())
        super().resizeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())