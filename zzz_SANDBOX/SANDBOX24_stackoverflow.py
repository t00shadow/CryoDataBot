import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Test(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        model = QtGui.QStandardItemModel()
        wordList = ['John Doe', 'Jane Doe', 'Albert Einstein', 'Alfred E Newman']
        
        for word in wordList:
            item = QtGui.QStandardItem(word)
            model.appendRow(item)

        layout = QtWidgets.QVBoxLayout(self)
        self.line = QtWidgets.QLineEdit(self)
        layout.addWidget(self.line)

        complete = CustomCompleter(self)
        complete.setModel(model)
        complete.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        complete.setCompletionMode(QtWidgets.QCompleter.InlineCompletion)
        complete.setWrapAround(False)

        self.line.setCompleter(complete)


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