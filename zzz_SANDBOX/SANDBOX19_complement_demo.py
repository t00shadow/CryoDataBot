# TODO: nice did the styling in css. now just use z_Tag_main_alt_allcode_v2.py (rename that shit ew) cuz it already has editing.
# that file is the same as its original version except flipped to vertical layout. and then just style on that thing cuz its nicely made already.
# internally can use the same datastucture to store tokens (if struggling with that). this one is a list (well originally was also a set converted to a list but i disabled that)
# I'm thinking of using a dictionary instead (key:value is keyword_type:user_input. For example: "resolution"::"resolution: 2 to 4").
#   dictionary keys are implictly a set

from PyQt5 import QtWidgets, QtCore
import sys
from functools import partial
import os

class TagBar(QtWidgets.QWidget):
    def __init__(self):
        super(TagBar, self).__init__()
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

        custom_order = ['banana', 'apple', 'cherry']
        self.order_index = {item: index for index, item in enumerate(custom_order)}

    def setup_ui(self):
        self.line_edit.returnPressed.connect(self.create_tags)

    def create_tags(self):
        new_tags = self.line_edit.text().split(', ')
        print(new_tags)
        self.line_edit.setText('')
        self.tags.extend(new_tags)
        print(self.tags)
        self.tags = [x.lower() for x in self.tags]
        print(self.tags)
        self.tags = list(set(self.tags))     # no repeats, disabled to allow repeats
        # self.tags.sort(key=lambda x: x.lower())    # No need to sort tags BUTTT could later sorta based on a custom order of keywords
        self.tags = sorted(self.tags, key=lambda x: self.order_index.get(x, float('inf')))
        self.refresh()

    def refresh(self):
        # loop thru in reverse and detach each widget from parent using setParent(None), effecitvely removes from display
        for i in reversed(range(self.h_layout.count())):
            self.h_layout.itemAt(i).widget().setParent(None)     # check if memory is freed up
        # readd all widgets including unchanged ones
        for tag in self.tags:
            self.add_tag_to_bar(tag)
        self.h_layout.addWidget(self.line_edit)
        self.line_edit.setFocus()

    def print_shit(self, event):
        print(self.objectName)

    def add_tag_to_bar(self, text):
        tag = QtWidgets.QFrame()
        tag.setStyleSheet("""
            border: 2px solid hotpink;
            border-radius: 4px;
            font-size: 8pt;
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
        label.mouseDoubleClickEvent = self.print_shit
        print(label.objectName)
        hbox.addWidget(label)
        x_button = QtWidgets.QPushButton('x')
        x_button.setFixedSize(16, 16)
        x_button.setStyleSheet("QPushButton {\n"
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
        x_button.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        x_button.clicked.connect(partial(self.delete_tag, text))
        hbox.addWidget(x_button)
        tag.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        self.h_layout.addWidget(tag)

    def delete_tag(self, tag_name):
        self.tags.remove(tag_name)
        self.refresh()
        # do i need del or deleteLater() here? wait nvm check refresh, cuz tags is just a list

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Tag Bar Example")
        self.setGeometry(300, 300, 600, 100)

        # Create a central widget and set it for the main window
        central_widget = QtWidgets.QWidget()
        central_widget.setStyleSheet('background: darkgrey')
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QtWidgets.QVBoxLayout(central_widget)

        border = QtWidgets.QWidget()      #fchange to self.border? (can also change style sheets in main)
        border.setStyleSheet('background: white; border-radius: 16px;')
        central_widget.setStyleSheet('background: darkgrey;')
        # Add the TagBar widget to the layout
        self.tag_bar = TagBar()
        border.setLayout(QtWidgets.QVBoxLayout())
        border.layout().addWidget(self.tag_bar)
        layout.addWidget(border)
        self.widgetCount_btn = QtWidgets.QPushButton("widget count")
        layout.addWidget(self.widgetCount_btn)
        # self.widgetCount_btn.clicked.connect(self.print_widgets)
        self.widgetCount_btn.clicked.connect(self.betterCountWidgets)


        self.checkbox = QtWidgets.QCheckBox('Delete')
        self.button = QtWidgets.QPushButton('Open', self)
        self.button.clicked.connect(self.openDialog)
        # layout = QtWidgets.QHBoxLayout(self)     # already have layout
        layout.addWidget(self.checkbox)
        layout.addWidget(self.button)


        # Apply stylesheet for a unified look between QLineEdit and tags
        self.tag_bar.setStyleSheet('background: transparent; border: 0px')


    def print_widgets(self, event):
        # Print all currently existing widgets
        print("Currently existing widgets:")
        count = 0
        for widget in QtWidgets.QApplication.allWidgets():
            count += 1
            print(f"Widget: {widget}, Type: {type(widget)}")
        print(f"widget count: {count}")

    def betterCountWidgets(self):
        objects = self.findChildren(QtCore.QObject)
        print('Objects = %d' % len(objects))

    # by default dialog windows dont delete themselves (have to either set the attribute or manually delete)
    def openDialog(self):
            widget = QtWidgets.QDialog(self)
            if (self.checkbox.isChecked() and
                not widget.testAttribute(QtCore.Qt.WA_DeleteOnClose)):
                widget.setAttribute(QtCore.Qt.WA_DeleteOnClose)
                for child in self.findChildren(QtWidgets.QDialog):
                    if child is not widget:
                        child.deleteLater()
            label = QtWidgets.QLabel(widget)
            button = QtWidgets.QPushButton('Close', widget)
            button.clicked.connect(widget.close)
            layout = QtWidgets.QVBoxLayout(widget)
            layout.addWidget(label)
            layout.addWidget(button)
            objects = self.findChildren(QtCore.QObject)
            label.setText('Objects = %d' % len(objects))
            print(objects)
            widget.show()


if __name__ == '__main__':
    # os.environ["QT_SCALE_FACTOR"] = "1.5"    # temporarily increase size (shit too small on laptop)
    # os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
    qt_app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.setStyleSheet('color:olive')
    qt_app.exec_()
