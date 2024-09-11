import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QListWidgetItem
from PyQt5.QtCore import Qt
from label_manager_popup import Ui_Dialog  # Import the generated UI file

class Dictlist(dict):
    def __setitem__(self, key, value):
        if key not in self:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)

class MainApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI

        self.labels_dict = Dictlist()     # group:label
        print(self.labels_dict)

        # Console logging connections
        self.ui.addgroup_btn.clicked.connect(self.on_button_click)
        self.ui.delgroup_btn.clicked.connect(self.on_button_click)
        self.ui.addlabel_btn.clicked.connect(self.on_button_click)
        self.ui.dellabel_btn.clicked.connect(self.on_button_click)

        # Actual core functionality connections
        self.ui.listWidget_groups.clear()
        self.ui.listWidget_labels.clear()
        self.add_group()
        self.add_label()
        self.ui.addgroup_btn.clicked.connect(self.add_group)
        self.ui.delgroup_btn.clicked.connect(self.del_group)
        self.ui.addlabel_btn.clicked.connect(self.add_label)
        # self.ui.listWidget_groups.currentItemChanged.connect(lambda:print("changed group"))
        # self.ui.listWidget_groups.itemSelectionChanged.connect(lambda:print("changed group"))   # us itemSelectionChanged if need to respond to multiselection
        self.ui.listWidget_groups.itemSelectionChanged.connect(self.load_labels)

    def on_button_click(self):
        # Example slot method triggered when the button is clicked
        print("Button clicked!")
        print(f"{self.ui.listWidget_groups.count()}    {self.ui.listWidget_labels.count()}")

    def add_group(self):
        self.ui.listWidget_groups.blockSignals(True)      # For a cleaner and more manageable way to block signals, use QSignalBlocker, which automatically unblocks signals when it goes out of scope.
        self.ui.listWidget_labels.blockSignals(True)
        """Add a new group to the groups list widget (editable)."""
        group_name = f"Group {self.ui.listWidget_groups.count() + 1}"
        group_item = QListWidgetItem(group_name)
        group_item.setFlags(group_item.flags() | Qt.ItemIsEditable)  # Make the group item editable

        # Add (always goes to bottom)
        # self.ui.listWidget_groups.addItem(group_item)

        # Insert (adds at specific row)
        current_row = self.ui.listWidget_groups.currentRow()    # wtf index starts at -1?? ig for empty listwidget
        self.ui.listWidget_groups.insertItem(current_row + 1, group_item)

        # Automatically select the newly added group
        self.ui.listWidget_groups.setCurrentItem(group_item)

        # self.labels_dict[group_name] = None
        self.labels_dict[group_name] = current_row + 1     # first value is now group index
        # self.labels_dict.setdefault(group_name)    # if key exists, does nothing and simply returns value
        print(self.labels_dict)
        self.ui.listWidget_groups.blockSignals(False)
        self.ui.listWidget_labels.blockSignals(False)

    def del_group(self):
        # Get the selected item
        selected_item = self.ui.listWidget_groups.currentItem()

        if selected_item is not None:
            # Remove the selected item from the QListWidget
            row = self.ui.listWidget_groups.row(selected_item)
            self.ui.listWidget_groups.takeItem(row)

            # Items removed from a list widget will not be managed by Qt, and will need to be deleted manually.
            del selected_item
        
        key = f"Group {self.ui.listWidget_groups.currentRow() + 1}"
        self.labels_dict.pop(key)
        print(self.labels_dict)

    def add_label(self):
        if self.ui.listWidget_groups.count() == 0:
            print("make a group first")
            return

        """Determine the selected group."""
        current_group_name = self.ui.listWidget_groups.currentItem().text()

        """Add a new group to the labels list widget (editable)."""
        label_name = f"Label {self.ui.listWidget_labels.count() + 1}"
        label_item = QListWidgetItem(label_name)
        label_item.setFlags(label_item.flags() | Qt.ItemIsEditable)  # Make the group item editable

        # Add (always goes to bottom)
        self.ui.listWidget_labels.addItem(label_item)

        # Insert (adds at specific row)
        # current_row = self.ui.listWidget_labels.currentRow()
        # self.ui.listWidget_labels.insertItem(current_row + 1, label_item)

        self.labels_dict[current_group_name] = label_name
        print(self.labels_dict)

    def load_labels(self):
        current_group_name = self.ui.listWidget_groups.currentItem().text()
        print("current group:", current_group_name)
        labels_to_load = self.labels_dict[current_group_name][1:]     # drop first value (group index)
        print("labels to load:", labels_to_load)
        self.ui.listWidget_labels.clear()
        self.ui.listWidget_labels.addItems(labels_to_load)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
