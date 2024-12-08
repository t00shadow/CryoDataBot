import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QPushButton, QTextEdit, QHBoxLayout, QWidget
)


# Backend Thread
class BackendThread(QThread):
    log_signal = pyqtSignal(str)  # Signal to send logs to the GUI
    finished_signal = pyqtSignal()  # Signal when process finishes
    aborted_signal = pyqtSignal()  # Signal if process is aborted

    def __init__(self):
        super().__init__()
        self._abort = False

    def run(self):
        for i in range(5):
            if self._abort:
                self.log_signal.emit("Process aborted.")
                self.aborted_signal.emit()
                return
            time.sleep(1)  # Simulating work
            self.log_signal.emit(f"Processing step {i + 1} completed.")
        self.log_signal.emit("Process finished.")
        self.finished_signal.emit()

    def abort(self):
        self._abort = True


# Main GUI
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.backend_threads = []
        self.queued_threads = []

    def init_ui(self):
        self.setWindowTitle("PyQt5 GUI with Thread Management")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout(self)

        self.log_box = QTextEdit(self)
        self.log_box.setReadOnly(True)
        layout.addWidget(self.log_box)

        self.thread_box = QTextEdit(self)
        self.thread_box.setReadOnly(True)
        layout.addWidget(self.thread_box)

        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Queue Backend Process", self)
        self.start_button.clicked.connect(self.queue_backend_process)
        button_layout.addWidget(self.start_button)

        self.cancel_button = QPushButton("Cancel Queued Process", self)
        self.cancel_button.clicked.connect(self.cancel_queued_process)
        button_layout.addWidget(self.cancel_button)

        self.abort_button = QPushButton("Abort Running Process", self)
        self.abort_button.clicked.connect(self.abort_running_process)
        button_layout.addWidget(self.abort_button)

        layout.addLayout(button_layout)

    def log_message(self, message):
        self.log_box.append(message)

    def update_thread_list(self):
        running_threads = [f"Running: Process {i + 1}" for i, t in enumerate(self.backend_threads) if t.isRunning()]
        queued_threads = [f"Queued: Process {i + 1}" for i in range(len(self.queued_threads))]
        self.thread_box.setPlainText("\n".join(running_threads + queued_threads))

    def queue_backend_process(self):
        thread = BackendThread()
        thread.log_signal.connect(self.log_message)
        thread.finished_signal.connect(lambda: self.backend_threads.remove(thread))
        thread.finished_signal.connect(self.update_thread_list)
        thread.aborted_signal.connect(lambda: self.backend_threads.remove(thread))
        thread.aborted_signal.connect(self.update_thread_list)

        if not any(t.isRunning() for t in self.backend_threads):
            self.backend_threads.append(thread)
            thread.start()
        else:
            self.queued_threads.append(thread)

        self.update_thread_list()

    def cancel_queued_process(self):
        if self.queued_threads:
            thread = self.queued_threads.pop(0)
            self.log_message("Cancelled a queued process.")
            self.update_thread_list()

    def abort_running_process(self):
        running_threads = [t for t in self.backend_threads if t.isRunning()]
        if running_threads:
            running_threads[0].abort()
            self.log_message("Aborting the running process...")
        else:
            self.log_message("No running process to abort.")

    def start_next_in_queue(self):
        if self.queued_threads and not any(t.isRunning() for t in self.backend_threads):
            thread = self.queued_threads.pop(0)
            self.backend_threads.append(thread)
            thread.start()
            self.update_thread_list()


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
