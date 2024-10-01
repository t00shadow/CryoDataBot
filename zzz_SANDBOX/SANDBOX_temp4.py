import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt

# Create a modern-styled window with multiple pages using a color scheme
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Cryo-EM Themed GUI")
        self.setGeometry(100, 100, 600, 400)

        # Main layout container
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # Create pages
        self.home_page = self.create_home_page()
        self.page_1 = self.create_page("Page 1")
        self.page_2 = self.create_page("Page 2")

        # Add pages to stack
        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.page_1)
        self.stack.addWidget(self.page_2)

        # Set default page
        self.stack.setCurrentWidget(self.home_page)

        # Apply color scheme
        self.apply_color_scheme()

    def create_home_page(self):
        """Create the home page with navigation buttons"""
        page = QWidget()
        layout = QVBoxLayout()

        # Home page label
        label = QLabel("Home Page")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 24px; color: #1D3557;")  # Steel Gray for text
        layout.addWidget(label)

        # Navigation buttons
        btn_page1 = QPushButton("Go to Page 1")
        btn_page1.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_1))
        btn_page1.setStyleSheet(self.button_style())

        btn_page2 = QPushButton("Go to Page 2")
        btn_page2.clicked.connect(lambda: self.stack.setCurrentWidget(self.page_2))
        btn_page2.setStyleSheet(self.button_style())

        layout.addWidget(btn_page1)
        layout.addWidget(btn_page2)

        page.setLayout(layout)
        return page

    def create_page(self, title):
        """Create a generic page with a back button"""
        page = QWidget()
        layout = QVBoxLayout()

        label = QLabel(title)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 24px; color: #1D3557;")  # Steel Gray for text
        layout.addWidget(label)

        # Back button to return to home
        btn_back = QPushButton("Back to Home")
        btn_back.clicked.connect(lambda: self.stack.setCurrentWidget(self.home_page))
        btn_back.setStyleSheet(self.button_style())
        layout.addWidget(btn_back)

        page.setLayout(layout)
        return page

    def button_style(self):
        """Return a modern button style"""
        return """
            QPushButton {
                background-color: #457B9D;  /* Electron Blue */
                color: #F1FAEE;             /* Frost White */
                padding: 10px;
                font-size: 18px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2A9D8F;  /* Cold Teal */
            }
        """

    def apply_color_scheme(self):
        """Set the main window's color palette to the Cryo-EM theme"""
        palette = QPalette()

        # Set primary background color (Ice Blue)
        palette.setColor(QPalette.Window, QColor("#A8DADC"))
        
        # Set text color for labels
        palette.setColor(QPalette.WindowText, QColor("#1D3557"))  # Steel Gray

        self.setPalette(palette)

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())