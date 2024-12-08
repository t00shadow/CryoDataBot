import sys
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QTextEdit, QWidget


# Worker Class
class Worker(QObject):
    log_signal = pyqtSignal(str)
    finished_signal = pyqtSignal()
    aborted_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._abort = False

    def do_work(self):
        self._abort = False
        for i in range(5):
            if self._abort:
                self.log_signal.emit("Worker aborted.")
                self.aborted_signal.emit()
                return
            time.sleep(1)  # Simulating work
            self.log_signal.emit(f"Worker step {i + 1} completed.")
        self.log_signal.emit("Worker finished.")
        self.finished_signal.emit()

    def abort(self):
        self._abort = True


# Main GUI
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.worker_thread = None
        self.worker = None

    def init_ui(self):
        self.setWindowTitle("QObject Worker with QThread")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout(self)

        self.log_box = QTextEdit(self)
        self.log_box.setReadOnly(True)
        layout.addWidget(self.log_box)

        self.start_button = QPushButton("Start Worker", self)
        self.start_button.clicked.connect(self.start_worker)
        layout.addWidget(self.start_button)

        self.abort_button = QPushButton("Abort Worker", self)
        self.abort_button.clicked.connect(self.abort_worker)
        layout.addWidget(self.abort_button)

    def log_message(self, message):
        self.log_box.append(message)

    def start_worker(self):
        if self.worker_thread and self.worker_thread.isRunning():
            self.log_message("Worker is already running.")
            return

        self.worker_thread = QThread()
        self.worker = Worker()

        # Connect signals
        self.worker.log_signal.connect(self.log_message)
        self.worker.finished_signal.connect(self.worker_thread.quit)
        self.worker.aborted_signal.connect(self.worker_thread.quit)
        self.worker_thread.finished.connect(self.cleanup_worker)

        # Move the worker to the thread and start the thread
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.do_work)
        self.worker_thread.start()

    def abort_worker(self):
        if self.worker:
            self.worker.abort()

    def cleanup_worker(self):
        self.worker_thread.deleteLater()
        self.worker = None
        self.worker_thread = None
        self.log_message("Worker thread cleaned up.")


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
