# from PyQt5.QtCore import QObject, pyqtSignal

# class Worker(QObject):
#     finished = pyqtSignal()
#     # aborted = pyqtSignal()
#     progress = pyqtSignal(str)

#     def __init__(self, task):
#         super().__init__()
#         # self._abort = False
#         self.task = task
    
#     def run(self):
#         self.progress.emit(f"Starting task: {self.task}")
#         result = self.task()
#         self.progress.emit(f"Task result: {result}")
#         self.finished.emit()


import sys
from PyQt5.QtCore import QObject, pyqtSignal
from io import StringIO

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(str)

    def __init__(self, task, *args, **kwargs):
        super().__init__()
        self.task = task
        self.args = args if args else []
        self.kwargs = kwargs if kwargs else {}

    def run(self):
        # redirect stdout to capture prints
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            self.task(self.progress.emit, *self.args, **self.kwargs)
            # emit captured output
            self.progress.emit(sys.stdout.getvalue())
        finally:
            # restore stdout
            sys.stdout = old_stdout

        self.finished.emit()