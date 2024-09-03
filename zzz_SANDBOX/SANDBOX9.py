from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time
import requests
from concurrent.futures import ThreadPoolExecutor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the main window
        self.setWindowTitle("Progress Bar Example")
        
        # Create the progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        
        # Create a start button
        self.start_button = QPushButton("Start Task")
        self.start_button.clicked.connect(self.start_task)

        # Create other butttons
        self.button2 = QPushButton("button 2")
        self.button2.clicked.connect(self.hello_world)
        self.button3 = QPushButton("button 3")
        self.button3.clicked.connect(self.hello_world2)
        
        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.start_button)

        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        
        # Set up the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_task(self):
        # Start the long-running task in a separate thread
        self.thread = WorkerThread()
        self.thread.progress_update.connect(self.update_progress_bar)
        # self.thread.progress_update.connect(self.progress_bar.setValue)   #can just do this too since the int will get passed from signal to slot iirc
        self.thread.start()

    def update_progress_bar(self, value):
        temp = self.progress_bar.value()
        print(temp)
        self.progress_bar.setValue(temp + value)

    def hello_world(self):
        print("hello world")

    def hello_world2(self):
        print("look gui is still interactive during long process")

class WorkerThread(QThread):
    # Define a signal that sends an integer value to update the progress bar
    progress_update = pyqtSignal(int)
    n_tasks = 7

    # def run(self):
    #     # Simulate a long-running task
    #     for i in range(101):
    #         time.sleep(0.1)  # Simulate time-consuming task
    #         self.progress_update.emit(i)  # Emit the progress update signal
    #         #print(i)

    def real_task(self):
        session = requests.Session()
        entry_id = '37271'
        url = f"https://www.ebi.ac.uk/emdb/api/analysis/{entry_id}"
        try:
            file = session.get(url).json()
        except:
            print("empty")
            return '', ''
            
        try:
            qscore = file[entry_id]["qscore"]["allmodels_average_qscore"]
        except Exception:
            qscore = ''
        try:
            atom_inclusion = file[entry_id]["atom_inclusion_by_level"]["average_ai_allmodels"]
        except Exception:
            atom_inclusion = ''

        print("request finished")
        self.progress_update.emit(int(100 / self.n_tasks))
        return qscore, atom_inclusion
    
    def run(self):
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.real_task) for _ in range(self.n_tasks)]
        print("done")
        self.progress_update.emit(100)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
