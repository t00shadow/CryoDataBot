# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/c/Users/noelu/Python Projects/PyQt GUI practice/QtDesigner_practice/dataset_gen_tool_GUI/dataset_gen_tool_v8.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 841)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    /*border-top: 2px solid #C2C7CB;*/\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 12ex;\n"
"    padding: 2px 8px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"QTabBar::tab:first {\n"
"    border-top-color: #6668ad;\n"
"    border-left-color: #6668ad;\n"
"    border-right-color: #6668ad;\n"
"    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,\n"
"                                stop: 0 #FF92BB, stop: 1 white);\n"
"}\n"
"\n"
"QTabBar::tab:last {\n"
"    border-top-color: #ffaaff;\n"
"    border-left-color: #ffaaff;\n"
"    border-right-color: #ffaaff;\n"
"    color: #ffaaff;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.baseLayer_1 = QtWidgets.QGroupBox(self.page1)
        self.baseLayer_1.setStyleSheet("QGroupBox#baseLayer_1 {\n"
"    font-size: 24pt;\n"
"    font-weight: bold;\n"
"    border: transparent;\n"
"    padding-top: 30px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    background-color: transparent;\n"
"    color: #6668ad;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"/*\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"*/")
        self.baseLayer_1.setObjectName("baseLayer_1")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.baseLayer_1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem1, 0, 0, 1, 1)
        self.A_quickStart = QtWidgets.QGroupBox(self.baseLayer_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A_quickStart.sizePolicy().hasHeightForWidth())
        self.A_quickStart.setSizePolicy(sizePolicy)
        self.A_quickStart.setStyleSheet("QGroupBox#A_quickStart {\n"
"    border-radius: 20px;\n"
"    background-color: #6668ad;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    /*padding-top: 30px;*/\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    background-color: transparent;\n"
"    padding-top: 20px;\n"
"    /*padding-left: 16px;*/\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"")
        self.A_quickStart.setTitle("")
        self.A_quickStart.setObjectName("A_quickStart")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.A_quickStart)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.A1_instructions = QtWidgets.QGroupBox(self.A_quickStart)
        self.A1_instructions.setMinimumSize(QtCore.QSize(0, 300))
        self.A1_instructions.setMaximumSize(QtCore.QSize(16777215, 350))
        self.A1_instructions.setStyleSheet("\n"
"QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}\n"
"")
        self.A1_instructions.setTitle("")
        self.A1_instructions.setObjectName("A1_instructions")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.A1_instructions)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.textBrowser_p1 = QtWidgets.QTextBrowser(self.A1_instructions)
        self.textBrowser_p1.setMaximumSize(QtCore.QSize(16777215, 400))
        self.textBrowser_p1.setStyleSheet("background-color: transparent;\n"
"border: transparent;")
        self.textBrowser_p1.setOpenExternalLinks(True)
        self.textBrowser_p1.setObjectName("textBrowser_p1")
        self.horizontalLayout_11.addWidget(self.textBrowser_p1)
        self.verticalLayout_2.addWidget(self.A1_instructions)
        self.label = QtWidgets.QLabel(self.A_quickStart)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #ffffff;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.A4_queryBox = QtWidgets.QGroupBox(self.A_quickStart)
        self.A4_queryBox.setStyleSheet("QGroupBox#B2_queryBox_2{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"    padding-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    padding: 0;\n"
"}")
        self.A4_queryBox.setTitle("")
        self.A4_queryBox.setObjectName("A4_queryBox")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.A4_queryBox)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lineEdit = QtWidgets.QLineEdit(self.A4_queryBox)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_12.addWidget(self.lineEdit)
        self.pushButton_p1_2 = QtWidgets.QPushButton(self.A4_queryBox)
        self.pushButton_p1_2.setStyleSheet("QPushButton {\n"
"    background: #e5e5e5;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 6px solid transparent;\n"
"}")
        self.pushButton_p1_2.setObjectName("pushButton_p1_2")
        self.horizontalLayout_12.addWidget(self.pushButton_p1_2)
        self.verticalLayout_2.addWidget(self.A4_queryBox)
        self.widget_4 = QtWidgets.QWidget(self.A_quickStart)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #ffffff;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #ffffff;")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget = QtWidgets.QWidget(self.A_quickStart)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: lightgrey;\n"
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
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: lightgrey;\n"
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
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.widget)
        self.label_3 = QtWidgets.QLabel(self.A_quickStart)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #ffffff;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.A2_savePath = QtWidgets.QGroupBox(self.A_quickStart)
        self.A2_savePath.setTitle("")
        self.A2_savePath.setObjectName("A2_savePath")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.A2_savePath)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.lineEdit_p1 = QtWidgets.QLineEdit(self.A2_savePath)
        self.lineEdit_p1.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_p1.setText("")
        self.lineEdit_p1.setDragEnabled(False)
        self.lineEdit_p1.setClearButtonEnabled(True)
        self.lineEdit_p1.setObjectName("lineEdit_p1")
        self.horizontalLayout_41.addWidget(self.lineEdit_p1)
        self.pushButton_p1 = QtWidgets.QPushButton(self.A2_savePath)
        self.pushButton_p1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p1.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.pushButton_p1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/browsefilesicon_zoomed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_p1.setIcon(icon1)
        self.pushButton_p1.setObjectName("pushButton_p1")
        self.horizontalLayout_41.addWidget(self.pushButton_p1)
        self.verticalLayout_2.addWidget(self.A2_savePath)
        self.A5_generateDataset = QtWidgets.QGroupBox(self.A_quickStart)
        self.A5_generateDataset.setStyleSheet("\n"
"QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}\n"
"")
        self.A5_generateDataset.setTitle("")
        self.A5_generateDataset.setObjectName("A5_generateDataset")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.A5_generateDataset)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem4)
        self.pushButton_p1_3 = QtWidgets.QPushButton(self.A5_generateDataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p1_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p1_3.setSizePolicy(sizePolicy)
        self.pushButton_p1_3.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_p1_3.setFont(font)
        self.pushButton_p1_3.setStyleSheet("QPushButton {\n"
"    background: #81cfd8;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:pressed {\n"
"    background: #000000;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 6px solid transparent;\n"
"}")
        self.pushButton_p1_3.setObjectName("pushButton_p1_3")
        self.horizontalLayout_14.addWidget(self.pushButton_p1_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem5)
        self.verticalLayout_2.addWidget(self.A5_generateDataset)
        self.widget_2 = QtWidgets.QWidget(self.A_quickStart)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.progressBar = QtWidgets.QProgressBar(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 20))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    /*background-color: #CD96CD;*/\n"
"    background-color: #60b5ff;\n"
"    width: 10px;\n"
"    margin: 0.5px;\n"
"}\n"
"")
        self.progressBar.setProperty("value", 37)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.gridLayout_7.addWidget(self.A_quickStart, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.baseLayer_1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.page1, "")
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 1, 0, 1, 1)
        self.baseLayer_2 = QtWidgets.QGroupBox(self.page2)
        self.baseLayer_2.setStyleSheet("QGroupBox#baseLayer_2 {\n"
"    font-size: 24pt;\n"
"    font-weight: bold;\n"
"    border: transparent;\n"
"    padding-top: 30px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    background-color: transparent;\n"
"    color: #81cfd8;\n"
"    padding-bottom: 10px;\n"
"    /*padding-left: 10px;*/\n"
"}\n"
"\n"
"/*\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"*/")
        self.baseLayer_2.setObjectName("baseLayer_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.baseLayer_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem7, 0, 0, 1, 1)
        self.B_enterQuery = QtWidgets.QGroupBox(self.baseLayer_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B_enterQuery.sizePolicy().hasHeightForWidth())
        self.B_enterQuery.setSizePolicy(sizePolicy)
        self.B_enterQuery.setStyleSheet("QGroupBox#B_enterQuery {\n"
"    border-radius: 20px;\n"
"    background-color: #81cfd8;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    /*padding-top: 30px;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;*/\n"
"    padding: 30% 15% 20%;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    background-color: transparent;\n"
"    padding-top: 20px;\n"
"    padding-left: 16px;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"")
        self.B_enterQuery.setObjectName("B_enterQuery")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.B_enterQuery)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.B4_downloadbtn = QtWidgets.QGroupBox(self.B_enterQuery)
        self.B4_downloadbtn.setStyleSheet("\n"
"QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}\n"
"")
        self.B4_downloadbtn.setTitle("")
        self.B4_downloadbtn.setObjectName("B4_downloadbtn")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.B4_downloadbtn)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.pushButton_p2_2 = QtWidgets.QPushButton(self.B4_downloadbtn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p2_2.sizePolicy().hasHeightForWidth())
        self.pushButton_p2_2.setSizePolicy(sizePolicy)
        self.pushButton_p2_2.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_p2_2.setFont(font)
        self.pushButton_p2_2.setStyleSheet("QPushButton {\n"
"    background: #6668ad;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:pressed {\n"
"    background: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 6px solid transparent;\n"
"}")
        self.pushButton_p2_2.setObjectName("pushButton_p2_2")
        self.horizontalLayout_4.addWidget(self.pushButton_p2_2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.gridLayout_9.addWidget(self.B4_downloadbtn, 4, 0, 1, 1)
        self.B5_progressDisplay = QtWidgets.QGroupBox(self.B_enterQuery)
        self.B5_progressDisplay.setTitle("")
        self.B5_progressDisplay.setObjectName("B5_progressDisplay")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.B5_progressDisplay)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.progressBar_p4_2 = QtWidgets.QProgressBar(self.B5_progressDisplay)
        self.progressBar_p4_2.setMaximumSize(QtCore.QSize(16777215, 16))
        self.progressBar_p4_2.setStyleSheet("QProgressBar {\n"
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
        self.progressBar_p4_2.setProperty("value", 24)
        self.progressBar_p4_2.setObjectName("progressBar_p4_2")
        self.horizontalLayout_13.addWidget(self.progressBar_p4_2)
        self.gridLayout_9.addWidget(self.B5_progressDisplay, 5, 0, 1, 1)
        self.rename_everything = QtWidgets.QWidget(self.B_enterQuery)
        self.rename_everything.setObjectName("rename_everything")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.rename_everything)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.rename_everything)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.B1_csvFilepath = QtWidgets.QGroupBox(self.rename_everything)
        self.B1_csvFilepath.setTitle("")
        self.B1_csvFilepath.setObjectName("B1_csvFilepath")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.B1_csvFilepath)
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.lineEdit_p2 = QtWidgets.QLineEdit(self.B1_csvFilepath)
        self.lineEdit_p2.setEnabled(True)
        self.lineEdit_p2.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_p2.setText("")
        self.lineEdit_p2.setDragEnabled(False)
        self.lineEdit_p2.setClearButtonEnabled(True)
        self.lineEdit_p2.setObjectName("lineEdit_p2")
        self.horizontalLayout_40.addWidget(self.lineEdit_p2)
        self.pushButton_p2 = QtWidgets.QPushButton(self.B1_csvFilepath)
        self.pushButton_p2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p2.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.pushButton_p2.setText("")
        self.pushButton_p2.setIcon(icon1)
        self.pushButton_p2.setObjectName("pushButton_p2")
        self.horizontalLayout_40.addWidget(self.pushButton_p2)
        self.verticalLayout_6.addWidget(self.B1_csvFilepath)
        self.gridLayout_9.addWidget(self.rename_everything, 3, 0, 1, 1)
        self.B1_instructions = QtWidgets.QGroupBox(self.B_enterQuery)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B1_instructions.sizePolicy().hasHeightForWidth())
        self.B1_instructions.setSizePolicy(sizePolicy)
        self.B1_instructions.setMinimumSize(QtCore.QSize(0, 100))
        self.B1_instructions.setMaximumSize(QtCore.QSize(16777215, 150))
        self.B1_instructions.setStyleSheet("\n"
"QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}\n"
"")
        self.B1_instructions.setTitle("")
        self.B1_instructions.setObjectName("B1_instructions")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.B1_instructions)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.textBrowser_p2_2 = QtWidgets.QTextBrowser(self.B1_instructions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_p2_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_p2_2.setSizePolicy(sizePolicy)
        self.textBrowser_p2_2.setMinimumSize(QtCore.QSize(0, 180))
        self.textBrowser_p2_2.setStyleSheet("background-color: transparent;\n"
"border: transparent;\n"
"/*padding: 10%;*/")
        self.textBrowser_p2_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textBrowser_p2_2.setOpenExternalLinks(True)
        self.textBrowser_p2_2.setObjectName("textBrowser_p2_2")
        self.verticalLayout_8.addWidget(self.textBrowser_p2_2)
        self.gridLayout_9.addWidget(self.B1_instructions, 0, 0, 1, 1)
        self.B2_queryBox = QtWidgets.QGroupBox(self.B_enterQuery)
        self.B2_queryBox.setStyleSheet("/*QGroupBox#B2_queryBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    background-color: transparent;\n"
"    color: black;\n"
"    padding: 0;\n"
"}\n"
"*/")
        self.B2_queryBox.setTitle("")
        self.B2_queryBox.setObjectName("B2_queryBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.B2_queryBox)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_p2 = QtWidgets.QLabel(self.B2_queryBox)
        self.label_p2.setObjectName("label_p2")
        self.verticalLayout_4.addWidget(self.label_p2)
        self.widget_7 = QtWidgets.QWidget(self.B2_queryBox)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_20.addWidget(self.lineEdit_2)
        self.validateQuery_btn = QtWidgets.QPushButton(self.widget_7)
        self.validateQuery_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.validateQuery_btn.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.validateQuery_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/send-alt-2-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.validateQuery_btn.setIcon(icon2)
        self.validateQuery_btn.setObjectName("validateQuery_btn")
        self.horizontalLayout_20.addWidget(self.validateQuery_btn)
        self.verticalLayout_4.addWidget(self.widget_7)
        self.gridLayout_9.addWidget(self.B2_queryBox, 1, 0, 1, 1)
        self.fancySearchBar = QtWidgets.QWidget(self.B_enterQuery)
        self.fancySearchBar.setStyleSheet("background: black;\n"
"border-radius: 12px;")
        self.fancySearchBar.setObjectName("fancySearchBar")
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout(self.fancySearchBar)
        self.horizontalLayout_58.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.fancySearchBar)
        self.lineEdit_12.setMaximumSize(QtCore.QSize(16777215, 24))
        self.lineEdit_12.setStyleSheet("background: white;\n"
"border: transparent;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"padding-left: 4px;\n"
"padding-bottom: 2px;")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_58.addWidget(self.lineEdit_12)
        self.pushButton_16 = QtWidgets.QPushButton(self.fancySearchBar)
        self.pushButton_16.setMaximumSize(QtCore.QSize(16777215, 24))
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {    \n"
"    background-color: rgba(255, 255, 255, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}")
        self.pushButton_16.setText("")
        self.pushButton_16.setIcon(icon2)
        self.pushButton_16.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_58.addWidget(self.pushButton_16)
        self.gridLayout_9.addWidget(self.fancySearchBar, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.B_enterQuery, 2, 0, 1, 1)
        self.A_notesForUser = QtWidgets.QGroupBox(self.baseLayer_2)
        self.A_notesForUser.setMinimumSize(QtCore.QSize(0, 100))
        self.A_notesForUser.setMaximumSize(QtCore.QSize(16777215, 120))
        self.A_notesForUser.setStyleSheet("QGroupBox#A_notesForUser {\n"
"    border: gray;\n"
"    padding-top: 10px;\n"
"}")
        self.A_notesForUser.setTitle("")
        self.A_notesForUser.setObjectName("A_notesForUser")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.A_notesForUser)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_7.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.textBrowser_p2 = QtWidgets.QTextBrowser(self.A_notesForUser)
        self.textBrowser_p2.setMaximumSize(QtCore.QSize(16777215, 180))
        self.textBrowser_p2.setStyleSheet("background-color: transparent;\n"
"border: transparent;")
        self.textBrowser_p2.setOpenExternalLinks(True)
        self.textBrowser_p2.setObjectName("textBrowser_p2")
        self.verticalLayout_7.addWidget(self.textBrowser_p2)
        self.gridLayout_3.addWidget(self.A_notesForUser, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.baseLayer_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.page2, "")
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page3)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.baseLayer_3 = QtWidgets.QGroupBox(self.page3)
        self.baseLayer_3.setStyleSheet("QGroupBox#baseLayer_3 {\n"
"    font-size: 24pt;\n"
"    font-weight: bold;\n"
"    border: transparent;\n"
"    padding-top: 30px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    background-color: transparent;\n"
"    color: #81cfd8;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"/*\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"*/")
        self.baseLayer_3.setObjectName("baseLayer_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.baseLayer_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem10, 0, 0, 1, 1)
        self.A_chooseCSV = QtWidgets.QGroupBox(self.baseLayer_3)
        self.A_chooseCSV.setStyleSheet("QGroupBox#A_chooseCSV {\n"
"    border-radius: 20px;\n"
"    background-color: #81cfd8;\n"
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
"    color: black;\n"
"}\n"
"\n"
"\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"")
        self.A_chooseCSV.setObjectName("A_chooseCSV")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.A_chooseCSV)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.A1_dragAndDrop = QtWidgets.QGroupBox(self.A_chooseCSV)
        self.A1_dragAndDrop.setTitle("")
        self.A1_dragAndDrop.setObjectName("A1_dragAndDrop")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.A1_dragAndDrop)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_19.addWidget(self.A1_dragAndDrop)
        self.A2_csvFilepath = QtWidgets.QGroupBox(self.A_chooseCSV)
        self.A2_csvFilepath.setTitle("")
        self.A2_csvFilepath.setObjectName("A2_csvFilepath")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.A2_csvFilepath)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.lineEdit_p3 = QtWidgets.QLineEdit(self.A2_csvFilepath)
        self.lineEdit_p3.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_p3.setText("")
        self.lineEdit_p3.setDragEnabled(False)
        self.lineEdit_p3.setClearButtonEnabled(True)
        self.lineEdit_p3.setObjectName("lineEdit_p3")
        self.horizontalLayout_19.addWidget(self.lineEdit_p3)
        self.pushButton_p3 = QtWidgets.QPushButton(self.A2_csvFilepath)
        self.pushButton_p3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_p3.setStyleSheet("/*border-image: url(:/icons/browsefilesicon.png);*/\n"
"background-color: white;\n"
"border-radius: 6;")
        self.pushButton_p3.setText("")
        self.pushButton_p3.setIcon(icon1)
        self.pushButton_p3.setObjectName("pushButton_p3")
        self.horizontalLayout_19.addWidget(self.pushButton_p3)
        self.verticalLayout_19.addWidget(self.A2_csvFilepath)
        self.gridLayout_6.addWidget(self.A_chooseCSV, 1, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem11, 2, 0, 1, 1)
        self.B_refineCSV = QtWidgets.QGroupBox(self.baseLayer_3)
        self.B_refineCSV.setStyleSheet("QGroupBox#B_refineCSV {\n"
"    border-radius: 20px;\n"
"    background-color: #81cfd8;\n"
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
"    color: black;\n"
"}\n"
"\n"
"\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"")
        self.B_refineCSV.setObjectName("B_refineCSV")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.B_refineCSV)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.B1_dragAndDrop = QtWidgets.QGroupBox(self.B_refineCSV)
        self.B1_dragAndDrop.setStyleSheet("")
        self.B1_dragAndDrop.setTitle("")
        self.B1_dragAndDrop.setObjectName("B1_dragAndDrop")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.B1_dragAndDrop)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.verticalLayout_9.addWidget(self.B1_dragAndDrop)
        self.widget_6 = QtWidgets.QWidget(self.B_refineCSV)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.widget1 = QtWidgets.QWidget(self.widget_6)
        self.widget1.setObjectName("widget1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_4.setVerticalSpacing(12)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.similaritySpinBox = QtWidgets.QSpinBox(self.widget1)
        self.similaritySpinBox.setAccelerated(True)
        self.similaritySpinBox.setMaximum(100)
        self.similaritySpinBox.setObjectName("similaritySpinBox")
        self.gridLayout_4.addWidget(self.similaritySpinBox, 2, 1, 1, 1)
        self.clearMMF_btn = QtWidgets.QPushButton(self.widget1)
        self.clearMMF_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearMMF_btn.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.clearMMF_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/reset-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearMMF_btn.setIcon(icon3)
        self.clearMMF_btn.setObjectName("clearMMF_btn")
        self.gridLayout_4.addWidget(self.clearMMF_btn, 1, 2, 1, 1)
        self.mapModelFitnessSpinBox = QtWidgets.QSpinBox(self.widget1)
        self.mapModelFitnessSpinBox.setAccelerated(True)
        self.mapModelFitnessSpinBox.setMaximum(100)
        self.mapModelFitnessSpinBox.setObjectName("mapModelFitnessSpinBox")
        self.gridLayout_4.addWidget(self.mapModelFitnessSpinBox, 1, 1, 1, 1)
        self.similarityLabel = QtWidgets.QLabel(self.widget1)
        self.similarityLabel.setObjectName("similarityLabel")
        self.gridLayout_4.addWidget(self.similarityLabel, 2, 0, 1, 1)
        self.mapModelFitnessLabel = QtWidgets.QLabel(self.widget1)
        self.mapModelFitnessLabel.setObjectName("mapModelFitnessLabel")
        self.gridLayout_4.addWidget(self.mapModelFitnessLabel, 1, 0, 1, 1)
        self.qScoreSpinBox = QtWidgets.QSpinBox(self.widget1)
        self.qScoreSpinBox.setAccelerated(True)
        self.qScoreSpinBox.setMaximum(100)
        self.qScoreSpinBox.setObjectName("qScoreSpinBox")
        self.gridLayout_4.addWidget(self.qScoreSpinBox, 0, 1, 1, 1)
        self.clearSim_btn = QtWidgets.QPushButton(self.widget1)
        self.clearSim_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearSim_btn.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.clearSim_btn.setText("")
        self.clearSim_btn.setIcon(icon3)
        self.clearSim_btn.setObjectName("clearSim_btn")
        self.gridLayout_4.addWidget(self.clearSim_btn, 2, 2, 1, 1)
        self.qScoreLabel = QtWidgets.QLabel(self.widget1)
        self.qScoreLabel.setObjectName("qScoreLabel")
        self.gridLayout_4.addWidget(self.qScoreLabel, 0, 0, 1, 1)
        self.clearQScore_btn = QtWidgets.QPushButton(self.widget1)
        self.clearQScore_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearQScore_btn.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.clearQScore_btn.setText("")
        self.clearQScore_btn.setIcon(icon3)
        self.clearQScore_btn.setObjectName("clearQScore_btn")
        self.gridLayout_4.addWidget(self.clearQScore_btn, 0, 2, 1, 1)
        self.horizontalLayout_17.addWidget(self.widget1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem12)
        self.verticalLayout_9.addWidget(self.widget_6)
        self.B2_csvFilepath = QtWidgets.QGroupBox(self.B_refineCSV)
        self.B2_csvFilepath.setTitle("")
        self.B2_csvFilepath.setObjectName("B2_csvFilepath")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.B2_csvFilepath)
        self.horizontalLayout_39.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.lineEdit_p3_2 = QtWidgets.QLineEdit(self.B2_csvFilepath)
        self.lineEdit_p3_2.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_p3_2.setDragEnabled(False)
        self.lineEdit_p3_2.setClearButtonEnabled(True)
        self.lineEdit_p3_2.setObjectName("lineEdit_p3_2")
        self.horizontalLayout_39.addWidget(self.lineEdit_p3_2)
        self.pushButton_p3_2 = QtWidgets.QPushButton(self.B2_csvFilepath)
        self.pushButton_p3_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p3_2.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.pushButton_p3_2.setText("")
        self.pushButton_p3_2.setIcon(icon1)
        self.pushButton_p3_2.setObjectName("pushButton_p3_2")
        self.horizontalLayout_39.addWidget(self.pushButton_p3_2)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem13)
        self.pushButton_p3_3 = QtWidgets.QPushButton(self.B2_csvFilepath)
        self.pushButton_p3_3.setStyleSheet("QPushButton {\n"
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
        self.pushButton_p3_3.setIcon(icon)
        self.pushButton_p3_3.setObjectName("pushButton_p3_3")
        self.horizontalLayout_39.addWidget(self.pushButton_p3_3)
        self.verticalLayout_9.addWidget(self.B2_csvFilepath)
        self.B4_downloadbtn_2 = QtWidgets.QGroupBox(self.B_refineCSV)
        self.B4_downloadbtn_2.setStyleSheet("\n"
"QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}\n"
"")
        self.B4_downloadbtn_2.setTitle("")
        self.B4_downloadbtn_2.setObjectName("B4_downloadbtn_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.B4_downloadbtn_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.pushButton_p3_4 = QtWidgets.QPushButton(self.B4_downloadbtn_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p3_4.sizePolicy().hasHeightForWidth())
        self.pushButton_p3_4.setSizePolicy(sizePolicy)
        self.pushButton_p3_4.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_p3_4.setFont(font)
        self.pushButton_p3_4.setStyleSheet("QPushButton {\n"
"    background: #6668ad;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:pressed {\n"
"    background: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 6px solid transparent;\n"
"}")
        self.pushButton_p3_4.setObjectName("pushButton_p3_4")
        self.horizontalLayout_5.addWidget(self.pushButton_p3_4)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.verticalLayout_9.addWidget(self.B4_downloadbtn_2)
        self.gridLayout_6.addWidget(self.B_refineCSV, 3, 0, 1, 1)
        self.gridLayout_12.addWidget(self.baseLayer_3, 0, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem16, 1, 0, 1, 1)
        self.tabWidget.addTab(self.page3, "")
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.page4)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.baseLayer_4 = QtWidgets.QGroupBox(self.page4)
        self.baseLayer_4.setStyleSheet("QGroupBox#baseLayer_4 {\n"
"    font-size: 24pt;\n"
"    font-weight: bold;\n"
"    border: transparent;\n"
"    padding-top: 30px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    background-color: transparent;\n"
"    color: #81cfd8;\n"
"    padding-bottom: 10px;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"/*\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"*/")
        self.baseLayer_4.setObjectName("baseLayer_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.baseLayer_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.A_datasetOptions = QtWidgets.QGroupBox(self.baseLayer_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A_datasetOptions.sizePolicy().hasHeightForWidth())
        self.A_datasetOptions.setSizePolicy(sizePolicy)
        self.A_datasetOptions.setStyleSheet("QGroupBox#A_datasetOptions {\n"
"    border-radius: 20px;\n"
"    background-color: #81cfd8;\n"
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
"    color: black;\n"
"}\n"
"\n"
"\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"")
        self.A_datasetOptions.setObjectName("A_datasetOptions")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.A_datasetOptions)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.A_datasetOptions)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_15.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.addgroup_btn = QtWidgets.QPushButton(self.widget_3)
        self.addgroup_btn.setObjectName("addgroup_btn")
        self.horizontalLayout_15.addWidget(self.addgroup_btn)
        self.addlabel_btn = QtWidgets.QPushButton(self.widget_3)
        self.addlabel_btn.setObjectName("addlabel_btn")
        self.horizontalLayout_15.addWidget(self.addlabel_btn)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem17)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.A1_featureLabels = QtWidgets.QGroupBox(self.A_datasetOptions)
        self.A1_featureLabels.setMinimumSize(QtCore.QSize(0, 300))
        self.A1_featureLabels.setMaximumSize(QtCore.QSize(16777215, 400))
        self.A1_featureLabels.setObjectName("A1_featureLabels")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.A1_featureLabels)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.treeWidget_p4 = QtWidgets.QTreeWidget(self.A1_featureLabels)
        self.treeWidget_p4.setStyleSheet("QTreeWidget::item {\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    background-color: #85b5e8;\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background-color: #85b5e8;\n"
"}")
        self.treeWidget_p4.setAlternatingRowColors(True)
        self.treeWidget_p4.setAnimated(True)
        self.treeWidget_p4.setObjectName("treeWidget_p4")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_p4)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_p4)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_p4)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.horizontalLayout_9.addWidget(self.treeWidget_p4)
        self.verticalLayout_3.addWidget(self.A1_featureLabels)
        self.A2_cubeSize = QtWidgets.QGroupBox(self.A_datasetOptions)
        self.A2_cubeSize.setTitle("")
        self.A2_cubeSize.setObjectName("A2_cubeSize")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.A2_cubeSize)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_p4 = QtWidgets.QLabel(self.A2_cubeSize)
        self.label_p4.setObjectName("label_p4")
        self.horizontalLayout_10.addWidget(self.label_p4)
        self.lineEdit_p4 = QtWidgets.QLineEdit(self.A2_cubeSize)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_p4.sizePolicy().hasHeightForWidth())
        self.lineEdit_p4.setSizePolicy(sizePolicy)
        self.lineEdit_p4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_p4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_p4.setObjectName("lineEdit_p4")
        self.horizontalLayout_10.addWidget(self.lineEdit_p4)
        self.label_p4_2 = QtWidgets.QLabel(self.A2_cubeSize)
        self.label_p4_2.setObjectName("label_p4_2")
        self.horizontalLayout_10.addWidget(self.label_p4_2)
        spacerItem18 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem18)
        self.verticalLayout_3.addWidget(self.A2_cubeSize)
        self.widget_5 = QtWidgets.QWidget(self.A_datasetOptions)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_10 = QtWidgets.QLabel(self.widget_5)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_16.addWidget(self.label_10)
        self.spinBox = QtWidgets.QSpinBox(self.widget_5)
        self.spinBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_16.addWidget(self.spinBox)
        self.label_11 = QtWidgets.QLabel(self.widget_5)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_16.addWidget(self.label_11)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget_5)
        self.spinBox_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.spinBox_2.setMaximum(100)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_16.addWidget(self.spinBox_2)
        self.label_12 = QtWidgets.QLabel(self.widget_5)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_16.addWidget(self.label_12)
        self.spinBox_3 = QtWidgets.QSpinBox(self.widget_5)
        self.spinBox_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.spinBox_3.setMaximum(100)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_16.addWidget(self.spinBox_3)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.A4_generateDataset = QtWidgets.QGroupBox(self.A_datasetOptions)
        self.A4_generateDataset.setTitle("")
        self.A4_generateDataset.setObjectName("A4_generateDataset")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.A4_generateDataset)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem19)
        self.pushButton_p4_2 = QtWidgets.QPushButton(self.A4_generateDataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p4_2.sizePolicy().hasHeightForWidth())
        self.pushButton_p4_2.setSizePolicy(sizePolicy)
        self.pushButton_p4_2.setMinimumSize(QtCore.QSize(170, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_p4_2.setFont(font)
        self.pushButton_p4_2.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background: #6668ad;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:pressed {\n"
"    background: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 6px solid transparent;\n"
"}")
        self.pushButton_p4_2.setObjectName("pushButton_p4_2")
        self.horizontalLayout_6.addWidget(self.pushButton_p4_2)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem20)
        self.verticalLayout_3.addWidget(self.A4_generateDataset)
        self.A5_progressDisplay = QtWidgets.QGroupBox(self.A_datasetOptions)
        self.A5_progressDisplay.setTitle("")
        self.A5_progressDisplay.setObjectName("A5_progressDisplay")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.A5_progressDisplay)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.progressBar_p4 = QtWidgets.QProgressBar(self.A5_progressDisplay)
        self.progressBar_p4.setMaximumSize(QtCore.QSize(16777215, 16))
        self.progressBar_p4.setStyleSheet("QProgressBar {\n"
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
        self.progressBar_p4.setProperty("value", 24)
        self.progressBar_p4.setObjectName("progressBar_p4")
        self.horizontalLayout_7.addWidget(self.progressBar_p4)
        self.verticalLayout_3.addWidget(self.A5_progressDisplay)
        self.gridLayout_5.addWidget(self.A_datasetOptions, 3, 0, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem21, 0, 0, 1, 1)
        self.A2_savePath_2 = QtWidgets.QGroupBox(self.baseLayer_4)
        self.A2_savePath_2.setTitle("")
        self.A2_savePath_2.setObjectName("A2_savePath_2")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout(self.A2_savePath_2)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.lineEdit_p1_2 = QtWidgets.QLineEdit(self.A2_savePath_2)
        self.lineEdit_p1_2.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_p1_2.setDragEnabled(False)
        self.lineEdit_p1_2.setClearButtonEnabled(True)
        self.lineEdit_p1_2.setObjectName("lineEdit_p1_2")
        self.horizontalLayout_42.addWidget(self.lineEdit_p1_2)
        self.pushButton_p1_4 = QtWidgets.QPushButton(self.A2_savePath_2)
        self.pushButton_p1_4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_p1_4.setStyleSheet("/*border-image: url(:/icons/browsefilesicon.png);*/\n"
"background-color: white;\n"
"border-radius: 6;")
        self.pushButton_p1_4.setText("")
        self.pushButton_p1_4.setIcon(icon1)
        self.pushButton_p1_4.setObjectName("pushButton_p1_4")
        self.horizontalLayout_42.addWidget(self.pushButton_p1_4)
        self.gridLayout_5.addWidget(self.A2_savePath_2, 1, 0, 1, 1)
        self.verticalLayout_18.addWidget(self.baseLayer_4)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem22)
        self.tabWidget.addTab(self.page4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("QWidget#tab {\n"
"    \n"
"    background-color: rgb(234, 234, 234);\n"
"}")
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 530, 160, 214))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.option1Label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.option1Label_2.setObjectName("option1Label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.option1Label_2)
        self.option1LineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.option1LineEdit_2.setObjectName("option1LineEdit_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.option1LineEdit_2)
        self.option2Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.option2Label.setObjectName("option2Label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.option2Label)
        self.option2LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.option2LineEdit.setObjectName("option2LineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.option2LineEdit)
        self.option3Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.option3Label.setObjectName("option3Label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.option3Label)
        self.option3LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.option3LineEdit.setObjectName("option3LineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.option3LineEdit)
        self.option4Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.option4Label.setObjectName("option4Label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.option4Label)
        self.option4LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.option4LineEdit.setObjectName("option4LineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.option4LineEdit)
        self.option5Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.option5Label.setObjectName("option5Label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.option5Label)
        self.option5LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.option5LineEdit.setObjectName("option5LineEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.option5LineEdit)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.adfasfLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.adfasfLabel.setObjectName("adfasfLabel")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.adfasfLabel)
        self.adfasfDial = QtWidgets.QDial(self.formLayoutWidget)
        self.adfasfDial.setObjectName("adfasfDial")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.adfasfDial)
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(270, 630, 186, 62))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("Color: grey;")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSlider = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider.setStyleSheet("")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setPageStep(2)
        self.horizontalSlider.setProperty("value", 10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(15, 0))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.widget_9 = QtWidgets.QWidget(self.tab)
        self.widget_9.setGeometry(QtCore.QRect(50, 10, 611, 351))
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_26 = QtWidgets.QLabel(self.widget_9)
        self.label_26.setTextFormat(QtCore.Qt.PlainText)
        self.label_26.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_11.addWidget(self.label_26)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget_9)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_11.addWidget(self.plainTextEdit)
        self.widget_8 = QtWidgets.QWidget(self.widget_9)
        self.widget_8.setStyleSheet("background: black;\n"
"border-radius: 16px;")
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_8)
        self.lineEdit_3.setStyleSheet("background: white;\n"
"border: transparent;\n"
"border-radius: 8px;\n"
"padding-left: 4px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_21.addWidget(self.lineEdit_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_21.addWidget(self.pushButton_4)
        self.verticalLayout_11.addWidget(self.widget_8)
        self.label_28 = QtWidgets.QLabel(self.widget_9)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_11.addWidget(self.label_28)
        self.widget_20 = QtWidgets.QWidget(self.widget_9)
        self.widget_20.setStyleSheet("background: black;\n"
"border-radius: 12px;")
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout(self.widget_20)
        self.horizontalLayout_54.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget_20)
        self.lineEdit_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_8.setStyleSheet("background: white;\n"
"border: transparent;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"padding-left: 4px;\n"
"padding-bottom: 2px;")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_54.addWidget(self.lineEdit_8)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_20)
        self.pushButton_12.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    padding-right: 2px;\n"
"    padding-top: 1px;\n"
"    padding-bottom: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {    \n"
"    background-color: rgba(255, 255, 255, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}")
        self.pushButton_12.setText("")
        self.pushButton_12.setIcon(icon2)
        self.pushButton_12.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_54.addWidget(self.pushButton_12)
        self.verticalLayout_11.addWidget(self.widget_20)
        self.label_14 = QtWidgets.QLabel(self.widget_9)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_11.addWidget(self.label_14)
        self.widget_21 = QtWidgets.QWidget(self.widget_9)
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout(self.widget_21)
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget_21)
        self.lineEdit_9.setStyleSheet("background: white;\n"
"border: transparent;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"padding-left: 4px;\n"
"padding-bottom: 2px;")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_55.addWidget(self.lineEdit_9)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_21)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    padding-right: 2px;\n"
"    padding-top: 1px;\n"
"    padding-bottom: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {    \n"
"    background-color: rgba(255, 255, 255, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}")
        self.pushButton_13.setText("")
        self.pushButton_13.setIcon(icon2)
        self.pushButton_13.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_55.addWidget(self.pushButton_13)
        self.verticalLayout_11.addWidget(self.widget_21)
        self.label_29 = QtWidgets.QLabel(self.widget_9)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_11.addWidget(self.label_29)
        self.widget_24 = QtWidgets.QWidget(self.widget_9)
        self.widget_24.setStyleSheet("background: black;\n"
"border-radius: 12px;")
        self.widget_24.setObjectName("widget_24")
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout(self.widget_24)
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.widget_25 = QtWidgets.QWidget(self.widget_24)
        self.widget_25.setObjectName("widget_25")
        self.horizontalLayout_62 = QtWidgets.QHBoxLayout(self.widget_25)
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.widget_25)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_14.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_14.setStyleSheet("background: white;\n"
"border: transparent;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"padding-left: 4px;\n"
"padding-bottom: 2px;")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_62.addWidget(self.lineEdit_14)
        self.pushButton_18 = QtWidgets.QPushButton(self.widget_25)
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_18.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_18.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    padding-right: 2px;\n"
"    padding-top: 1px;\n"
"    padding-bottom: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {    \n"
"    background-color: rgba(255, 255, 255, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}")
        self.pushButton_18.setText("")
        self.pushButton_18.setIcon(icon2)
        self.pushButton_18.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_62.addWidget(self.pushButton_18)
        self.horizontalLayout_61.addWidget(self.widget_25)
        self.verticalLayout_11.addWidget(self.widget_24)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_11.addWidget(self.pushButton_5)
        self.widget_26 = QtWidgets.QWidget(self.tab)
        self.widget_26.setGeometry(QtCore.QRect(70, 440, 593, 20))
        self.widget_26.setObjectName("widget_26")
        self.horizontalLayout_64 = QtWidgets.QHBoxLayout(self.widget_26)
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.widget_26)
        self.lineEdit_16.setStyleSheet("background: white;\n"
"border: transparent;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"padding-left: 4px;\n"
"padding-bottom: 2px;")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.horizontalLayout_64.addWidget(self.lineEdit_16)
        self.pushButton_20 = QtWidgets.QPushButton(self.widget_26)
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_20.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    padding-right: 2px;\n"
"    padding-top: 1px;\n"
"    padding-bottom: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {    \n"
"    background-color: rgba(255, 255, 255, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}")
        self.pushButton_20.setText("")
        self.pushButton_20.setIcon(icon2)
        self.pushButton_20.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_64.addWidget(self.pushButton_20)
        self.widget_27 = QtWidgets.QWidget(self.tab)
        self.widget_27.setGeometry(QtCore.QRect(70, 470, 593, 38))
        self.widget_27.setStyleSheet("background: black;\n"
"border-radius: 12px;")
        self.widget_27.setObjectName("widget_27")
        self.horizontalLayout_65 = QtWidgets.QHBoxLayout(self.widget_27)
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        self.widget_28 = QtWidgets.QWidget(self.widget_27)
        self.widget_28.setObjectName("widget_28")
        self.horizontalLayout_66 = QtWidgets.QHBoxLayout(self.widget_28)
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName("horizontalLayout_66")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.widget_28)
        self.lineEdit_17.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_17.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_17.setStyleSheet("background: white;\n"
"border: transparent;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"padding-left: 4px;\n"
"padding-bottom: 2px;")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.horizontalLayout_66.addWidget(self.lineEdit_17)
        self.pushButton_21 = QtWidgets.QPushButton(self.widget_28)
        self.pushButton_21.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_21.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    padding-right: 2px;\n"
"    padding-top: 1px;\n"
"    padding-bottom: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {    \n"
"    background-color: rgba(255, 255, 255, 200);\n"
"}\n"
"\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}")
        self.pushButton_21.setText("")
        self.pushButton_21.setIcon(icon2)
        self.pushButton_21.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_66.addWidget(self.pushButton_21)
        self.horizontalLayout_65.addWidget(self.widget_28)
        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setGeometry(QtCore.QRect(70, 410, 471, 21))
        self.label_27.setStyleSheet("background-color: #ababab;")
        self.label_27.setObjectName("label_27")
        self.tabWidget.addTab(self.tab, "")
        self.sidebar = QtWidgets.QWidget(self.splitter)
        self.sidebar.setObjectName("sidebar")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.sidebar)
        self.verticalLayout_10.setContentsMargins(0, 20, 0, 0)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.sidebar)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_10.addWidget(self.label_13)
        self.logViewBox = QtWidgets.QTextEdit(self.sidebar)
        self.logViewBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.logViewBox.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.logViewBox.setReadOnly(True)
        self.logViewBox.setObjectName("logViewBox")
        self.verticalLayout_10.addWidget(self.logViewBox)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: #3e4348;")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.horizontalSlider.valueChanged['int'].connect(self.label_8.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.baseLayer_1.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.baseLayer_1.setTitle(_translate("MainWindow", "Quick Start"))
        self.textBrowser_p1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Valid query format: </span><span style=\" font-weight:600; color:#ffffff;\">sample</span><span style=\" font-weight:600; color:#ff6969;\">*</span><span style=\" font-weight:600; color:#ffffff;\">,</span><span style=\" color:#ffffff;\"> keyword1, keyword2, ... </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; color:#ff6969;\">    </span><span style=\" font-size:6pt; font-weight:600; color:#ff6969;\">*required</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Available keywords shown in dropdown. Keywords are connected by boolean operators (AND, OR, NOT). Default is AND.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">ex.  </span><span style=\" color:#00dfa4;\">spliceosome AND resolution:[2 TO 4]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">ex.  </span><span style=\" color:#00dfa4;\">(spliceosome OR ribonucleoprotein) AND NOT human AND xref_UNIPROTKB:[* TO *]</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#00dfa4;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.ebi.ac.uk/emdb/documentation/search\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; text-decoration: underline; color:#0000ff;\">https://www.ebi.ac.uk/emdb/documentation/search</span></a></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Query [i in circle that links to https://www.ebi.ac.uk/emdb/documentation/search]"))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">Valid query format: </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#000000;\">sample</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#ff6969;\">*</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#000000;\">,</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\"> keyword1, keyword2, ... <br/></span><span style=\" font-family:\'Segoe UI\'; font-size:6pt; font-weight:600; color:#ff6969;\">*required</span></p><p><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">Available keywords shown in dropdown. Keywords are connected by boolean operators (AND, OR, NOT). Default is AND.<br/><br/>ex. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#00007f;\">spliceosome AND resolution:[2 TO 4]<br/></span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">ex. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#00007f;\">(spliceosome OR ribonucleoprotein) AND NOT human AND xref_UNIPROTKB:[* TO *]</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "query"))
        self.pushButton_p1_2.setText(_translate("MainWindow", "preview query"))
        self.label_5.setText(_translate("MainWindow", "Refinement         -->"))
        self.label_6.setText(_translate("MainWindow", "Labels"))
        self.pushButton_2.setText(_translate("MainWindow", "refine options"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>CHANGE THIS NAME</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Label manager"))
        self.label_3.setText(_translate("MainWindow", "Generate Dataset"))
        self.lineEdit_p1.setPlaceholderText(_translate("MainWindow", "save location"))
        self.pushButton_p1_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">this is limiting the window\'s thickness when shrinking btw, prob a better way to go about sizepolicys</span></p></body></html>"))
        self.pushButton_p1_3.setText(_translate("MainWindow", "Generate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page1), _translate("MainWindow", "Quick Start"))
        self.baseLayer_2.setTitle(_translate("MainWindow", "Fetch Sample Info"))
        self.B_enterQuery.setTitle(_translate("MainWindow", "Enter a Query"))
        self.pushButton_p2_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">this is limiting the window\'s thickness when shrinking btw, prob a better way to go about sizepolicys</span></p></body></html>"))
        self.pushButton_p2_2.setText(_translate("MainWindow", "Download CSV"))
        self.label_4.setText(_translate("MainWindow", "TextLabel (indent this by adding a widget)"))
        self.lineEdit_p2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">Valid query format: </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#000000;\">sample</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#ff6969;\">*</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#000000;\">,</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\"> keyword1, keyword2, ... <br/></span><span style=\" font-family:\'Segoe UI\'; font-size:6pt; font-weight:600; color:#ff6969;\">*required</span></p><p><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">Available keywords shown in dropdown. Keywords are connected by boolean operators (AND, OR, NOT). Default is AND.<br/><br/>ex. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#00007f;\">spliceosome AND resolution:[2 TO 4]<br/></span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">ex. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#00007f;\">(spliceosome OR ribonucleoprotein) AND NOT human AND xref_UNIPROTKB:[* TO *]</span></p></body></html>"))
        self.lineEdit_p2.setPlaceholderText(_translate("MainWindow", "save location"))
        self.textBrowser_p2_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Valid query format: </span><span style=\" font-weight:600; color:#000000;\">sample</span><span style=\" font-weight:600; color:#ff6969;\">*</span><span style=\" font-weight:600; color:#000000;\">,</span><span style=\" color:#000000;\"> keyword1, keyword2, ... </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; color:#ff6969;\">    </span><span style=\" font-size:6pt; font-weight:600; color:#ff6969;\">*required</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Keywords are connected by boolean operators (AND, OR, NOT). Default is AND.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.ebi.ac.uk/emdb/documentation/search\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; text-decoration: underline; color:#0000ff;\">More info.</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">ex.</span><span style=\" color:#007c82;\">  </span><span style=\" color:#00007f;\">spliceosome AND resolution:[2 TO 4]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">ex.  </span><span style=\" color:#00007f;\">(spliceosome OR ribonucleoprotein) AND NOT human AND xref_UNIPROTKB:[* TO *]</span></p></body></html>"))
        self.label_p2.setText(_translate("MainWindow", "Query"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "[sample] AND [range_keyword: x TO y] AND [keyword]"))
        self.lineEdit_12.setText(_translate("MainWindow", "new fancy search bar (tweak border width under qwidget\'s layout props, and height via maxHeight for lineedit AND btn)"))
        self.textBrowser_p2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:696; color:#616161;\">This step generates a sample information file [.csv] from EMDB. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:696; color:#616161;\">If you already have a .csv file with the following columns, you can </span><span style=\" font-weight:696; color:#0000ff;\">skip</span><span style=\" font-weight:696; color:#616161;\"> this step.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; font-weight:696; color:#616161;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline; color:#616161;\">Sample info columns:</span><span style=\" color:#616161;\"> emdb_id, resolution, fitted_pdbs, </span><span style=\" color:#b9b9b9;\">xref_UNIPROTKB, xref_ALPHAFOLD, qscore</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page2), _translate("MainWindow", "Query"))
        self.baseLayer_3.setTitle(_translate("MainWindow", "Preprocessing"))
        self.A_chooseCSV.setTitle(_translate("MainWindow", "Choose File (from page 1 or your own)"))
        self.lineEdit_p3.setToolTip(_translate("MainWindow", "type or browse (note to self: check that file exists, if not spit the error out to the statusbar)"))
        self.lineEdit_p3.setPlaceholderText(_translate("MainWindow", "query file (*.csv)"))
        self.pushButton_p3.setToolTip(_translate("MainWindow", "browse or type"))
        self.B_refineCSV.setTitle(_translate("MainWindow", "Refine query"))
        self.similaritySpinBox.setSuffix(_translate("MainWindow", "%"))
        self.mapModelFitnessSpinBox.setSuffix(_translate("MainWindow", "%"))
        self.similarityLabel.setText(_translate("MainWindow", "Similarity:"))
        self.mapModelFitnessLabel.setText(_translate("MainWindow", "Map Model Fitness:"))
        self.qScoreSpinBox.setSuffix(_translate("MainWindow", "%"))
        self.qScoreLabel.setText(_translate("MainWindow", "QScore:"))
        self.lineEdit_p3_2.setText(_translate("MainWindow", "might remove this whole row"))
        self.lineEdit_p3_2.setPlaceholderText(_translate("MainWindow", "CSV filepath"))
        self.pushButton_p3_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select a CSV file first.</p></body></html>"))
        self.pushButton_p3_3.setText(_translate("MainWindow", "Open CSV editor"))
        self.pushButton_p3_4.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">this is limiting the window\'s thickness when shrinking btw, prob a better way to go about sizepolicys</span></p></body></html>"))
        self.pushButton_p3_4.setText(_translate("MainWindow", "Download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page3), _translate("MainWindow", "Preprocess"))
        self.baseLayer_4.setTitle(_translate("MainWindow", "Generate Dataset"))
        self.A_datasetOptions.setTitle(_translate("MainWindow", "Labels"))
        self.addgroup_btn.setText(_translate("MainWindow", "add group"))
        self.addlabel_btn.setText(_translate("MainWindow", "add label"))
        self.A1_featureLabels.setTitle(_translate("MainWindow", "Labels:"))
        self.treeWidget_p4.headerItem().setText(1, _translate("MainWindow", "2ndary struct"))
        self.treeWidget_p4.headerItem().setText(2, _translate("MainWindow", "residues"))
        self.treeWidget_p4.headerItem().setText(3, _translate("MainWindow", "atoms"))
        __sortingEnabled = self.treeWidget_p4.isSortingEnabled()
        self.treeWidget_p4.setSortingEnabled(False)
        self.treeWidget_p4.topLevelItem(0).setText(0, _translate("MainWindow", "Group 1"))
        self.treeWidget_p4.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Label 1"))
        self.treeWidget_p4.topLevelItem(0).child(0).setText(1, _translate("MainWindow", "protein - helix"))
        self.treeWidget_p4.topLevelItem(0).child(0).setText(2, _translate("MainWindow", "all"))
        self.treeWidget_p4.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Label 2"))
        self.treeWidget_p4.topLevelItem(0).child(1).setText(1, _translate("MainWindow", "protein - sheet"))
        self.treeWidget_p4.topLevelItem(1).setText(0, _translate("MainWindow", "Group 2"))
        self.treeWidget_p4.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Label 1"))
        self.treeWidget_p4.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "Label 2"))
        self.treeWidget_p4.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "Label 3"))
        self.treeWidget_p4.topLevelItem(1).child(3).setText(0, _translate("MainWindow", "Label 4"))
        self.treeWidget_p4.topLevelItem(1).child(4).setText(0, _translate("MainWindow", "Label 5"))
        self.treeWidget_p4.topLevelItem(2).setText(0, _translate("MainWindow", "Group 3"))
        self.treeWidget_p4.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "Label 1"))
        self.treeWidget_p4.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "Label 2"))
        self.treeWidget_p4.setSortingEnabled(__sortingEnabled)
        self.label_p4.setText(_translate("MainWindow", "Cube size:"))
        self.lineEdit_p4.setText(_translate("MainWindow", "64"))
        self.label_p4_2.setText(_translate("MainWindow", "^3"))
        self.label_10.setText(_translate("MainWindow", "Training:"))
        self.spinBox.setSuffix(_translate("MainWindow", "%"))
        self.label_11.setText(_translate("MainWindow", "Testing:"))
        self.spinBox_2.setSuffix(_translate("MainWindow", "%"))
        self.label_12.setText(_translate("MainWindow", "Validation:"))
        self.spinBox_3.setSuffix(_translate("MainWindow", "%"))
        self.pushButton_p4_2.setText(_translate("MainWindow", "Generate Dataset"))
        self.lineEdit_p1_2.setText(_translate("MainWindow", "fix the alignment, shit looks ass (also consider renaming this pg\'s tab to \"Dataset\""))
        self.lineEdit_p1_2.setPlaceholderText(_translate("MainWindow", "*.csv of downloaded models"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page4), _translate("MainWindow", "Generate Dataset"))
        self.option1Label_2.setText(_translate("MainWindow", "option 1"))
        self.option2Label.setText(_translate("MainWindow", "option 2"))
        self.option3Label.setText(_translate("MainWindow", "option 3"))
        self.option4Label.setText(_translate("MainWindow", "option 4"))
        self.option5Label.setText(_translate("MainWindow", "option 5"))
        self.doubleSpinBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>uses qscore</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "map quality"))
        self.adfasfLabel.setText(_translate("MainWindow", "adfasf"))
        self.label_7.setText(_translate("MainWindow", "Slider"))
        self.label_9.setText(_translate("MainWindow", "example slider"))
        self.label_8.setText(_translate("MainWindow", "10"))
        self.label_26.setText(_translate("MainWindow", "text for testing maxLength (based on character count). Not perfect tho b/c dif charas have dif width (capital W widest)"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "abcdefghijklmnopqrstuvwxyz\n"
"maxLength: 100\n"
"maxLength: 103\n"
"these values dont mean anything anymore cuz changed widget width\n"
"disabled currently (well technically 16 bit INT_MAX)"))
        self.lineEdit_3.setText(_translate("MainWindow", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuv"))
        self.label_28.setText(_translate("MainWindow", "↓ explicit max height                 THIS is the FINAL version btw (rename the outer widget to smth good)"))
        self.lineEdit_8.setText(_translate("MainWindow", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy"))
        self.label_14.setText(_translate("MainWindow", "↓ frameless (lineedit and button have same vertical sizepolicy in designer)"))
        self.lineEdit_9.setText(_translate("MainWindow", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy"))
        self.label_29.setText(_translate("MainWindow", "↓ explicit max AND min height. Also added an extra empty widget layer btwn lineedit and border"))
        self.lineEdit_14.setText(_translate("MainWindow", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.lineEdit_16.setText(_translate("MainWindow", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy"))
        self.lineEdit_17.setText(_translate("MainWindow", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy"))
        self.label_27.setText(_translate("MainWindow", "these 2 are just for templates (missing/empty base widget so may look weird in python)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "TEST"))
        self.label_13.setText(_translate("MainWindow", "Logs"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
