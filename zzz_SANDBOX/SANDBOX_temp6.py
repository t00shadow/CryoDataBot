from PyQt5.QtWidgets import QApplication, QPushButton, QGraphicsDropShadowEffect, QVBoxLayout, QWidget, QMenu
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

app = QApplication([])

# Create the main window
main_window = QWidget()
main_layout = QVBoxLayout(main_window)

# Create the gradient background widget
gradient_widget = QWidget()
gradient_layout = QVBoxLayout(gradient_widget)
# gradient_widget.setFixedSize(144, 54)  # Slightly larger than button

# Set the gradient background using a stylesheet
gradient_widget.setStyleSheet("""
    background: qlineargradient(spread:pad, x1:0.27, y1:0, x2:0.8, y2:1, stop:0 #AF40FF, stop:0.5 #5B42F3, stop:1 #00DDEB);
    border-radius: 8px;
""")
gradient_widget.setContentsMargins(0, 0, 0, 0)

# Create the button
button = QPushButton("Button 64")
# button.setFixedSize(140, 50)  # Set fixed size
button.setCursor(Qt.PointingHandCursor)  # Set cursor to pointer when hovered

# Apply the button's style using a stylesheet
button.setStyleSheet("""
    QPushButton {
        background-color: black;
        border: 0;
        border-radius: 8px;
        color: #FFFFFF;
        font-family: sans-serif;
        font-size: 20px;
        padding: 16px 24px;
        min-width: 140px;
        white-space: nowrap;
        text-align: center;
    }
    QPushButton:hover {
        background-color: transparent;
    }
    QPushButton:pressed {
        outline: none;
    }
""")

# Create the shadow effect for the button
shadow = QGraphicsDropShadowEffect()
shadow.setBlurRadius(30)  # Set blur radius for shadow
shadow.setOffset(0, 15)  # Set shadow offset
shadow.setColor(QColor(151, 65, 252, 50))  # Set shadow color with transparency (50 = 20%)

# Apply the shadow effect to the button
button.setGraphicsEffect(shadow)

# menu for button
menu = QMenu()
menu.addAction("First Item")
menu.addAction("Second Item")
menu.addAction("Third Item")

button.setMenu(menu)

# Add the gradient widget and the button to the layout
gradient_layout.addWidget(button)
main_layout.addWidget(gradient_widget)

# Set a margin around the layout to ensure the shadow is fully visible
main_layout.setContentsMargins(20, 20, 20, 20)

# Show the main window
main_window.show()

app.exec_()
