import sys
from PyQt5.QtWidgets import QComboBox, QCompleter, QToolButton
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QIcon


class LabelComboBox(QComboBox):
    def __init__(self, parent=None, placeholder_text="Select an option"):
        super().__init__(parent)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.NoInsert)
        self.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.completer().popup().setStyleSheet("background-color: blue; color:white")     # looks insanely ugly, just for debugging
        
        # Install event filter to handle mouse clicks
        self.lineEdit().installEventFilter(self)
        self.view().installEventFilter(self)

        # Placeholder text styling
        self.lineEdit().setPlaceholderText(placeholder_text)
        self.setStyleSheet("color: teal;")
        self.lineEdit().setStyleSheet("color: brown;")
        self.lineEdit().setClearButtonEnabled(True)
        self.lineEdit().findChild(QToolButton).setIcon(QIcon(r"GUI_custom_widgets/svgs/clear_small-svgrepo-com.svg"))

        self.popup_visible = False
        self.cooldown = False

        self.version = 3


    def eventFilter(self, source, event):
        if source == self.lineEdit() and event.type() == QEvent.MouseButtonPress:
            if self.version == 1:
                # assert(self.lineEdit().text() == '')
                if self.popup_visible:
                    self.hidePopup()
                    self.popup_visible = False
                    print("internal variable false")
                elif not self.popup_visible:
                    self.showPopup()
                    self.popup_visible = True

            elif self.version == 2:
                # assert(self.lineEdit().text() == '')
                if self.view().isVisible():
                    self.hidePopup()
                elif not self.view().isVisible():
                    self.showPopup()
            
            elif self.version == 3:
                # assert(self.lineEdit().text() == '')
                self.showPopup()

            elif self.version == 4:
                self.hidePopup()     # Always disable QComboBox's popup. Using the completer's popup instead.
                if not self.completer().popup().isVisible():
                    self.completer().complete()  # Show the popup
                elif self.completer().popup().isVisible():
                    self.completer().popup().hide()  # Hide the popup
                print(f"before click, popup_visible={self.view().isVisible()}\n")
                
        if source == self.view() and event.type() == QEvent.FocusOut:     # only relevant for version 1
            print("QComboBox popup lost focus")

        return super().eventFilter(source, event)