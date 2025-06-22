from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from cryodatabot.src.frontend.ui_files.quickstart_labels_dialog_ui import Ui_Dialog   # Auto-generated class from .ui file

class Quickstart_Labels_Dialog(QDialog):
    labels = pyqtSignal(dict)

    def __init__(self, parent=None, changethisifneeded=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Data persistence
        # self.ui.qScoreDoubleSpinBox_2.setValue(qscore),
        # self.ui.mapModelFitnessSpinBox_2.setValue(mmf),
        # self.ui.similaritySpinBox_2.setValue(similarity)

        # Connect button signal to function
        self.ui.buttonBox.accepted.connect(self.on_submit)

    def on_submit(self):
        data = {
            # "qscore": self.ui.qScoreDoubleSpinBox_2.value(),
            # "mmf": self.ui.mapModelFitnessSpinBox_2.value(),
            # "similarity": self.ui.similaritySpinBox_2.value()
        }
        self.labels.emit(data)