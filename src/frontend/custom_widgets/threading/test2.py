import sys
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton

class Worker(QObject):
    output_signal = pyqtSignal(str)    # useless right now, just delete it

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.func(*self.args, **self.kwargs)


class OutputRedirector(QObject):
    output_signal = pyqtSignal(str)

    def write(self, message):
        self.output_signal.emit(message)

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
        def print_numbers():
            for i in range(10):
                print(f"Number: {i}")
                QThread.sleep(1)

        def print_numbers2(start, end):
            for i in range(start, end):
                print(f"Number: {i}")
                QThread.sleep(1)

        self.thread = QThread()
        # self.worker = Worker(print_numbers)
        self.worker = Worker(print_numbers2, 3, 7)
        self.worker.moveToThread(self.thread)

        self.worker.output_signal.connect(self.text_edit.append)
        self.thread.started.connect(self.worker.run)
        self.thread.start()
    
    def closeEvent(self, event):
        # Restore the original stdout when the app is closed
        sys.stdout = sys.__stdout__   # Restore stdout
        event.accept()   # Accept the event to close the window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
