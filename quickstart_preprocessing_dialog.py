from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from quickstart_preprocessing_dialog_ui import Ui_Dialog   # Auto-generated class from .ui file

class Quickstart_Preprocessing_Dialog(QDialog):
    preprocessing_options = pyqtSignal(dict)

    def __init__(self, parent=None, qscore=0, mmf=0, similarity=100):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Data persistence
        self.ui.qScoreDoubleSpinBox_2.setValue(qscore),
        self.ui.mapModelFitnessSpinBox_2.setValue(mmf),
        self.ui.similaritySpinBox_2.setValue(similarity)

        # Connect button signal to function
        self.ui.buttonBox.accepted.connect(self.on_submit)

    def on_submit(self):
        data = {
            "qscore": self.ui.qScoreDoubleSpinBox_2.value(),
            "mmf": self.ui.mapModelFitnessSpinBox_2.value(),
            "similarity": self.ui.similaritySpinBox_2.value()
        }
        self.preprocessing_options.emit(data)