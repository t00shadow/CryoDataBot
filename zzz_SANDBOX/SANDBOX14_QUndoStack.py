from PyQt5.QtWidgets import QApplication, QListWidget, QPushButton, QVBoxLayout, QWidget, QUndoStack, QUndoCommand, QShortcut
from PyQt5.QtGui import QKeySequence
import sys

# Custom command to add an item to the list
class AddCommand(QUndoCommand):
    def __init__(self, list_widget, item_text):
        super().__init__()
        self.list_widget = list_widget
        self.item_text = item_text
        self.row = None
        self.setText(f"Add {item_text}")

    def redo(self):
        if self.row is None:
            self.list_widget.addItem(self.item_text)
            self.row = self.list_widget.count() - 1
        else:
            self.list_widget.insertItem(self.row, self.item_text)

    def undo(self):
        self.list_widget.takeItem(self.row)

# Custom command to delete an item from the list
class DeleteCommand(QUndoCommand):
    def __init__(self, list_widget):
        super().__init__()
        self.list_widget = list_widget
        self.item = None
        self.row = self.list_widget.currentRow()
        if self.row != -1:
            self.item = self.list_widget.item(self.row).text()
        self.setText(f"Delete {self.item}")

    def redo(self):
        if self.row != -1:
            self.list_widget.takeItem(self.row)

    def undo(self):
        if self.row != -1:
            self.list_widget.insertItem(self.row, self.item)

# Main window class
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QListWidget and buttons
        self.list_widget = QListWidget(self)
        self.add_button = QPushButton("Add Item", self)
        self.delete_button = QPushButton("Delete Selected Item", self)
        self.undo_button = QPushButton("Undo", self)
        self.redo_button = QPushButton("Redo", self)

        # Create an undo stack
        self.undo_stack = QUndoStack(self)

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.undo_button)
        layout.addWidget(self.redo_button)

        # Connect buttons to their functions
        self.add_button.clicked.connect(self.add_item)
        self.delete_button.clicked.connect(self.delete_item)
        self.undo_button.clicked.connect(self.undo_stack.undo)
        self.redo_button.clicked.connect(self.undo_stack.redo)

        # Add keyboard shortcuts
        undo_shortcut = QShortcut(QKeySequence("Ctrl+Z"), self)
        undo_shortcut.activated.connect(self.undo_stack.undo)

        redo_shortcut = QShortcut(QKeySequence("Ctrl+Y"), self)
        redo_shortcut.activated.connect(self.undo_stack.redo)

    def add_item(self):
        item_text = f"Item {self.list_widget.count() + 1}"
        command = AddCommand(self.list_widget, item_text)
        self.undo_stack.push(command)

    def delete_item(self):
        if self.list_widget.currentItem():
            command = DeleteCommand(self.list_widget)
            self.undo_stack.push(command)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
