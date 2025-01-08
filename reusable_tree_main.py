from PyQt5 import QtWidgets as qtw
from reusable_tree_utils import TreeWidgetManager

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # Setup your UI here (load from .ui file or create programmatically)
        self.tree_widget = qtw.QTreeWidget()
        self.add_label_button = qtw.QPushButton("Add Label")
        self.status_bar = self.statusBar()

        # Initialize TreeWidgetManager
        self.tree_manager = TreeWidgetManager(
            self.tree_widget,
            add_label_button=self.add_label_button,
            status_bar=self.status_bar
        )

        # Example button connections
        add_group_button = qtw.QPushButton("Add Group")
        add_group_button.clicked.connect(self.tree_manager.add_group)

        self.add_label_button.clicked.connect(self.tree_manager.add_label)
        self.add_label_button.setDisabled(True)  # Initially disabled

        # Layout
        central_widget = qtw.QWidget()
        layout = qtw.QVBoxLayout()
        layout.addWidget(add_group_button)
        layout.addWidget(self.add_label_button)
        layout.addWidget(self.tree_widget)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = qtw.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
