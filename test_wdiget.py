# from PyQt5.QtCore import Qt, QPoint, QRect
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QScrollArea, QLabel, QFrame
# )


# class VerticallyResizableWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setMinimumHeight(100)
#         self.setStyleSheet("background-color: lightyellow;")

#         layout = QVBoxLayout(self)
#         label = QLabel("Drag the bottom edge to resize vertically")
#         layout.addWidget(label)

#         self.resizing = False
#         self.handle_height = 10

#     def mousePressEvent(self, event):
#         if self._on_resize_handle(event.pos()):
#             self.resizing = True
#             self.start_pos = event.globalPos()
#             self.start_height = self.height()

#     def mouseMoveEvent(self, event):
#         if self.resizing:
#             delta_y = event.globalPos().y() - self.start_pos.y()
#             new_height = max(self.minimumHeight(), self.start_height + delta_y)
#             self.resize(self.width(), new_height)

#     def mouseReleaseEvent(self, event):
#         self.resizing = False

#     def _on_resize_handle(self, pos: QPoint) -> bool:
#         """Check if the mouse is on the bottom edge."""
#         return QRect(
#             0,
#             self.height() - self.handle_height,
#             self.width(),
#             self.handle_height
#         ).contains(pos)

#     def paintEvent(self, event):
#         """Optional: paint a visual resize handle."""
#         super().paintEvent(event)
#         painter = QFrame(self)
#         painter.setGeometry(
#             0,
#             self.height() - self.handle_height,
#             self.width(),
#             self.handle_height
#         )
#         painter.setStyleSheet("background-color: gray;")


# class ScrollableWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Vertical Resize Inside ScrollArea")
#         layout = QVBoxLayout(self)

#         scroll = QScrollArea()
#         scroll.setWidgetResizable(False)  # Allow manual resizing

#         self.content = VerticallyResizableWidget()
#         scroll.setWidget(self.content)

#         layout.addWidget(scroll)


# app = QApplication([])
# window = ScrollableWindow()
# window.resize(400, 300)
# window.show()
# app.exec_()





# ================================

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
    QDialog, QLineEdit, QHBoxLayout
)
from PyQt5.QtCore import Qt
import sys

# # Define your custom dialog window
# class CustomDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Popup Dialog")
#         self.setWindowFlags(Qt.Window)  # Makes it act like a regular independent window
#         self.setModal(False)

#         self.setMinimumWidth(300)

#         layout = QVBoxLayout()
#         self.input = QLineEdit(self)
#         self.submit_btn = QPushButton("Submit", self)
#         self.close_btn = QPushButton("Close", self)

#         layout.addWidget(self.input)
#         layout.addWidget(self.submit_btn)
#         layout.addWidget(self.close_btn)

#         self.setLayout(layout)

#         self.close_btn.clicked.connect(self.close)
#         self.submit_btn.clicked.connect(self.handle_submit)

#     def handle_submit(self):
#         print("Input submitted:", self.input.text())

# QDialog with custom UI
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from quickstart_preprocessing_dialog_ui import Ui_Dialog  # Auto-generated class from .ui file

class CustomDialog(QDialog):
    preprocessing_options = pyqtSignal(dict)

    def __init__(self, parent=None, qscore=0, mmf=0, similarity=100):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # # Example: connect buttons
        # self.ui.submit_btn.clicked.connect(self.handle_submit)
        # self.ui.close_btn.clicked.connect(self.close)

        # print(self.ui.buttonBox.buttons())
        # self.ui.buttonBox.accepted.connect(lambda:print("HHHHHDKAHSDK"))     # buttonBox is actually p clean
        self.ui.buttonBox.accepted.connect(self.on_submit)

        self.ui.qScoreDoubleSpinBox_2.setValue(qscore),
        self.ui.mapModelFitnessSpinBox_2.setValue(mmf),
        self.ui.similaritySpinBox_2.setValue(similarity)

    # def handle_submit(self):
    #     print("Input submitted:", self.ui.input_line.text())

    def on_submit(self):
        # self.preprocessing_options.emit({"hot": "dog", "taco": "cat"})      # dummy data
        data = {
            "qscore": self.ui.qScoreDoubleSpinBox_2.value(),
            "mmf": self.ui.mapModelFitnessSpinBox_2.value(),
            "similarity": self.ui.similaritySpinBox_2.value()
        }
        self.preprocessing_options.emit(data)              # could checkif any values changed, but not necessary


# Main window that opens the dialog
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        self.button = QPushButton("Open Popup")
        self.button.clicked.connect(self.open_popup)

        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.quickstart_qscore = 0
        self.quickstart_mmf = 0
        self.quickstart_similarity = 100

        self.popup = None

    # def open_popup(self):
    #     if self.popup is None or not self.popup.isVisible():
    #         self.popup = CustomDialog(self)
    #         self.popup.show()
    #     else:
    #         self.popup.raise_()
    #         self.popup.activateWindow()

    def open_popup(self):
        dialog = CustomDialog(self, qscore=self.quickstart_qscore, mmf=self.quickstart_mmf, similarity=self.quickstart_similarity)
        dialog.preprocessing_options.connect(self.handle_dialog_data)
        dialog.show()
    
    def handle_dialog_data(self, data):
        print(f"Data from dialog:{data}")
        self.quickstart_qscore = data["qscore"]
        self.quickstart_mmf = data["mmf"]
        self.quickstart_similarity = data["similarity"]


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

