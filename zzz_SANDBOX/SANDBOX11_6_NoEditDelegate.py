from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QPushButton, QStyledItemDelegate
from PyQt5.QtCore import Qt

class NoEditDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def createEditor(self, parent, option, index):
        # Return None to prevent editing
        return None

class TreeWidgetApp(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        
        # Create the QTreeWidget with 3 columns
        self.tree_widget = QTreeWidget()
        self.tree_widget.setColumnCount(3)
        self.tree_widget.setHeaderLabels(["Name", "Price", "Color"])

        # Set the delegate for the first column
        self.tree_widget.setItemDelegateForColumn(0, NoEditDelegate(self))

        # Add a sample item
        item = QTreeWidgetItem(["Editable Name", "100", "Red"])
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.tree_widget.addTopLevelItem(item)

        self.layout.addWidget(self.tree_widget)
        self.setLayout(self.layout)
        self.setWindowTitle("TreeWidget with Custom Delegate")

if __name__ == "__main__":
    app = QApplication([])
    window = TreeWidgetApp()
    window.show()
    app.exec_()
