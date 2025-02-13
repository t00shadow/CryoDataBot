import sys
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget

class OutputRedirector(QObject):
    output_signal = pyqtSignal(str)

    def write(self, message):
        self.output_signal.emit(message)

class Worker(QThread):
    result_signal = pyqtSignal(str)  # Signal to emit the result
    output_signal = pyqtSignal(str)  # Signal to emit the print output

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        result = self.func(*self.args, **self.kwargs)
        self.result_signal.emit(result)  # Emit the result value
        self.output_signal.emit(f"Download finished. File saved at: {result}")  # Emit result in output stream

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit(self)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.button = QPushButton('Start Download', self)
        self.button.clicked.connect(self.start_download)

        # Redirect stdout
        self.redirector = OutputRedirector()
        self.redirector.output_signal.connect(self.text_edit.append)
        sys.stdout = self.redirector

        self.downloaded_file_path = None  # Variable to store the final path

        self.button2 = QPushButton('Abort', self)
        self.button2.clicked.connect(self.abort)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.button2)
        layout.addWidget(self.text_edit)
        self.centralWidget.setLayout(layout)


    def start_download(self):
        def download_file():
            # Simulate download progress and final path
            for i in range(20):
                print(f"Downloading... {i*5}%")
                QThread.sleep(1)
            return "/path/to/downloaded/file"

        self.worker = Worker(download_file)
        # self.worker.output_signal.connect(self.text_edit.append)  # Connect the output signal to text_edit
        self.worker.result_signal.connect(self.handle_result)  # Connect the result signal to handle_result
        self.worker.start()

    def handle_result(self, result):
        # Store the result (downloaded file path)
        self.downloaded_file_path = result
        print(f"Download finished. File saved at: {self.downloaded_file_path}")
    
    def abort(self) -> None:
        self.worker.terminate()
        print("aborted")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
