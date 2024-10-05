import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QSplitter, QVBoxLayout, QPushButton, QLabel, QSizePolicy
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
        self.buttons = []        # NOTE: ohhhh this is one way to access the buttons (start)
        self.add_button("Home", "GUI_custom_widgets/svgs/lock-open-svgrepo-com.svg")
        self.add_button("Search", "GUI_custom_widgets/svgs/reset-hard-svgrepo-com.svg")
        self.add_button("Library", "GUI_custom_widgets/svgs/cog-svgrepo-com.svg")

    def add_button(self, text, icon_path):
        """Helper function to add buttons with both icons and text."""
        button = QPushButton(text)
        button.setIcon(QIcon(icon_path))
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        button.setIconSize(QSize(24, 24))
        self.layout.addWidget(button)
        self.buttons.append(button)        # NOTE: ohhhh this is one way to access the buttons (end)
    
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
    COLLAPSED_WIDTH = 100  # Width when collapsed
    EXPANDED_WIDTH = 300  # Width when expanded
    
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

        # Set minimum width for the sidebar to prevent dragging below COLLAPSED_WIDTH
        self.sidebar.setMinimumWidth(self.COLLAPSED_WIDTH)

        # Set initial sidebar width
        self.splitter.setSizes([self.EXPANDED_WIDTH, 600])  # Sidebar width: 200, Content width: 600
        
        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.splitter)
        
        # Add a hamburger button to toggle collapse/expand
        self.toggle_button = QPushButton("Toggle Sidebar")
        self.toggle_button.clicked.connect(self.toggle_sidebar)
        layout.addWidget(self.toggle_button)
        
        self.setLayout(layout)
        
        # Listen to the splitter resizing to snap the sidebar dynamically
        self.splitter.splitterMoved.connect(self.handle_sidebar_resize)

        # Set window properties
        self.setWindowTitle('Combined: same as 5_2 (snappy) but can also expand, expand is smooth tho')
        self.setGeometry(300, 300, 800, 400)

    def handle_sidebar_resize(self, pos, index):
        """Detect when the sidebar is resized and snap to collapsed or expanded width."""
        sidebar_width = self.splitter.sizes()[0]  # Get the width of the sidebar
        
        # Snap to COLLAPSED_WIDTH or EXPANDED_WIDTH based on current size
        if sidebar_width < (self.EXPANDED_WIDTH + self.COLLAPSED_WIDTH) // 2:
            self.snap_to_collapsed()
        elif sidebar_width >= (self.EXPANDED_WIDTH + self.COLLAPSED_WIDTH) // 2 and sidebar_width < self.EXPANDED_WIDTH:
            self.snap_to_expanded()

    def snap_to_collapsed(self):
        """Collapse the sidebar and set the size to COLLAPSED_WIDTH."""
        self.splitter.setSizes([self.COLLAPSED_WIDTH, self.width() - self.COLLAPSED_WIDTH])
        self.sidebar.collapse()

    def snap_to_expanded(self):
        """Expand the sidebar and set the size to EXPANDED_WIDTH."""
        self.splitter.setSizes([self.EXPANDED_WIDTH, self.width() - self.EXPANDED_WIDTH])
        self.sidebar.expand()

    def toggle_sidebar(self):
        """Toggle sidebar collapse/expand manually using the button."""
        sidebar_width = self.splitter.sizes()[0]
        if sidebar_width == self.COLLAPSED_WIDTH:
            self.snap_to_expanded()
        else:
            self.snap_to_collapsed()

# Boilerplate code to run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
