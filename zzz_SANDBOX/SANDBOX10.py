from PyQt5.QtWidgets import QApplication, QTextBrowser, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class NoScrollTextBrowser(QTextBrowser):
    def __init__(self):
        super().__init__()
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Disable vertical scrollbar
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Disable horizontal scrollbar
        # self.document().contentsChanged.connect(self.adjust_size_to_content)  # Adjust size when content changes
    
    def adjust_size_to_content(self):
        # Resize the QTextBrowser based on content size
        self.setFixedHeight(int(self.document().size().height()) + int(self.frameWidth()) * 2)  # Adjust height to content
        self.setFixedWidth(int(self.document().size().width()) + int(self.frameWidth()) * 2)   # Adjust width to content if needed

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.text_browser = NoScrollTextBrowser()
        self.text_browser.setText("This is a long text. It should dynamically resize the QTextBrowser so no scrollbars are shown. DOESNT work btw. commented out the dynamic resizing line")
        
        layout.addWidget(self.text_browser)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()