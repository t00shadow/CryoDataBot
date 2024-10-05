import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSplitter, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        # Create a splitter
        self.splitter = QSplitter(Qt.Horizontal)

        # Create widgets
        self.sidebar = QPushButton("Sidebar")
        self.sidebar.setMinimumWidth(70)
        self.sidebar.setMaximumWidth(150)
        self.content = QLabel("Content")
        self.right_widget = QLabel("Right Widget")

        # Add widgets to the splitter
        self.splitter.addWidget(self.sidebar)
        self.splitter.addWidget(self.content)
        self.splitter.addWidget(self.right_widget)
        self.splitter.setCollapsible(0, False)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.splitter)
        self.setLayout(layout)

        # Connect the splitter's splitterMoved signal to a slot
        self.splitter.splitterMoved.connect(self.on_splitter_moved)

        # Set window properties
        self.setWindowTitle('QSplitter IndexOf Example')
        self.setGeometry(300, 300, 800, 400)

    def on_splitter_moved(self, pos, index):
        """Slot called when the splitter is moved."""
        print(f"Splitter moved. Position: {pos}, Index: {index}")
        
        # Print the index of the handle (0 for the first handle, 1 for the second handle, etc.)
        handle_index = self.splitter.indexOf(self.splitter.handle(index))
        print(f"Handle index: {handle_index}")

        if index == 1:
            if pos < 150:    # note: works on the way back bc it ALSO triggers this condition, so dont need an else
                print("asdfsaf")
                self.splitter.setSizes([70, 200, 200])

# Boilerplate code to run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())