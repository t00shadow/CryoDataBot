# KEEP ME
# very very close. mouse click event is not smooth enough
#   > build this up myself using this stack overflow post (so can remove unncessary/buggy shit): https://stackoverflow.com/a/61510686
# consider ignoring double click mouse event. One on hand its a nice unintentional feature since can double click to hightlgt text for easier deletion. A clear button would also cover this. On the other hand it "feels" less responsive cuz fast clicks count as double clicks which get handled as highlight text

from PyQt5 import QtWidgets, QtCore
from itertools import product

class ToggleableComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEditable(True)
        self.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        
        # Install event filter to handle mouse clicks
        self.lineEdit().installEventFilter(self)
        self.popup_visible = False

        # Placeholder text styling
        self.lineEdit().setPlaceholderText("Select an option")
        self.lineEdit().setStyleSheet("color: gray;")

    def eventFilter(self, obj, event):
        if obj == self.lineEdit() and event.type() == QtCore.QEvent.MouseButtonPress:
            print(f"Event Filter: Before toggle - popup_visible={self.popup_visible}")
            self.togglePopup()    # MOVE HERE
            print(f"Event Filter: After toggle - popup_visible={self.popup_visible}")
            return True
        return super().eventFilter(obj, event)

    # Can move this whole function into the eventFilter fxn (at the location MOVE HERE)
    def togglePopup(self):    
        if self.popup_visible:
            self.hidePopup()
        else:
            self.showPopup()
        # Toggle the visibility state after showing/hiding
        self.popup_visible = not self.popup_visible

    def showPopup(self):
        if not self.completer().popup().isVisible():
            self.completer().complete()  # Show the popup

    def hidePopup(self):
        if self.completer().popup().isVisible():
            self.completer().popup().hide()  # Hide the popup

# Test application
if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    wordlist = [''.join(combo) for combo in product('abc', repeat=4)]

    table = QtWidgets.QTableWidget(1, 4)
    table.setHorizontalHeaderLabels(["ComboBox 1", "ComboBox 2", "ComboBox 3", "LineEdit"])

    for i in range(3):
        combo = ToggleableComboBox()
        combo.addItem(None)
        combo.addItems(wordlist)
        table.setCellWidget(0, i, combo)

    line_edit = QtWidgets.QLineEdit()
    table.setCellWidget(0, 3, line_edit)

    window = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(table)
    window.setLayout(layout)
    window.setWindowTitle('Toggleable ComboBox Example')
    window.resize(800, 200)
    window.show()

    app.exec()