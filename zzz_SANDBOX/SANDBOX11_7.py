from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QVBoxLayout, QWidget, QStyledItemDelegate
from PyQt5.QtCore import Qt, QModelIndex

class TreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(3)
        self.setHeaderLabels(["Name", "Price", "Color"])
        self.itemDoubleClicked.connect(self.on_item_double_clicked)

    def on_item_double_clicked(self, item, column):
        # Open the persistent editor for the double-clicked item and column
        if column == 1:  # Example: Only allow editing in the "Price" column
            self.openPersistentEditor(item, column)
        else:
            self.closePersistentEditor(item, column)
    
    def closeEvent(self, event):
        # Ensure persistent editors are closed before closing the widget
        for item in self.findItems("*", Qt.MatchWildcard):
            for col in range(self.columnCount()):
                self.closePersistentEditor(item, col)
        super().closeEvent(event)

class TreeWidgetApp(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        
        # Initialize the custom TreeWidget
        self.tree_widget = TreeWidget()

        # Add a sample item
        item = QTreeWidgetItem(["Editable Name", "100", "Red"])
        self.tree_widget.addTopLevelItem(item)
        item2 = QTreeWidgetItem(["ADAD", "12123", "Blue"])
        self.tree_widget.addTopLevelItem(item2)

        self.layout.addWidget(self.tree_widget)
        self.setLayout(self.layout)
        self.setWindowTitle("TreeWidget with Persistent Editors")

if __name__ == "__main__":
    app = QApplication([])
    window = TreeWidgetApp()
    window.show()
    app.exec_()
