import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QSlider

class ScalableForm(QWidget):
    def __init__(self):
        super().__init__()

        self.scale_factor = 1.0  # Initial scaling factor

        self.layout = QVBoxLayout()

        # Create widgets
        self.label = QLabel("Enter your name:")
        self.input_field = QLineEdit()
        self.submit_button = QPushButton("Submit")
        
        # Create a slider for scaling
        self.scale_slider = QSlider()
        self.scale_slider.setRange(10, 300)  # Range for 10% to 300%
        self.scale_slider.setValue(100)  # Start at 100%
        self.scale_slider.valueChanged.connect(self.update_scale)

        # Add widgets to the layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.scale_slider)

        self.setLayout(self.layout)

        # Initial scaling
        self.scale_ui(self.scale_factor)

    def scale_ui(self, factor):
        # Scale font for the label
        font = self.label.font()
        font.setPointSize(int(10 * factor))  # Adjust base font size
        self.label.setFont(font)

        # Scale input field
        input_size = self.input_field.sizeHint()
        self.input_field.setFixedSize(int(input_size.width() * factor), int(input_size.height() * factor))

        # Scale button
        button_size = self.submit_button.sizeHint()
        self.submit_button.setFixedSize(int(button_size.width() * factor), int(button_size.height() * factor))
        self.submit_button.setFont(font)

    def set_scale_factor(self, factor):
        self.scale_factor = factor
        self.scale_ui(self.scale_factor)

    def update_scale(self, value):
        self.set_scale_factor(value / 100.0)  # Convert percentage to scale factor

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScalableForm()
    window.show()
    
    sys.exit(app.exec_())
