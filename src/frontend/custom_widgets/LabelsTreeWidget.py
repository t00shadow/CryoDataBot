# booty gpt code, but good enough to prove can work.
# The key is to just make custom widgets like the token tagging input box, and then insert them under a QTreeWidgetItem that's set as its parent.

import sys
from PyQt5.QtWidgets import (
    QApplication, QTreeWidget, QTreeWidgetItem, QWidget, QHBoxLayout,
    QLabel, QComboBox, QLineEdit, QCompleter, QVBoxLayout, QToolButton
)
from PyQt5.QtCore import QStringListModel, QEvent
from PyQt5.QtGui import QIcon

from LabelComboBox import LabelComboBox


class LabelComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.NoInsert)
        self.completer().setCompletionMode(QCompleter.PopupCompletion)
        
        # Install event filter to handle mouse clicks
        self.lineEdit().installEventFilter(self)
        self.view().installEventFilter(self)

        # Placeholder text styling
        self.lineEdit().setPlaceholderText("Select an option")
        self.setStyleSheet("color: teal;")
        self.lineEdit().setStyleSheet("color: brown;")
        self.lineEdit().setClearButtonEnabled(True)
        self.lineEdit().findChild(QToolButton).setIcon(QIcon(r"GUI_custom_widgets/svgs/clear_small-svgrepo-com.svg"))

        self.popup_visible = False


    def eventFilter(self, source, event):
        if source == self.lineEdit() and event.type() == QEvent.MouseButtonPress:
            # assert(self.lineEdit().text() == '')
            # if self.popup_visible:
            #     self.hidePopup()
            #     self.popup_visible = False
            #     print("internal variable still false")
            # elif not self.popup_visible:
            #     self.showPopup()
            #     self.popup_visible = True

            self.hidePopup()     # always disable QComboBox's popup. instead use the completer's popup.
            if not self.completer().popup().isVisible():
                self.completer().complete()  # Show the popup
            elif self.completer().popup().isVisible():
                self.completer().popup().hide()  # Hide the popup
            print(f"before click, popup_visible={self.view().isVisible()}\n")

        if source == self.view() and event.type() == QEvent.FocusOut:     # this is only if using QCombobox's popup instead of QCompleter's popup
            print("QComboBox popup lost focus")
        return super().eventFilter(source, event)


class LabelWidget(QWidget):
    def __init__(self, parent=None):
        super(LabelWidget, self).__init__(parent)

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
        self.setHeaderLabels(["", "Secondary Structure", "Residues", "Atoms"])
        
        # Add a top-level item
        top_item = QTreeWidgetItem(self, ["Item 1"])
        self.addTopLevelItem(top_item)

        # Add the custom row as a child item widget
        self.add_custom_row(top_item)
        top_item.setExpanded(True)
        
        # Add another top-level item
        top_item2 = QTreeWidgetItem(self, ["Item 2"])
        self.addTopLevelItem(top_item2)
        top_item2.setExpanded(True)
        
        # Add another custom row as a child item widget
        child_item = QTreeWidgetItem(top_item2)
        top_item2.addChild(child_item)
        custom_combo = LabelComboBox()
        custom_combo.addItems(['', 'dig', 'bar'])
        self.setItemWidget(child_item, 1, custom_combo)
        custom_combo2 = LabelComboBox()
        custom_combo2.addItems(['', 'yuno', 'miles'])
        self.setItemWidget(child_item, 2, custom_combo2)
        custom_combo3 = tokenLineEdit.TagTextEdit()
        custom_combo3.installEventFilter(self)
        self.setItemWidget(child_item, 3, custom_combo3)
        # self.add_custom_row(top_item2)

    def eventFilter(self, source, event):
        if source == tokenLineEdit.TagTextEdit() and event.type() == QEvent.MouseButtonPress:
            print("asdfasf")
            # assert(self.lineEdit().text() == '')
            # self.showPopup()
            # print(f"before click, popup_visible={self.completer().popup().isVisible():}\n")
            # if not self.completer().popup().isVisible():
            #     self.completer().complete()  # Show the popup
            # elif self.completer().popup().isVisible():
            #     self.completer().popup().hide()  # Hide the popup
            # print(f"before click, popup_visible={self.view().isVisible()}\n")
        return super().eventFilter(source, event)

    def add_custom_row(self, parent_item):
        # Create the custom widget
        custom_row = LabelWidget(self)

        # Add a child item
        child_item = QTreeWidgetItem(parent_item)
        parent_item.addChild(child_item)

        # Set the custom widget as the widget for the second column
        self.setItemWidget(child_item, 1, custom_row)

if __name__ == "__main__":
    import z_Tag_main_alt_allcode_v2 as tokenLineEdit
    app = QApplication(sys.argv)

    # Create the tree widget
    tree_widget = TreeWidgetWithCustomRow()
    tree_widget.setWindowTitle("QTreeWidget with Custom Subitem Row")
    tree_widget.resize(400, 300)
    
    tree_widget.show()
    sys.exit(app.exec_())
