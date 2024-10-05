import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QListWidgetItem, QLineEdit, QHBoxLayout
from PyQt5.QtCore import Qt

class EditableListWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

        self.item_numbers = set()  # Internal list to store existing item numbers

    def init_ui(self):
        layout = QVBoxLayout()

        # List widget to display items
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        # Add buttons
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Item")
        self.delete_button = QPushButton("Delete Selected Item")
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.delete_button)

        layout.addLayout(button_layout)

        # Connect button signals
        self.add_button.clicked.connect(self.add_item)
        self.delete_button.clicked.connect(self.delete_item)

        # Handle editing finish signal
        self.list_widget.itemChanged.connect(lambda: print("item changed"))
        self.list_widget.itemChanged.connect(self.on_item_edited)

        self.setLayout(layout)
        self.setWindowTitle("Editable List")
        self.show()

    def add_item(self):
        """ Add a new item to the list with the lowest available item number. """
        # Find the lowest available item number
        new_item_num = self.get_lowest_available_number()

        # Add new item number to internal list
        self.item_numbers.add(new_item_num)

        # Create the item and make it editable
        item_name = f"item{new_item_num}"
        list_item = QListWidgetItem(item_name)
        list_item.setFlags(list_item.flags() | Qt.ItemIsEditable)
        list_item.setData(Qt.UserRole, item_name)  # Store initial name for future reference

        # Add the item to the list widget
        self.list_widget.addItem(list_item)

    def delete_item(self):
        """ Delete selected items and refresh the internal list of numbers. """
        selected_items = self.list_widget.selectedItems()
        if not selected_items:
            return

        # Delete selected items from the list
        for item in selected_items:
            self.list_widget.takeItem(self.list_widget.row(item))

        # Refresh the internal list of item numbers after deletion
        self.refresh_item_numbers()

    def on_item_edited(self, item):
        """ Update internal list of numbers when an item is edited. """
        # Refresh the internal list of item numbers
        self.refresh_item_numbers()

    def refresh_item_numbers(self):
        """ Refresh the internal list of numbers by analyzing all items in the list. """
        self.item_numbers.clear()

        for i in range(self.list_widget.count()):
            list_item = self.list_widget.item(i)
            item_name = list_item.text()

            # If the item name follows the itemX format, extract the number and store it
            if item_name.startswith("item"):
                try:
                    item_num = int(item_name[4:])
                    self.item_numbers.add(item_num)
                except ValueError:
                    pass

    def get_lowest_available_number(self):
        """ Get the lowest available number that can be used for a new item. """
        num = 1
        while num in self.item_numbers:
            num += 1
        return num


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EditableListWidget()
    sys.exit(app.exec_())
