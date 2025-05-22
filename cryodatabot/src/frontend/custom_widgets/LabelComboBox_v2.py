from PyQt5.QtWidgets import QComboBox, QLineEdit
from PyQt5.QtCore import QEvent, QCoreApplication, Qt
from PyQt5.QtGui import QKeyEvent, QFocusEvent

class LabelComboBox_v2(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEditable(True)
        self.view().installEventFilter(self)   # Install event filter on the view

        # self.lineEdit().textEdited.connect(self.showPopup)
        self.lineEdit().setPlaceholderText("Select")

    # Event filter forwards view key events to the line edit
    def eventFilter(self, watched, event):
        if event.type() == QEvent.KeyPress:
            keyEvent = event
            # Create a new key event
            newEvent = QKeyEvent(
                keyEvent.type(),
                keyEvent.key(),
                keyEvent.modifiers(),
                keyEvent.text(),
                keyEvent.isAutoRepeat(),
                keyEvent.count()
            )
            # Send focus and key events to the line edit
            focusEvent = QFocusEvent(QEvent.FocusIn, Qt.OtherFocusReason)
            QCoreApplication.postEvent(self.lineEdit(), focusEvent)
            QCoreApplication.postEvent(self.lineEdit(), newEvent)
        return False    # Return false to let the event propagate further