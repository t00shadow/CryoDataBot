import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTreeWidget, QTreeWidgetItem, QHBoxLayout
from PyQt5.QtCore import Qt

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
        
        # Create the QTreeWidget with 3 columns
        self.tree_widget = QTreeWidget()
        self.tree_widget.setColumnCount(3)
        self.tree_widget.setHeaderLabels(["Name", "Price", "Color"])

        # Add widgets to the main layout
        self.layout.addLayout(self.button_layout)
        self.layout.addWidget(self.tree_widget)
        
        # Set the layout for the main window
        self.setLayout(self.layout)
        self.setWindowTitle("TreeWidget with Editable Subitems")

    def add_group(self):
        """Add a new group to the tree widget (top-level item, non-editable)."""
        group_name = f"Group {self.tree_widget.topLevelItemCount() + 1}"
        group_item = QTreeWidgetItem([group_name, "", ""])
        group_item.setFlags(group_item.flags() & ~Qt.ItemIsEditable)  # Make the group item non-editable
        self.tree_widget.addTopLevelItem(group_item)

        # Automatically select the newly added group
        self.tree_widget.setCurrentItem(group_item)

    def add_label(self):
        """Add a label (subitem, editable) to the selected group or the parent group of the selected label."""
        selected_item = self.tree_widget.currentItem()

        # Check if a group or label is selected
        if selected_item is not None:
            if selected_item.parent() is None:
                # If a group is selected, add a label to the group
                group_item = selected_item
            else:
                # If a label is selected, add a label to its parent group
                group_item = selected_item.parent()

            label_name = f"Label {group_item.childCount() + 1}"
            label_item = QTreeWidgetItem([label_name, "", ""])
            label_item.setFlags(label_item.flags() | Qt.ItemIsEditable)  # Allow editing of the label item
            group_item.addChild(label_item)
            group_item.setExpanded(True)  # Automatically expand the group when a label is added

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TreeWidgetApp()
    window.show()
    sys.exit(app.exec_())
