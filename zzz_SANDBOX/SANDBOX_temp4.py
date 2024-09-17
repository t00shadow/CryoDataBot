import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Example(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.tree = QtWidgets.QTreeWidget(self)
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(['Items'])

        # Create items
        self.parent_item = QtWidgets.QTreeWidgetItem(self.tree, ['Parent Item'])
        self.child_item1 = QtWidgets.QTreeWidgetItem(self.parent_item, ['Child Item 1'])
        self.child_item2 = QtWidgets.QTreeWidgetItem(self.parent_item, ['Child Item 2'])

        # Create buttons to delete child items
        delete_child1_button = QtWidgets.QPushButton('Delete Child Item 1', self)
        delete_child2_button = QtWidgets.QPushButton('Delete Child Item 2', self)
        
        delete_child1_button.clicked.connect(self.delete_child1)
        delete_child2_button.clicked.connect(self.delete_child2)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.tree)
        layout.addWidget(delete_child1_button)
        layout.addWidget(delete_child2_button)

    def delete_child1(self):
        self.parent_item.removeChild(self.child_item1)

    def delete_child2(self):
        self.parent_item.removeChild(self.child_item2)

#===============================================================================
# Unit Testing
#===============================================================================
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Example()
    window.show()
    sys.exit(app.exec_())
