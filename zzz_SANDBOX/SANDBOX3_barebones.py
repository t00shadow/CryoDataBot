# from https://stackoverflow.com/a/61510686

from PyQt5 import QtWidgets
from itertools import product

app = QtWidgets.QApplication([])

# wordlist for testing
wordlist = [''.join(combo) for combo in product('abc', repeat = 4)]

combo = QtWidgets.QComboBox()
# combo.addItem("")    # kinda hacky solution to start with blank text
combo.addItems(wordlist)

# completers only work for editable combo boxes. QComboBox.NoInsert prevents insertion of the search text
combo.setEditable(True)
combo.setInsertPolicy(QtWidgets.QComboBox.NoInsert)

# change completion mode of the default completer from InlineCompletion to PopupCompletion
combo.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

combo.show()
app.exec()