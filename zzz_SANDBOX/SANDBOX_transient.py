# REWRITE THIS SHIT, DONT PUT CHATGPT CODE INTO THE CODEBASE

from PyQt5.QtWidgets import QApplication, QSpinBox, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class DependentSpinBoxes(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize three spin boxes
        self.spin_box1 = QSpinBox()
        self.spin_box2 = QSpinBox()
        self.spin_box3 = QSpinBox()

        # Set ranges for each spin box
        self.spin_box1.setRange(0, 100)
        self.spin_box2.setRange(0, 100)
        self.spin_box3.setRange(0, 100)

        # Set initial values
        self.spin_box1.setValue(100)
        self.spin_box2.setValue(0)
        self.spin_box3.setValue(0)

        # Track the last edited spinbox
        self.last_edited_spinbox = None

        # Connect signals to handle value changes
        self.spin_box1.valueChanged.connect(self.on_spin_box1_changed)
        self.spin_box2.valueChanged.connect(self.on_spin_box2_changed)
        self.spin_box3.valueChanged.connect(self.on_spin_box3_changed)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.spin_box1)
        layout.addWidget(self.spin_box2)
        layout.addWidget(self.spin_box3)

        self.setLayout(layout)
        self.setWindowTitle("Dependent Spin Boxes")

    def on_spin_box1_changed(self, value):
        # When spin_box1 changes, adjust spin_box2 and spin_box3
        remaining = 100 - value
        self.last_edited_spinbox = self.spin_box1

        self.spin_box2.blockSignals(True)
        self.spin_box3.blockSignals(True)

        self.spin_box2.setValue(remaining)
        self.spin_box3.setValue(0)

        self.spin_box2.blockSignals(False)
        self.spin_box3.blockSignals(False)

        self.check_total()

    def on_spin_box2_changed(self, value):
        # When spin_box2 changes, adjust spin_box3 based on the sum of spin_box1 and spin_box2
        total = self.spin_box1.value() + value
        remaining = max(0, 100 - total)
        self.last_edited_spinbox = self.spin_box2

        self.spin_box3.blockSignals(True)
        self.spin_box3.setValue(remaining)
        self.spin_box3.blockSignals(False)

        self.check_total()

    def on_spin_box3_changed(self, value):
        # When spin_box3 changes, ensure the total doesn't go above 100
        total = self.spin_box1.value() + self.spin_box2.value() + value
        self.last_edited_spinbox = self.spin_box3

        if total > 100:
            remaining = max(0, 100 - self.spin_box1.value() - self.spin_box2.value())
            self.spin_box3.blockSignals(True)
            self.spin_box3.setValue(remaining)
            self.spin_box3.blockSignals(False)

        self.check_total()

    def check_total(self):
        """Check if the total of the spinboxes is above 100 and set the border color."""
        total = self.spin_box1.value() + self.spin_box2.value() + self.spin_box3.value()

        if total > 100:
            # Set red border for the last edited spinbox
            self.last_edited_spinbox.setStyleSheet("border: 2px solid red;")
        else:
            # Reset the border for all spinboxes
            self.spin_box1.setStyleSheet("")
            self.spin_box2.setStyleSheet("")
            self.spin_box3.setStyleSheet("")

if __name__ == "__main__":
    app = QApplication([])
    window = DependentSpinBoxes()
    window.show()
    app.exec_()