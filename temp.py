from pathlib import Path
import os

print(Path(r'C:\Users\noelu/CryoDataBot\temp.py'))

print(Path.cwd())
print(type(Path.cwd()))
print(str(Path.cwd()))
print(type(str(Path.cwd())))
print(os.getcwd())
print(type(os.getcwd()))


assert(False)

from pathlib import Path
# my_directory = "zzzzz_TEST/parent/parent/directory"
# Path(my_directory).mkdir(parents=True, exist_ok=True)

# path = Path(r'C:\Users\noelu\CryoDataBot\temp.py')
path = Path(r'C:\Users\noelu/CryoDataBot\temp.py')
path = str(path)
print(path)
print(type(path))


from PyInstaller.utils.hooks import collect_submodules
...
hiddenimports = collect_submodules('cupy_backends.cuda')  # collect submodules only for CUDA backend
# hiddenimports += collect_submodules('cupy_backends.cuda')  # collect submodules only for CUDA backend
#hiddenimports += collect_submodules('cupy_backends')  # collect submodules for all backends
print(hiddenimports)

assert(False)

import csv

# def has_data_rows(csv_file):
#     with open(csv_file, newline='', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         rows = list(reader)  # Read all rows into a list
#         return len(rows) > 1  # True if there is more than just the header

def has_data_rows(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        _ = next(reader, None)  # Read the header row
        return next(reader, None) is not None  # Try to read one more row

# Example usage
# csv_file = "JUNKSTUFF/CryoDataBot/download_file_034/download_file_034.csv"
csv_file = "JUNKSTUFF/CryoDataBot/download_file_041/download_file_041.csv"
if not has_data_rows(csv_file):
    print("Invalid CSV: No data rows found.")
else:
    print("Valid CSV: Contains at least one data row.")



import keyword
print(keyword.iskeyword('for'))
print(keyword.iskeyword('file_utils'))



from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

app = QApplication([])

tree = QTreeWidget()
tree.setColumnCount(4)  # 4 columns in total
tree.setHeaderLabels(["Label", "Column 1", "Column 2", "Column 3"])

item1 = QTreeWidgetItem(tree, ["Item 1"])  # Only first column
item2 = QTreeWidgetItem(tree, ["Item 2", "Data 1", "Data 2"])  # Partial fill
item3 = QTreeWidgetItem(tree, ["Item 3", "Data 1", "Data 2", "Data 3"])  # Full row

tree.show()
app.exec_()
