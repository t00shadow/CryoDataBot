# booty gpt code, but good enough to prove can work.
# The key is to just make custom widgets like the token tagging input box, and then insert them under a QTreeWidgetItem that's set as its parent.

import sys
from PyQt5.QtWidgets import (
    QApplication, QTreeWidget, QTreeWidgetItem, QWidget, QHBoxLayout,
    QLabel, QComboBox, QLineEdit, QCompleter, QVBoxLayout
)
from PyQt5.QtCore import QStringListModel

class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super(CustomWidget, self).__init__(parent)

        # Create the layout
        layout = QHBoxLayout(self)

        # Create label
        label = QLabel("Label:", self)
        layout.addWidget(label)

        # First combobox
        combobox1 = QComboBox(self)
        combobox1.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addWidget(combobox1)

        # Line edit with completer
        line_edit = QLineEdit(self)
        completer = QCompleter()
        completer_model = QStringListModel(["Complete 1", "Complete 2", "Complete 3"])
        completer.setModel(completer_model)
        line_edit.setCompleter(completer)
        layout.addWidget(line_edit)

        # Second combobox
        combobox2 = QComboBox(self)
        combobox2.addItems(["Choice A", "Choice B", "Choice C"])
        layout.addWidget(combobox2)

        # Adjust layout
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

class TreeWidgetWithCustomRow(QTreeWidget):
    def __init__(self, parent=None):
        super(TreeWidgetWithCustomRow, self).__init__(parent)
        
        # Set headers for the tree widget
        self.setHeaderLabels(["Main Item", "Details"])
        
        # Add a top-level item
        top_item = QTreeWidgetItem(self, ["Item 1"])
        self.addTopLevelItem(top_item)

        # Add the custom row as a child item widget
        self.add_custom_row(top_item)
        
        # Add another top-level item
        top_item2 = QTreeWidgetItem(self, ["Item 2"])
        self.addTopLevelItem(top_item2)
        
        # Add another custom row as a child item widget
        self.add_custom_row(top_item2)

    def add_custom_row(self, parent_item):
        # Create the custom widget
        custom_row = CustomWidget(self)

        # Add a child item
        child_item = QTreeWidgetItem(parent_item)
        parent_item.addChild(child_item)

        # Set the custom widget as the widget for the second column
        self.setItemWidget(child_item, 1, custom_row)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the tree widget
    tree_widget = TreeWidgetWithCustomRow()
    tree_widget.setWindowTitle("QTreeWidget with Custom Subitem Row")
    tree_widget.resize(400, 300)
    
    tree_widget.show()
    sys.exit(app.exec_())
