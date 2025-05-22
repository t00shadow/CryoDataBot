import sys
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QProgressBar, QPushButton
import time
from tqdm import tqdm

class Worker(QThread):
    result_signal = pyqtSignal(str)  # Signal to emit the result
    output_signal = pyqtSignal(str)  # Signal to emit the print output
    progress_signal = pyqtSignal(int)  # Signal to update progress bar

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        for progress in self.func(*self.args, **self.kwargs):
            result = self.progress_signal.emit(progress)
        self.result_signal.emit(result)  # Emit the result value
        self.output_signal.emit(f"Download finished. File saved at: {result}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(20, 50, 300, 30)

        self.button = QPushButton('Start Task', self)
        self.button.clicked.connect(self.start_task)

        self.worker = None

    def start_task(self):
        def long_task():
            total = 100
            for i in tqdm(range(total)):
                time.sleep(0.05)  # Simulating work
                yield int((i + 1) * 100 / total)
            return "junk"

        self.worker = Worker(long_task)
        # self.worker.progress_signal.connect(self.update_progress)
        self.worker.progress_signal.connect(self.progress_bar.setValue)
        self.worker.result_signal.connect(self.handle_result)  # Connect the result signal to handle_result
        self.worker.start()

    # def update_progress(self, progress):
    #     self.progress_bar.setValue(progress)

    def handle_result(self, result):
        # Store the result (downloaded file path)
        self.downloaded_file_path = result
        print(f"Download finished. File saved at: {self.downloaded_file_path}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
