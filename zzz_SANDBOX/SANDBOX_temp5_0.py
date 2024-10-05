import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QSplitter, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSizePolicy
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        # Layout for the sidebar
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        # Add buttons with icons and text
        self.buttons = []
        self.add_button("Home", "GUI_custom_widgets/svgs/lock-open-svgrepo-com.svg")
        self.add_button("Search", "GUI_custom_widgets/svgs/reset-hard-svgrepo-com.svg")
        self.add_button("Library", "GUI_custom_widgets/svgs/cog-svgrepo-com.svg")
        
        self.is_collapsed = False

    def add_button(self, text, icon_path):
        """Helper function to add buttons with both icons and text."""
        button = QPushButton(text)
        button.setIcon(QIcon(icon_path))
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        button.setIconSize(QSize(24, 24))
        self.layout.addWidget(button)
        self.buttons.append(button)
    
    def collapse(self):
        """Collapse sidebar by hiding button text, showing only icons."""
        for button in self.buttons:
            button.setText("")  # Hide the text
    
    def expand(self):
        """Expand sidebar by showing button text along with icons."""
        self.buttons[0].setText("Home")
        self.buttons[1].setText("Search")
        self.buttons[2].setText("Library")

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create a sidebar widget
        self.sidebar = Sidebar()

        # Main content area
        self.content = QLabel("Main Content Area")
        
        # Create a splitter
        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.sidebar)
        self.splitter.addWidget(self.content)
        

        # Set initial sidebar width
        self.splitter.setSizes([200, 600])  # Sidebar width: 200, Content width: 600
        
        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.splitter)
        self.setLayout(layout)
        
        # Listen to the splitter resizing to collapse the sidebar dynamically
        self.splitter.splitterMoved.connect(self.handle_sidebar_resize)

        # Set window properties
        self.setWindowTitle('Spotify-like Snappy (rough) Sidebar Collapse Example')
        self.setGeometry(300, 300, 800, 400)

    def handle_sidebar_resize(self, pos, index):
        """Detect when the sidebar is resized to a small width and collapse/expand accordingly."""
        sidebar_width = self.splitter.sizes()[0]  # Get width of the sidebar
        
        # Threshold for collapsing the sidebar (e.g., less than 100 pixels)
        if sidebar_width < 100 and not self.sidebar.is_collapsed:
            self.sidebar.collapse()
            self.sidebar.is_collapsed = True
        elif sidebar_width >= 100 and self.sidebar.is_collapsed:
            self.sidebar.expand()
            self.sidebar.is_collapsed = False

# Boilerplate code to run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
