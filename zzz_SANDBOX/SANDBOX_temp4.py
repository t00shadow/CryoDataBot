from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QComboBox, QTableView, QTreeView
)
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QMouseEvent, QStandardItemModel, QStandardItem


class CustomComboBox(QComboBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setEditable(True)  # Optional, allows typing in the combo box

    # Override showPopup to install an event filter that will keep the popup open
    def showPopup(self):
        super().showPopup()
        # Install an event filter to control closing the popup
        self.view().viewport().installEventFilter(self)

    # Event filter to handle clicks on items in the view
    def eventFilter(self, obj, event):
        if isinstance(event, QMouseEvent):
            if event.type() == QMouseEvent.MouseButtonRelease:
                index = self.view().indexAt(event.pos())
                if index.isValid():
                    # Get the item at the clicked index
                    item = self.model().itemFromIndex(index)
                    if item.isCheckable():
                        # Toggle the checkbox state only if it's not already checked
                        if item.checkState() == Qt.Unchecked:
                            item.setCheckState(Qt.Checked)
                        else:
                            item.setCheckState(Qt.Unchecked)

                    return True  # Return True to keep the popup open after clicking
        return super().eventFilter(obj, event)


class ComboBoxViewsDemo(QWidget):
    def __init__(self):
        super().__init__()

        # Layout for the window
        layout = QVBoxLayout(self)

        # ComboBox with QTableView and Checkboxes
        self.table_combo = CustomComboBox(self)
        tableView = QTableView()
        tableView.horizontalHeader().setVisible(False)
        tableView.verticalHeader().setVisible(False)
        print(type(tableView))
        self.table_combo.setView(tableView)

        # Set up a model with multiple columns and checkboxes for the QTableView combo
        self.table_model = QStandardItemModel()
        self.table_combo.setModel(self.table_model)

        ### The following 2 versions of code accomplish the same thing (with maybe noteable difference in performance, setting rows is prob more efficient than single items since less function call overhead b/c less function calls)

        ### Set one table ROW at a time
        # for row in range(4):
        #     items = []
        #     for col in range(3):
        #         item = QStandardItem(f"Item {row} - Col {col}")
        #         item.setCheckable(True)
        #         item.setCheckState(Qt.Unchecked)
        #         items.append(item)
        #     table_model.appendRow(items)
        
        ### Set one table ITEM at a time
        for row in range(4):
            for col in range(3):
                item = QStandardItem(f"Item {row} - Col {col}")
                item.setCheckable(True)  # Make each item checkable
                item.setCheckState(Qt.Unchecked)  # Start as unchecked
                self.table_model.setItem(row, col, item)

        self.table_model.itemChanged.connect(self.updateLineEdit)
        layout.addWidget(self.table_combo)

        # ComboBox with QTreeView and Checkboxes
        tree_combo = CustomComboBox(self)
        treeView = QTreeView()
        tree_combo.setView(treeView)

        # Set up a tree model with checkboxes for the QTreeView combo
        tree_model = QStandardItemModel()
        tree_combo.setModel(tree_model)
        root_node = tree_model.invisibleRootItem()

        for i in range(3):
            parent_item = QStandardItem(f"Parent {i}")
            parent_item.setCheckable(True)
            parent_item.setCheckState(Qt.Unchecked)
            for j in range(2):
                child_item = QStandardItem(f"Child {i}.{j}")
                child_item.setCheckable(True)
                child_item.setCheckState(Qt.Unchecked)
                parent_item.appendRow(child_item)
            root_node.appendRow(parent_item)

        layout.addWidget(tree_combo)

        self.setLayout(layout)
        self.setWindowTitle('QComboBox with Persistent Popup and Checkboxes')
    
    def updateLineEdit(self):
        checked_items = []
        if self.table_model.item(0, 0).checkState() == Qt.Checked:
            print("select all")
        else:
            for row in range(self.table_model.rowCount()):
                for col in range(self.table_model.columnCount()):
                    item = self.table_model.item(row, col)
                    if item.checkState() == Qt.Checked:
                        checked_items.append(item.text())
        
        # Update the line edit with checked items
        self.table_combo.lineEdit().setText(", ".join(checked_items))

if __name__ == '__main__':
    app = QApplication([])

    window = ComboBoxViewsDemo()
    window.show()

    app.exec_()
