from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QDialog


class EasyCloseDialog(QDialog):
    def __init__(self, parent=None, fxn=None):
        super(EasyCloseDialog, self).__init__(parent)

    def eventFilter(self, watched, event):
        # Check if a mouse button is pressed outside the dialog
        if event.type() == QEvent.MouseButtonPress:
            if not self.rect().contains(self.mapFromGlobal(event.globalPos())):
                self.close()
        return super().eventFilter(watched, event)