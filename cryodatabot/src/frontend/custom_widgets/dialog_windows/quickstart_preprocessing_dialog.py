from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from cryodatabot.src.frontend.ui_files.quickstart_preprocessing_dialog_ui import Ui_Dialog   # Auto-generated class from .ui file

class Quickstart_Preprocessing_Dialog(QDialog):
    preprocessing_options = pyqtSignal(dict)

    def __init__(self, parent=None, current_values: dict = None, default_values: dict = None):
        """
        Initialize the custom dialog.

        Args:
            current_values (dict): The current values to populate the dialog with.
            default_values (dict): Base/default values used for initializing certain fields.
            parent (QWidget, optional): The parent widget of the dialog. Defaults to None.
        """
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Data persistence
        self.ui.qScoreDoubleSpinBox_2.setValue(current_values["qscore"]),
        self.ui.mapModelFitnessSpinBox_2.setValue(current_values["mmf"]),
        self.ui.similaritySpinBox_2.setValue(current_values["similarity"])

        # Connect dialog button signal to function
        self.ui.buttonBox.accepted.connect(self.on_submit)

        # Connect other buttons (nearly identical to main window)
        self.ui.clearQScore_btn_2.clicked.connect(lambda: self.ui.qScoreDoubleSpinBox_2.setValue(default_values["qscore"]))
        self.ui.clearSim_btn_2.clicked.connect(lambda: self.ui.similaritySpinBox_2.setValue(default_values["similarity"]))
        self.ui.clearMMF_btn_2.clicked.connect(lambda: self.ui.mapModelFitnessSpinBox_2.setValue(default_values["mmf"]))

    def on_submit(self):
        data = {
            "qscore": self.ui.qScoreDoubleSpinBox_2.value(),
            "similarity": self.ui.similaritySpinBox_2.value(),
            "mmf": self.ui.mapModelFitnessSpinBox_2.value(),
        }
        self.preprocessing_options.emit(data)