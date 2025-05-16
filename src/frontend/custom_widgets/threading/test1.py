import sys
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton

class OutputRedirector(QObject):
    output_signal = pyqtSignal(str)

    def write(self, message):
        self.output_signal.emit(message)

class Worker(QThread):
    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.func(*self.args, **self.kwargs)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.button = QPushButton('Start Process', self)
        self.button.clicked.connect(self.start_process)

        # Redirect stdout
        self.redirector = OutputRedirector()
        self.redirector.output_signal.connect(self.text_edit.append)
        sys.stdout = self.redirector

    def start_process(self):
        # Pass any function here. Example function that prints numbers
        def print_numbers():
            for i in range(10):
                print(f"Number: {i}")
                QThread.sleep(1)

        self.worker = Worker(print_numbers)
        self.worker.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
