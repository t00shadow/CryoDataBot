import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Test(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        wordList = ['C', 'P', 'N', 'H']
        layout = QtWidgets.QVBoxLayout(self)
        self.line = CustomLineEdit(wordList, self)
        layout.addWidget(self.line)

class CustomLineEdit(QtWidgets.QLineEdit):
    def __init__(self, wordList, parent=None):
        super().__init__(parent)

        model = QtGui.QStandardItemModel()
        for word in wordList:
            item = QtGui.QStandardItem(word)
            model.appendRow(item)
        
        self.complete = CustomCompleter(self)
        self.complete.setModel(model)
        self.complete.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.complete.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.complete.setWrapAround(False)

        self.setCompleter(self.complete)
        self.installEventFilter(self)
    
    def eventFilter(self, source, event):
        if source == self and self.text() == '' and event.type() == QtCore.QEvent.MouseButtonPress:
            print("caught")
            self.completer().complete()
        return super().eventFilter(source, event)

class CustomCompleter(QtWidgets.QCompleter):
    def __init__(self, parent=None):
        super().__init__(parent)

    def pathFromIndex(self, index):
        path = super().pathFromIndex(index)

        lst = str(self.widget().text()).split(',')
        if len(lst) > 1:
            path = '%s, %s' % (','.join(lst[:-1]), path)

        return path

    def splitPath(self, path):
        path = str(path.split(',')[-1]).lstrip(' ')
        return [path]

#===============================================================================
# Unit Testing
#===============================================================================
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())