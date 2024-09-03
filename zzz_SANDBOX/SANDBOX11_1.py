import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTreeWidget, QTreeWidgetItem, QHBoxLayout

class TreeWidgetApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main layout
        self.layout = QVBoxLayout()
        
        # Create the buttons
        self.btn_add_group = QPushButton("Add Group")
        self.btn_add_label = QPushButton("Add Label")
        
        # Connect buttons to functions
        self.btn_add_group.clicked.connect(self.add_group)
        self.btn_add_label.clicked.connect(self.add_label)

        # Create a horizontal layout for buttons
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.btn_add_group)
        self.button_layout.addWidget(self.btn_add_label)
        
        # Create the QTreeWidget
        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabels(["Groups and Labels"])

        # Add widgets to the main layout
        self.layout.addLayout(self.button_layout)
        self.layout.addWidget(self.tree_widget)
        
        # Set the layout for the main window
        self.setLayout(self.layout)
        self.setWindowTitle("TreeWidget Example")

    def add_group(self):
        """Add a new group to the tree widget."""
        group_name = f"Group {self.tree_widget.topLevelItemCount() + 1}"
        group_item = QTreeWidgetItem([group_name])
        self.tree_widget.addTopLevelItem(group_item)

    def add_label(self):
        """Add a label (subitem) to the selected group."""
        selected_item = self.tree_widget.currentItem()

        if selected_item is not None and selected_item.parent() is None:  # Ensure a group is selected
            label_name = f"Label {selected_item.childCount() + 1}"
            label_item = QTreeWidgetItem([label_name])
            selected_item.addChild(label_item)
            selected_item.setExpanded(True)  # Automatically expand the group when a label is added

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TreeWidgetApp()
    window.show()
    sys.exit(app.exec_())
