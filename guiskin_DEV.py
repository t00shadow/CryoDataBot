# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataset_gen_tool_v5_1_fixedspacing.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 756)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget_2.setStyleSheet("")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setStyleSheet("/*\n"
"background-color: #f9ece1;\n"
"*/")
        self.tab_3.setObjectName("tab_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 521, 691))
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(30, 60, 431, 181))
        self.textBrowser.setStyleSheet("background-color: transparent;\n"
"border: transparent;")
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox1 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox1.setGeometry(QtCore.QRect(20, 260, 481, 401))
        self.groupBox1.setStyleSheet("QGroupBox {\n"
"    border-radius: 20px;\n"
"    background-color: #6668ad;\n"
"}\n"
"\n"
"/*\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"*/")
        self.groupBox1.setTitle("")
        self.groupBox1.setObjectName("groupBox1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setStyleSheet("background-color: transparent;\n"
"border: transparent;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout.addWidget(self.textBrowser_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox1)
        self.textEdit.setStyleSheet("border: transparent;")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_4.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(self.groupBox1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background: #81cfd8;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 6px solid transparent;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #6668ad;\n"
"/*\n"
"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"background-color: white;\n"
"*/\n"
"padding: 10px")
        self.label_5.setObjectName("label_5")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 70, 491, 191))
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    border-radius: 20px;\n"
"    background-color: #81cfd8;\n"
"}\n"
"\n"
"/*\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"*/")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 150, 28, 21))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_3.setStyleSheet("border-image: url(:/icons/browsefilesicon.png);\n"
"background-color: white;\n"
"border-radius: 6;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_2.setGeometry(QtCore.QRect(50, 50, 271, 91))
        self.widget_2.setStyleSheet("border-image: url(:/icons/draganddrop.PNG);")
        self.widget_2.setObjectName("widget_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 1, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(50, 150, 231, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 150, 121, 24))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: #f9ecdf;\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/external-link-512.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 280, 491, 411))
        self.groupBox_3.setStyleSheet("QGroupBox {\n"
"    border-radius: 20px;\n"
"    background-color: #81cfd8;\n"
"}\n"
"\n"
"/*\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"*/")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 328, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background: #6668ad;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 6px solid transparent;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(30, 50, 141, 16))
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 260, 31, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(192, 260, 31, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(128, 261, 16, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 260, 31, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(178, 261, 16, 16))
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(30, 260, 61, 20))
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 290, 131, 24))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: #f9ecdf;\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
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
        icon = QtGui.QIcon.fromTheme("application-exit")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setGeometry(QtCore.QRect(40, 70, 141, 181))
        self.listWidget.setStyleSheet("QListWidget::item {\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #F0F0F0;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #E0E0E0;\n"
"}")
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox_3)
        self.stackedWidget.setGeometry(QtCore.QRect(190, 70, 271, 181))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.scrollArea = QtWidgets.QScrollArea(self.page)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 271, 181))
        self.scrollArea.setStyleSheet("/*scrollArea color*/\n"
"QWidget {\n"
"    background-color: white;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 269, 179))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridFrame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.gridFrame_4.setObjectName("gridFrame_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.gridFrame_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.checkBox_10 = QtWidgets.QCheckBox(self.gridFrame_4)
        self.checkBox_10.setStyleSheet("")
        self.checkBox_10.setObjectName("checkBox_10")
        self.verticalLayout_8.addWidget(self.checkBox_10)
        self.checkBox_11 = QtWidgets.QCheckBox(self.gridFrame_4)
        self.checkBox_11.setObjectName("checkBox_11")
        self.verticalLayout_8.addWidget(self.checkBox_11)
        self.checkBox_12 = QtWidgets.QCheckBox(self.gridFrame_4)
        self.checkBox_12.setObjectName("checkBox_12")
        self.verticalLayout_8.addWidget(self.checkBox_12)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.verticalLayout_7.addWidget(self.gridFrame_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 0, 271, 181))
        self.scrollArea_2.setStyleSheet("/*scrollArea_2 color*/\n"
"QWidget {\n"
"    background-color: white;\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 269, 179))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridFrame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.gridFrame_3.setObjectName("gridFrame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.gridFrame_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.gridFrame_3)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_6.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.gridFrame_3)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_6.addWidget(self.checkBox_8)
        self.checkBox_9 = QtWidgets.QCheckBox(self.gridFrame_3)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout_6.addWidget(self.checkBox_9)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.gridFrame_3)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.page_3)
        self.scrollArea_3.setGeometry(QtCore.QRect(0, 0, 271, 181))
        self.scrollArea_3.setStyleSheet("/*scrollArea_3 color*/\n"
"QWidget {\n"
"    background-color: white;\n"
"}\n"
"\n"
"/*Scroll bar*/\n"
"QScrollBar:vertical {\n"
"    border: 2px solid grey;\n"
"    background: #6668ad;\n"
"    width: 15px;\n"
"    margin: 20px 0 20px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: white;\n"
"    min-height: 20px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 2px solid grey;\n"
"    background: #6668ad;\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 2px solid grey;\n"
"    background: #6668ad;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: 2px solid grey;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: white;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 269, 556))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.gridFrame.setObjectName("gridFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gridFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_13 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_13.setObjectName("checkBox_13")
        self.verticalLayout_2.addWidget(self.checkBox_13)
        self.checkBox_14 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_14.setObjectName("checkBox_14")
        self.verticalLayout_2.addWidget(self.checkBox_14)
        self.checkBox_15 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_15.setObjectName("checkBox_15")
        self.verticalLayout_2.addWidget(self.checkBox_15)
        self.checkBox_16 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_16.setObjectName("checkBox_16")
        self.verticalLayout_2.addWidget(self.checkBox_16)
        self.checkBox_17 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_17.setObjectName("checkBox_17")
        self.verticalLayout_2.addWidget(self.checkBox_17)
        self.checkBox_18 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_18.setObjectName("checkBox_18")
        self.verticalLayout_2.addWidget(self.checkBox_18)
        self.checkBox_19 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_19.setObjectName("checkBox_19")
        self.verticalLayout_2.addWidget(self.checkBox_19)
        self.checkBox_20 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_20.setObjectName("checkBox_20")
        self.verticalLayout_2.addWidget(self.checkBox_20)
        self.checkBox_21 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_21.setObjectName("checkBox_21")
        self.verticalLayout_2.addWidget(self.checkBox_21)
        self.checkBox_22 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_22.setObjectName("checkBox_22")
        self.verticalLayout_2.addWidget(self.checkBox_22)
        self.checkBox_23 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_23.setObjectName("checkBox_23")
        self.verticalLayout_2.addWidget(self.checkBox_23)
        self.checkBox_24 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_24.setObjectName("checkBox_24")
        self.verticalLayout_2.addWidget(self.checkBox_24)
        self.checkBox_25 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_25.setObjectName("checkBox_25")
        self.verticalLayout_2.addWidget(self.checkBox_25)
        self.checkBox_26 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_26.setObjectName("checkBox_26")
        self.verticalLayout_2.addWidget(self.checkBox_26)
        self.checkBox_27 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_27.setObjectName("checkBox_27")
        self.verticalLayout_2.addWidget(self.checkBox_27)
        self.checkBox_28 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_28.setObjectName("checkBox_28")
        self.verticalLayout_2.addWidget(self.checkBox_28)
        self.checkBox_29 = QtWidgets.QCheckBox(self.gridFrame)
        self.checkBox_29.setObjectName("checkBox_29")
        self.verticalLayout_2.addWidget(self.checkBox_29)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.gridFrame)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar.setGeometry(QtCore.QRect(40, 380, 401, 16))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    /*background-color: #CD96CD;*/\n"
"    background-color: #ffdab5;\n"
"    width: 10px;\n"
"    margin: 0.5px;\n"
"}\n"
"")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #81cfd8;\n"
"/*\n"
"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"background-color: white;\n"
"*/\n"
"padding: 10px")
        self.label_7.setObjectName("label_7")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.testPage = QtWidgets.QWidget()
        self.testPage.setObjectName("testPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.testPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.baseLayer = QtWidgets.QGroupBox(self.testPage)
        self.baseLayer.setStyleSheet("QGroupBox#baseLayer {\n"
"    font-size: 24pt;\n"
"    font-weight: bold;\n"
"    border: transparent;\n"
"    padding-top: 30px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    background-color: transparent;\n"
"    color: #6668ad;\n"
"}\n"
"\n"
"/*\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"*/")
        self.baseLayer.setObjectName("baseLayer")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.baseLayer)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.enterQuery = QtWidgets.QGroupBox(self.baseLayer)
        self.enterQuery.setStyleSheet("QGroupBox#enterQuery {\n"
"    border-radius: 20px;\n"
"    background-color: #6668ad;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    padding-top: 30px;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    background-color: transparent;\n"
"    padding-top: 20px;\n"
"    padding-left: 16px;\n"
"    color: white;\n"
"}\n"
"\n"
"/*\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"*/")
        self.enterQuery.setObjectName("enterQuery")
        self.gridLayout = QtWidgets.QGridLayout(self.enterQuery)
        self.gridLayout.setObjectName("gridLayout")
        self.queryBox = QtWidgets.QGroupBox(self.enterQuery)
        self.queryBox.setStyleSheet("/*\n"
"QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}\n"
"*/")
        self.queryBox.setTitle("")
        self.queryBox.setObjectName("queryBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.queryBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.queryBox)
        self.textEdit_2.setStyleSheet("border: transparent;\n"
"background-color: white;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_3.addWidget(self.textEdit_2)
        self.gridLayout.addWidget(self.queryBox, 1, 0, 1, 3)
        self.instructions = QtWidgets.QGroupBox(self.enterQuery)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instructions.sizePolicy().hasHeightForWidth())
        self.instructions.setSizePolicy(sizePolicy)
        self.instructions.setMinimumSize(QtCore.QSize(0, 124))
        self.instructions.setStyleSheet("/*\n"
"QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}\n"
"*/")
        self.instructions.setTitle("")
        self.instructions.setObjectName("instructions")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.instructions)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.instructions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_3.sizePolicy().hasHeightForWidth())
        self.textBrowser_3.setSizePolicy(sizePolicy)
        self.textBrowser_3.setStyleSheet("background-color: transparent;\n"
"border: transparent;")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayout_2.addWidget(self.textBrowser_3)
        self.gridLayout.addWidget(self.instructions, 0, 0, 1, 1)
        self.downloadCSV = QtWidgets.QGroupBox(self.enterQuery)
        self.downloadCSV.setStyleSheet("/*\n"
"QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}\n"
"*/")
        self.downloadCSV.setTitle("")
        self.downloadCSV.setObjectName("downloadCSV")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.downloadCSV)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushButton_6 = QtWidgets.QPushButton(self.downloadCSV)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background: #81cfd8;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 6px solid transparent;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.gridLayout.addWidget(self.downloadCSV, 2, 0, 1, 2)
        self.gridLayout_3.addWidget(self.enterQuery, 2, 0, 1, 1)
        self.notesForUser = QtWidgets.QGroupBox(self.baseLayer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notesForUser.sizePolicy().hasHeightForWidth())
        self.notesForUser.setSizePolicy(sizePolicy)
        self.notesForUser.setMinimumSize(QtCore.QSize(0, 190))
        self.notesForUser.setStyleSheet("QGroupBox#notesForUser {\n"
"    border: transparent;\n"
"    padding-top: 10px;\n"
"}")
        self.notesForUser.setTitle("")
        self.notesForUser.setObjectName("notesForUser")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.notesForUser)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.notesForUser)
        self.textBrowser_5.setStyleSheet("background-color: transparent;\n"
"border: transparent;")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.gridLayout_4.addWidget(self.textBrowser_5, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.notesForUser, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.baseLayer, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.testPage, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_4.setGeometry(QtCore.QRect(20, 110, 522, 158))
        self.textBrowser_4.setStyleSheet("background-color: transparent;\n"
"border: transparent;")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.verticalLayout_3.addWidget(self.tabWidget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#616161;\">If you already have a CSV file, go to the next page.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; font-weight:700; color:#616161;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">CSV file requirements (columns):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - emdb_id</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - title</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - resolution</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - fitted_pdbs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - xref_UNIPROTKB</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - xref_ALPHAFOLD<br /></span><span style=\" font-style:italic; color:#616161;\">  *CSV files are downloaded from EMDB</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "1. Enter a query"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Type in sample name followed by keywords. Common keywords available in dropdown. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Hit </span><span style=\" font-weight:700; color:#ffffff;\">return</span><span style=\" color:#ffffff;\"> after each keyword. </span><span style=\" font-style:italic; color:#ffffff;\">Text not in the form of a tag (hitting return creates a tag) will NOT be read.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">ex. spliceosome </span><span style=\" color:#d1d1d1;\">[return] </span><span style=\" color:#ffffff;\">resolution:2-5</span> <span style=\" color:#d1d1d1;\">[return]</span></p></body></html>"))
        self.textEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>PLACEHOLDER widget, manually replace in code cuz still can\'t figure out how to import custom widgets into Qt Designer (used qt\'s custom widget interface and set environment variables, so maybe my custom widget\'s directory isn\'t set up correctly)</p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Type query here"))
        self.pushButton.setText(_translate("MainWindow", "Download CSV"))
        self.label_5.setText(_translate("MainWindow", "Create CSV"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Create CSV"))
        self.label_4.setText(_translate("MainWindow", "1. Select CSV file (autoselected if did step 1)"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "CSV filepath"))
        self.pushButton_5.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select a CSV file first.</p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "Open CSV editor"))
        self.pushButton_2.setText(_translate("MainWindow", "Generate Dataset"))
        self.label.setText(_translate("MainWindow", "Labels:"))
        self.lineEdit_3.setText(_translate("MainWindow", "64"))
        self.lineEdit_4.setText(_translate("MainWindow", "64"))
        self.label_2.setText(_translate("MainWindow", "2. Dataset Options"))
        self.label_8.setText(_translate("MainWindow", "x"))
        self.lineEdit_2.setText(_translate("MainWindow", "64"))
        self.label_9.setText(_translate("MainWindow", "x"))
        self.label_6.setText(_translate("MainWindow", "Cube size:"))
        self.pushButton_4.setText(_translate("MainWindow", "Advanced options"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Sample type"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Secondary structures"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Residue(s)"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Key atoms"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "Custom selections"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.checkBox_10.setText(_translate("MainWindow", "Protein"))
        self.checkBox_11.setText(_translate("MainWindow", "RNA"))
        self.checkBox_12.setText(_translate("MainWindow", "DNA"))
        self.checkBox_7.setText(_translate("MainWindow", "Helix"))
        self.checkBox_8.setText(_translate("MainWindow", "Sheet"))
        self.checkBox_9.setText(_translate("MainWindow", "Loop"))
        self.checkBox.setText(_translate("MainWindow", "Alanine (A)"))
        self.checkBox_2.setText(_translate("MainWindow", "Cysteine (C)"))
        self.checkBox_3.setText(_translate("MainWindow", "Aspartic acid (D)"))
        self.checkBox_13.setText(_translate("MainWindow", "Glutamic acid (E)"))
        self.checkBox_14.setText(_translate("MainWindow", "Phenylalanine (F)"))
        self.checkBox_15.setText(_translate("MainWindow", "Glycine (G)"))
        self.checkBox_16.setText(_translate("MainWindow", "Histidine (H)"))
        self.checkBox_17.setText(_translate("MainWindow", "Isoleucine (I)"))
        self.checkBox_18.setText(_translate("MainWindow", "Lysine (K)"))
        self.checkBox_19.setText(_translate("MainWindow", "Leucine (L)"))
        self.checkBox_20.setText(_translate("MainWindow", "Methionine (M)"))
        self.checkBox_21.setText(_translate("MainWindow", "Asparagine (N)"))
        self.checkBox_22.setText(_translate("MainWindow", "Proline (P)"))
        self.checkBox_23.setText(_translate("MainWindow", "Glutamine (Q)"))
        self.checkBox_24.setText(_translate("MainWindow", "Arginine (R)"))
        self.checkBox_25.setText(_translate("MainWindow", "Serine (S)"))
        self.checkBox_26.setText(_translate("MainWindow", "Threonine (T)"))
        self.checkBox_27.setText(_translate("MainWindow", "Valine (V)"))
        self.checkBox_28.setText(_translate("MainWindow", "Tryptophan (W)"))
        self.checkBox_29.setText(_translate("MainWindow", "Tyrosine (Y)"))
        self.label_7.setText(_translate("MainWindow", "Generate Dataset"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Generate Dataset"))
        self.baseLayer.setTitle(_translate("MainWindow", "Create CSV"))
        self.enterQuery.setTitle(_translate("MainWindow", "1. Enter a query"))
        self.textEdit_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>PLACEHOLDER widget, manually replace in code cuz still can\'t figure out how to import custom widgets into Qt Designer (used qt\'s custom widget interface and set environment variables, so maybe my custom widget\'s directory isn\'t set up correctly)</p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Type query here"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Type in sample name followed by keywords. Common keywords available in dropdown. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Hit </span><span style=\" font-weight:700; color:#ffffff;\">return</span><span style=\" color:#ffffff;\"> after each keyword. </span><span style=\" font-style:italic; color:#ffffff;\">Text not in the form of a tag (hitting return creates a tag) will NOT be read.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">ex. spliceosome </span><span style=\" color:#d1d1d1;\">[return] </span><span style=\" color:#ffffff;\">resolution:2-5</span> <span style=\" color:#d1d1d1;\">[return]</span></p></body></html>"))
        self.pushButton_6.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">this is limiting the window\'s thickness when shrinking btw, prob a better way to go about sizepolicys</span></p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "Download CSV"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#616161;\">If you already have a CSV file, go to the next page.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; font-weight:700; color:#616161;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">CSV file requirements (columns):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - emdb_id</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - title</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - resolution</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - fitted_pdbs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - xref_UNIPROTKB</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - xref_ALPHAFOLD<br /></span><span style=\" font-style:italic; color:#616161;\">  *CSV files are downloaded from EMDB</span></p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.testPage), _translate("MainWindow", "Page"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#616161;\">If you already have a CSV file, go to the next page.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; font-weight:700; color:#616161;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">CSV file requirements (columns):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - emdb_id</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - title</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - resolution</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - fitted_pdbs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - xref_UNIPROTKB</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#616161;\">     - xref_ALPHAFOLD<br /></span><span style=\" font-style:italic; color:#616161;\">  *CSV files are downloaded from EMDB</span></p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Page"))


if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"          # added line 1/2
    # os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
    # os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    # os.environ["QT_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)      # added line 2/2, still should continue creating proper layouts and sizePolicy's and using spacers when needed
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
