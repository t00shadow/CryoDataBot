import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLineEdit, QCompleter, QComboBox, QLabel

class CompleterExample(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Create a label to explain what completion mode is being shown
        self.label = QLabel("Completion Mode: PopupCompletion")
        layout.addWidget(self.label)

        # Create a QLineEdit for typing
        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        # Create a QCompleter with a list of suggestions
        word_list = ["apple", "banana", "cherry", "date", "grape", "kiwi", "orange", "watermelon", "blueberry"]
        self.completer = QCompleter(word_list)
        self.line_edit.setCompleter(self.completer)

        # Create a ComboBox to switch between completion modes
        self.combo_box = QComboBox()
        self.combo_box.addItem("PopupCompletion", QCompleter.PopupCompletion)
        self.combo_box.addItem("InlineCompletion", QCompleter.InlineCompletion)
        self.combo_box.addItem("UnfilteredPopupCompletion", QCompleter.UnfilteredPopupCompletion)
        layout.addWidget(self.combo_box)

        # Connect the combo box selection to change completion mode
        self.combo_box.currentIndexChanged.connect(self.change_completion_mode)

        # Set the layout
        self.setLayout(layout)

        self.setWindowTitle("QCompleter Completion Modes Example")
        self.show()

    def change_completion_mode(self, index):
        # Change the completion mode based on user selection
        mode = self.combo_box.currentData()
        self.completer.setCompletionMode(mode)

        # Update the label to show the current completion mode
        if mode == QCompleter.PopupCompletion:
            self.label.setText("Completion Mode: PopupCompletion")
        elif mode == QCompleter.InlineCompletion:
            self.label.setText("Completion Mode: InlineCompletion")
        elif mode == QCompleter.UnfilteredPopupCompletion:
            self.label.setText("Completion Mode: UnfilteredPopupCompletion")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CompleterExample()
    sys.exit(app.exec_())