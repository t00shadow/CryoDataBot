# This approach is bad. Not recommended to subclass QThread and implement your own run funcion. 
# Instead, use the worker object (subclass QObject) with moveToThread() approach.

import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QTextEdit, QWidget

# Backend Thread, custom implementation of QThread
class BackendThread(QThread):
    log_signal = pyqtSignal(str)

    def run(self):
        # Simulate a backend process
        for i in range(5):
            time.sleep(1)  # Simulating work
            self.log_signal.emit(f"Processing step {i + 1} completed.")
        self.log_signal.emit("Backend process finished.")
        # super().exec()   # no event loop run unless you call exec, but this was qt4.8 docs
        # super().run()    # someone said qthread's run calls exec by default

# Main GUI
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        # create the backend thread (instance of our custom BackendThread class), it's really that easy
        self.backend_thread = BackendThread()
        self.backend_thread.log_signal.connect(self.log_message)

    def init_ui(self):
        self.setWindowTitle("PyQt5 GUI with Backend Thread (retyped manually)")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout(self)

        self.log_box = QTextEdit(self)
        self.log_box.setReadOnly(True)
        self.layout.addWidget(self.log_box)

        self.start_button = QPushButton("Start Backend Process", self)
        self.start_button.clicked.connect(self.start_backend_process)
        self.layout.addWidget(self.start_button)

        self.dummy_2nd_button = QPushButton("Dummy 2nd Button", self)
        self.dummy_2nd_button.clicked.connect(self.dummy_2nd_btn_fxn)
        self.layout.addWidget(self.dummy_2nd_button)

    def log_message(self, message):
        self.log_box.append(message)

    def start_backend_process(self):
        # does nothing if the this backend process is already currently running
        if not self.backend_thread.isRunning():
            # self.log_box.append("Starting backend process...")
            self.log_message("Starting backend process...")
            self.backend_thread.start()

    def dummy_2nd_btn_fxn(self):
        # self.log_box.append("open na noor")
        self.log_message("open na noor")

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())