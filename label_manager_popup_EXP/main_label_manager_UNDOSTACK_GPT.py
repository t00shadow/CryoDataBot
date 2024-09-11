import sys
from PyQt5.QtWidgets import QApplication, QDialog, QListWidgetItem, QUndoStack, QUndoCommand, QVBoxLayout, QPushButton, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt
from label_manager_popup import Ui_Dialog  # Import the generated UI file


# Added qundostack using gpt (soooo yeah rewrite/verify)

# Command for adding a group
class AddGroupCommand(QUndoCommand):
    def __init__(self, dialog, group_name):
        super().__init__()
        self.dialog = dialog
        self.group_name = group_name
        self.group_item = None
        self.setText(f"Add {self.group_name}")

    def redo(self):
        """Perform the action to add a group."""
        self.group_item = QListWidgetItem(self.group_name)
        self.group_item.setFlags(self.group_item.flags() | Qt.ItemIsEditable)

        current_row = self.dialog.ui.listWidget_groups.currentRow()
        self.dialog.ui.listWidget_groups.insertItem(current_row + 1, self.group_item)
        self.dialog.ui.listWidget_groups.setCurrentItem(self.group_item)

    def undo(self):
        """Undo the action of adding a group."""
        row = self.dialog.ui.listWidget_groups.row(self.group_item)
        self.dialog.ui.listWidget_groups.takeItem(row)

# Command for deleting a group
class DeleteGroupCommand(QUndoCommand):
    def __init__(self, dialog):
        super().__init__()
        self.dialog = dialog
        self.selected_item = self.dialog.ui.listWidget_groups.currentItem()
        self.row = self.dialog.ui.listWidget_groups.currentRow()
        if self.selected_item is not None:
            self.group_name = self.selected_item.text()
        self.setText(f"Delete {self.group_name}")

    def redo(self):
        """Perform the action to delete the selected group."""
        self.dialog.ui.listWidget_groups.takeItem(self.row)

    def undo(self):
        """Undo the action of deleting the group."""
        self.dialog.ui.listWidget_groups.insertItem(self.row, self.selected_item)
        self.dialog.ui.listWidget_groups.setCurrentItem(self.selected_item)

# Main window class
class MainApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI

        # Create a QUndoStack to manage undo and redo commands
        self.undo_stack = QUndoStack(self)

        # Console logging connections
        self.ui.addgroup_btn.clicked.connect(self.on_button_click)
        self.ui.delgroup_btn.clicked.connect(self.on_button_click)

        # Core functionality connections
        self.ui.listWidget_groups.clear()
        self.ui.addgroup_btn.clicked.connect(self.add_group)
        self.ui.delgroup_btn.clicked.connect(self.del_group)

        # Add keyboard shortcuts for Undo/Redo
        undo_shortcut = QShortcut(QKeySequence("Ctrl+Z"), self)
        undo_shortcut.activated.connect(self.undo_stack.undo)

        redo_shortcut = QShortcut(QKeySequence("Ctrl+Y"), self)
        redo_shortcut.activated.connect(self.undo_stack.redo)

    def on_button_click(self):
        print("Button clicked!")
        print(f"Groups count: {self.ui.listWidget_groups.count()}")

    def add_group(self):
        """Add a new group to the list widget (top-level item, editable)."""
        group_name = f"Group {self.ui.listWidget_groups.count() + 1}"
        command = AddGroupCommand(self, group_name)
        self.undo_stack.push(command)

    def del_group(self):
        """Delete the selected group."""
        if self.ui.listWidget_groups.currentItem() is not None:
            command = DeleteGroupCommand(self)
            self.undo_stack.push(command)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())