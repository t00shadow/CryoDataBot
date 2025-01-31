# TODO: rename this file to distinguish it from the z_... files. Maybe g_ as prefix? g_TagTextEdit.py or just TagTextEdit.py
# last TODO: duplicate this file and remove the mainwindow class at the bottom


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QLabel, QHBoxLayout, \
    QPushButton, QLineEdit, QScrollArea, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt, pyqtSignal

# should prob be called a token oops TODO: rename tag to token everywhere (ugh)
class TagLabel(QWidget):
    # cant access these signals in main, move or connect to other class
    tagDeleted = pyqtSignal(str)
    tagEdited = pyqtSignal(str, str)

    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.text = text
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(5)

        self.label = QLabel(self.text)
        # self.label.setStyleSheet("background-color: lightgray; padding: 5px; border-radius: 3px;")
        # TODO: to get a single border around x button and label, just put a widget underneath both
        self.label.setStyleSheet("""
            background-color: lightgray; 
            padding: 5px;
            border: 2px solid hotpink;
            border-radius: 6px;
            font-size: 8pt;
        """)
        self.label.mouseDoubleClickEvent = self.editTag

        self.clearButton = QPushButton('x')
        self.clearButton.setFixedSize(16, 16)
        # self.clearButton.setStyleSheet("QPushButton { border: none; }")
        self.clearButton.setStyleSheet("QPushButton {\n"
        "    background-color: #f9ecdf;\n"
        "    border: 2px solid grey;\n"
        "    border-radius: 5px;\n"
        "    color: black;\n"
        "    font-size: 8pt;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: #ddd1c6;\n"
        "    border-color: darkgrey;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color: #bfb5ab;\n"
        "    border-color: darkgrey;\n"
        "}\n"
        "")
        self.clearButton.clicked.connect(self.deleteTag)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.clearButton)

        self.setLayout(self.layout)

    def deleteTag(self):
        self.tagDeleted.emit(self.text)
        self.deleteLater()

    def editTag(self, event):
        self.editField = QLineEdit(self.text, self)
        self.editField.setStyleSheet("background-color: white; padding: 5px; border-radius: 3px;")
        self.editField.setFixedWidth(self.width())
        self.editField.setSizePolicy(self.sizePolicy())
        self.editField.returnPressed.connect(self.finishEditing)
        self.layout.replaceWidget(self.label, self.editField)
        self.label.hide()
        self.editField.setFocus()

    def finishEditing(self):
        newText = self.editField.text()
        self.tagEdited.emit(self.text, newText)
        self.text = newText
        self.label.setText(self.text)
        self.layout.replaceWidget(self.editField, self.label)
        self.editField.deleteLater()
        self.label.show()

class TagTextEdit(QTextEdit):
    tagTextEdited = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        TESTFEATURE = "v1"  # kinda useless cuz changed to horizontal, but v1 actually works nicely

        self.setReadOnly(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setStyleSheet("QTextEdit { background-color: white; border: 1px solid gray; }")

        self.container = QWidget()
        self.containerLayout = QHBoxLayout(self.container)
        self.containerLayout.setContentsMargins(2, 2, 2, 2)
        self.containerLayout.setSpacing(5)
        if TESTFEATURE == "v1":
            self.containerLayout.setAlignment(Qt.AlignTop)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.container)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(QPushButton("ignore this"))
        self.layout().addWidget(self.scrollArea)

        self.textInput = QLineEdit()
        self.textInput.setFixedHeight(25)
        self.textInput.installEventFilter(self)

        self.containerLayout.addWidget(self.textInput)
        if TESTFEATURE == 'v2':
            verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
            self.containerLayout.addSpacerItem(verticalSpacer)


        self.junk_val = 5    # only for testing, delete this later
        self.junk_arr = [1, 2, 3, 4]
        self.keywords = []      # considered using set, but i think emdb would let you use the same keyword twice (like resolution 3: AND resolution :6). idk why anyeone would want to do that but ig u can


    def eventFilter(self, source, event):
        if event.type() == event.KeyPress and source is self.textInput:
            if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                text = self.textInput.text().strip()
                if text:
                    self.addTag(text)
                    # self.addTag("AND")
                self.textInput.clear()
                return True
            # TODO: implement a highlight method so have to press backspace twice to delete a tag, might be kinda hard
            if self.textInput.text() == '' and self.containerLayout.count() > 1 and event.key() == Qt.Key_Backspace:    # the lineedit counts as a widget in self.containerLayout too, hence > 1 instead of 0
                text = self.containerLayout.itemAt(self.containerLayout.count() - 2).widget().label.text()
                # print(text)
                self.removeTag(text)
                return True
        return super().eventFilter(source, event)

    def addTag(self, text):
        tag = TagLabel(text, self)
        #print(type(text))
        self.tagTextEdited.emit(text)
        self.keywords.append(text)
        tag.tagDeleted.connect(self.removeTag)
        tag.tagEdited.connect(self.editTag)
        self.containerLayout.insertWidget(self.containerLayout.count() - 1, tag)
        # print(tag)   # debugging backspace functionality
        # print(type(tag))

    def removeTag(self, text):
        for i in range(self.containerLayout.count()):
            item = self.containerLayout.itemAt(i)
            if item and item.widget() and isinstance(item.widget(), TagLabel):
                if item.widget().text == text:
                    # print("here")
                    self.keywords.remove(text)
                    self.containerLayout.takeAt(i).widget().deleteLater()
                    break

    def editTag(self, oldText, newText):
        for i in range(self.containerLayout.count()):
            item = self.containerLayout.itemAt(i)
            if item and item.widget() and isinstance(item.widget(), TagLabel):
                if item.widget().text == oldText:
                    item.widget().text = newText
                    self.tagTextEdited.emit(newText)
                    self.keywords[i] = newText
                    break

    # # ehh prob dont need a getter cuz no ones accessing the variable besides me
    # def getQuery(self):
    #     return self.junk_val

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Tag Editor")
#         self.setGeometry(100, 100, 400, 300)

#         self.tagTextEdit = TagTextEdit()
#         self.setCentralWidget(self.tagTextEdit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # mainWindow = MainWindow()
    mainWindow = TagTextEdit()
    mainWindow.setMinimumWidth(1000)
    mainWindow.show()
    sys.exit(app.exec_())