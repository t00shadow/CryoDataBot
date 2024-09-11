# This is actually good enough, just use stylesheets to make it look like the tags are in the same box as the lineedit. its actually good to have the lineedit not underneath so the text starts at the right place

from PyQt5 import QtWidgets, QtCore
import sys
from functools import partial

class TagBar(QtWidgets.QWidget):
    def __init__(self):
        super(TagBar, self).__init__()
        self.setWindowTitle('Tag Bar')
        self.tags = []
        self.h_layout = QtWidgets.QHBoxLayout()
        self.h_layout.setSpacing(4)
        self.setLayout(self.h_layout)
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.setContentsMargins(2, 2, 2, 2)
        self.h_layout.setContentsMargins(2, 2, 2, 2)
        self.refresh()
        self.setup_ui()
        self.show()

    def setup_ui(self):
        self.line_edit.returnPressed.connect(self.create_tags)

    def create_tags(self):
        new_tags = self.line_edit.text().split(', ')
        print(new_tags)
        self.line_edit.setText('')
        self.tags.extend(new_tags)
        # self.tags = list(set(self.tags))     # no repeats
        self.tags = list(self.tags)            # yes repeats
        # self.tags.sort(key=lambda x: x.lower())       # dont need to sort tags BUTTTT could sort in a custom order hmmm
        self.refresh()

    def refresh(self):
        for i in reversed(range(self.h_layout.count())):
            self.h_layout.itemAt(i).widget().setParent(None)
        for tag in self.tags:
            self.add_tag_to_bar(tag)
        self.h_layout.addWidget(self.line_edit)
        self.line_edit.setFocus()

    def add_tag_to_bar(self, text):
        tag = QtWidgets.QFrame()
        tag.setStyleSheet("""
            border: 2px solid pink;
            border-radius: 4px;
        """)
        tag.setContentsMargins(2, 2, 2, 2)
        tag.setFixedHeight(28)
        hbox = QtWidgets.QHBoxLayout()
        hbox.setContentsMargins(4, 4, 4, 4)
        hbox.setSpacing(10)
        tag.setLayout(hbox)
        label = QtWidgets.QLabel(text)
        label.setStyleSheet('border:0px')
        label.setFixedHeight(16)
        hbox.addWidget(label)
        x_button = QtWidgets.QPushButton('x')
        x_button.setFixedSize(8, 16)
        x_button.setStyleSheet('border:0px; font-weight:bold')
        x_button.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        x_button.clicked.connect(partial(self.delete_tag, text))
        hbox.addWidget(x_button)
        tag.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        self.h_layout.addWidget(tag)

    def delete_tag(self, tag_name):
        self.tags.remove(tag_name)
        self.refresh()

if __name__ == '__main__':
    qt_app = QtWidgets.QApplication(sys.argv)
    tag_bar = TagBar()
    tag_bar.setStyleSheet('''
        QLineEdit {
            background: transparent;
            border: 0px;
        }
    ''')
    qt_app.exec_()
