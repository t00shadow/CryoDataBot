from PyQt5 import QtWidgets as qtw, QtCore as qtc, QtGui as qtg

class TreeWidgetManager:
    def __init__(self, tree_widget, add_label_button=None, status_bar=None):
        """
        Initialize the TreeWidgetManager.
        :param tree_widget: The QTreeWidget to manage.
        :param add_label_button: Optional QPushButton to enable/disable for label addition.
        :param status_bar: Optional QStatusBar to show status messages.
        """
        self.tree_widget = tree_widget
        self.add_label_button = add_label_button
        self.status_bar = status_bar
        self.labels = []  # Example list to hold label data

    def add_group(self):
        """Add a new group to the tree widget (top-level item, editable)."""
        group_name = f"Group {self.tree_widget.topLevelItemCount() + 1}"
        group_item = qtw.QTreeWidgetItem([group_name, "", ""])
        group_item.setFlags(group_item.flags() | qtc.Qt.ItemIsEditable)
        self.tree_widget.addTopLevelItem(group_item)
        self.tree_widget.setCurrentItem(group_item)

    def add_group_with_delete_button(self, icon_path):
        """Add a new group with a delete button to the tree widget."""
        group_name = f"Group {self.tree_widget.topLevelItemCount() + 1}"
        group_item = qtw.QTreeWidgetItem([group_name, "", ""])
        group_item.setFlags(group_item.flags() | qtc.Qt.ItemIsEditable)
        self.tree_widget.addTopLevelItem(group_item)
        self.tree_widget.setCurrentItem(group_item)

        delete_button = qtw.QPushButton()
        delete_button.setIcon(qtg.QIcon(icon_path))
        delete_button.setFixedSize(16, 16)
        delete_button.setStyleSheet("background: transparent; border-radius: 8px;")
        delete_button.clicked.connect(lambda: self.delete_group(group_item))
        self.tree_widget.setItemWidget(group_item, 4, delete_button)

        if self.add_label_button:
            self.add_label_button.setEnabled(True)

    def add_label(self):
        """Add a label (subitem, editable) to the selected group or the parent group of the selected label."""
        selected_item = self.tree_widget.currentItem()
        if not selected_item:
            if self.status_bar:
                self.status_bar.showMessage("Create a group first", 250)
            return

        group_item = selected_item.parent() if selected_item.parent() else selected_item
        label_name = f"Label {group_item.childCount() + 1}"
        label_item = qtw.QTreeWidgetItem([label_name, "", ""])
        label_item.setFlags(label_item.flags() | qtc.Qt.ItemIsEditable)
        group_item.addChild(label_item)
        group_item.setExpanded(True)
        self.tree_widget.setCurrentItem(label_item)

    def delete_label(self):
        """Delete the currently selected label."""
        selected_item = self.tree_widget.currentItem()
        if selected_item and selected_item.parent():
            selected_item.parent().removeChild(selected_item)

    def delete_group(self, group_item):
        """Delete the specified group."""
        index = self.tree_widget.indexOfTopLevelItem(group_item)
        self.tree_widget.takeTopLevelItem(index)
        if self.tree_widget.topLevelItemCount() == 0 and self.add_label_button:
            self.add_label_button.setDisabled(True)
