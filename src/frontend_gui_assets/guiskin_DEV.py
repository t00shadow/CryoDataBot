# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataset_gen_tool_v6.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 784)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 120))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setStyleSheet("")
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
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_7.addItem(spacerItem, 0, 0, 1, 1)
        self.A_quickStart = QtWidgets.QGroupBox(self.baseLayer_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A1_instructions.sizePolicy().hasHeightForWidth())
        self.A1_instructions.setSizePolicy(sizePolicy)
        self.A1_instructions.setMinimumSize(QtCore.QSize(0, 200))
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_p1.sizePolicy().hasHeightForWidth())
        self.textBrowser_p1.setSizePolicy(sizePolicy)
        self.textBrowser_p1.setMinimumSize(QtCore.QSize(0, 200))
        self.textBrowser_p1.setStyleSheet("background-color: transparent;\n"
"border: transparent;")
        self.textBrowser_p1.setObjectName("textBrowser_p1")
        self.horizontalLayout_11.addWidget(self.textBrowser_p1)
        self.verticalLayout_2.addWidget(self.A1_instructions)
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
        self.A4_queryBox.setObjectName("A4_queryBox")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.A4_queryBox)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_2.addWidget(self.A4_queryBox)
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
        self.pushButton_p1.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_p1.setStyleSheet("/*border-image: url(:/icons/browsefilesicon.png);*/\n"
"background-color: white;\n"
"border-radius: 6;")
        self.pushButton_p1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/browsefilesicon_zoomed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_p1.setIcon(icon)
        self.pushButton_p1.setObjectName("pushButton_p1")
        self.horizontalLayout_41.addWidget(self.pushButton_p1)
        self.verticalLayout_2.addWidget(self.A2_savePath)
        self.A3_previewQuery = QtWidgets.QWidget(self.A_quickStart)
        self.A3_previewQuery.setObjectName("A3_previewQuery")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.A3_previewQuery)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_p1_2 = QtWidgets.QPushButton(self.A3_previewQuery)
        self.pushButton_p1_2.setObjectName("pushButton_p1_2")
        self.horizontalLayout.addWidget(self.pushButton_p1_2)
        self.verticalLayout_2.addWidget(self.A3_previewQuery)
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem2)
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
        font.setWeight(75)
        self.pushButton_p1_3.setFont(font)
        self.pushButton_p1_3.setStyleSheet("QPushButton {\n"
"    background: #81cfd8;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 6px solid transparent;\n"
"}")
        self.pushButton_p1_3.setObjectName("pushButton_p1_3")
        self.horizontalLayout_14.addWidget(self.pushButton_p1_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.A5_generateDataset)
        self.gridLayout_7.addWidget(self.A_quickStart, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_7.addItem(spacerItem4, 2, 0, 1, 1)
        self.gridLayout_8.addWidget(self.baseLayer_1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.page1, "")
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page2)
        self.gridLayout_2.setObjectName("gridLayout_2")
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
"    padding-left: 10px;\n"
"}\n"
"\n"
"/*\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"*/")
        self.baseLayer_2.setObjectName("baseLayer_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.baseLayer_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
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
        self.B_enterQuery.setObjectName("B_enterQuery")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.B_enterQuery)
        self.verticalLayout.setObjectName("verticalLayout")
        self.B1_instructions = QtWidgets.QGroupBox(self.B_enterQuery)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B1_instructions.sizePolicy().hasHeightForWidth())
        self.B1_instructions.setSizePolicy(sizePolicy)
        self.B1_instructions.setMinimumSize(QtCore.QSize(0, 124))
        self.B1_instructions.setMaximumSize(QtCore.QSize(16777215, 150))
        self.B1_instructions.setStyleSheet("\n"
"QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}\n"
"")
        self.B1_instructions.setTitle("")
        self.B1_instructions.setObjectName("B1_instructions")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.B1_instructions)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser_p2_2 = QtWidgets.QTextBrowser(self.B1_instructions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_p2_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_p2_2.setSizePolicy(sizePolicy)
        self.textBrowser_p2_2.setMinimumSize(QtCore.QSize(0, 180))
        self.textBrowser_p2_2.setStyleSheet("background-color: transparent;\n"
"border: transparent;")
        self.textBrowser_p2_2.setObjectName("textBrowser_p2_2")
        self.horizontalLayout_2.addWidget(self.textBrowser_p2_2)
        self.verticalLayout.addWidget(self.B1_instructions)
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
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_p2 = QtWidgets.QLabel(self.B2_queryBox)
        self.label_p2.setObjectName("label_p2")
        self.verticalLayout_4.addWidget(self.label_p2)
        self.verticalLayout.addWidget(self.B2_queryBox)
        self.B1_csvFilepath = QtWidgets.QGroupBox(self.B_enterQuery)
        self.B1_csvFilepath.setTitle("")
        self.B1_csvFilepath.setObjectName("B1_csvFilepath")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.B1_csvFilepath)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.lineEdit_p2 = QtWidgets.QLineEdit(self.B1_csvFilepath)
        self.lineEdit_p2.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_p2.setText("")
        self.lineEdit_p2.setDragEnabled(False)
        self.lineEdit_p2.setClearButtonEnabled(True)
        self.lineEdit_p2.setObjectName("lineEdit_p2")
        self.horizontalLayout_40.addWidget(self.lineEdit_p2)
        self.pushButton_p2 = QtWidgets.QPushButton(self.B1_csvFilepath)
        self.pushButton_p2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_p2.setStyleSheet("/*border-image: url(:/icons/browsefilesicon.png);*/\n"
"background-color: white;\n"
"border-radius: 6;")
        self.pushButton_p2.setText("")
        self.pushButton_p2.setIcon(icon)
        self.pushButton_p2.setObjectName("pushButton_p2")
        self.horizontalLayout_40.addWidget(self.pushButton_p2)
        self.verticalLayout.addWidget(self.B1_csvFilepath)
        self.B3_downloadCSV = QtWidgets.QGroupBox(self.B_enterQuery)
        self.B3_downloadCSV.setStyleSheet("\n"
"QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}\n"
"")
        self.B3_downloadCSV.setTitle("")
        self.B3_downloadCSV.setObjectName("B3_downloadCSV")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.B3_downloadCSV)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.pushButton_p2_2 = QtWidgets.QPushButton(self.B3_downloadCSV)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p2_2.sizePolicy().hasHeightForWidth())
        self.pushButton_p2_2.setSizePolicy(sizePolicy)
        self.pushButton_p2_2.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_p2_2.setFont(font)
        self.pushButton_p2_2.setStyleSheet("QPushButton {\n"
"    background: #6668ad;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 6px solid transparent;\n"
"}")
        self.pushButton_p2_2.setObjectName("pushButton_p2_2")
        self.horizontalLayout_4.addWidget(self.pushButton_p2_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout.addWidget(self.B3_downloadCSV)
        self.gridLayout_3.addWidget(self.B_enterQuery, 2, 0, 1, 1)
        self.A_notesForUser = QtWidgets.QGroupBox(self.baseLayer_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A_notesForUser.sizePolicy().hasHeightForWidth())
        self.A_notesForUser.setSizePolicy(sizePolicy)
        self.A_notesForUser.setMinimumSize(QtCore.QSize(0, 0))
        self.A_notesForUser.setMaximumSize(QtCore.QSize(16777215, 120))
        self.A_notesForUser.setBaseSize(QtCore.QSize(0, 150))
        self.A_notesForUser.setStyleSheet("QGroupBox#A_notesForUser {\n"
"    border: gray;\n"
"    padding-top: 10px;\n"
"}")
        self.A_notesForUser.setTitle("")
        self.A_notesForUser.setObjectName("A_notesForUser")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.A_notesForUser)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textBrowser_p2 = QtWidgets.QTextBrowser(self.A_notesForUser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_p2.sizePolicy().hasHeightForWidth())
        self.textBrowser_p2.setSizePolicy(sizePolicy)
        self.textBrowser_p2.setMinimumSize(QtCore.QSize(0, 150))
        self.textBrowser_p2.setMaximumSize(QtCore.QSize(16777215, 120))
        self.textBrowser_p2.setBaseSize(QtCore.QSize(0, 150))
        self.textBrowser_p2.setStyleSheet("background-color: transparent;\n"
"border: transparent;")
        self.textBrowser_p2.setObjectName("textBrowser_p2")
        self.gridLayout_4.addWidget(self.textBrowser_p2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.A_notesForUser, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.baseLayer_2, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 1, 0, 1, 1)
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
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_6.addItem(spacerItem8, 0, 0, 1, 1)
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
        self.pushButton_p3.setIcon(icon)
        self.pushButton_p3.setObjectName("pushButton_p3")
        self.horizontalLayout_19.addWidget(self.pushButton_p3)
        self.verticalLayout_19.addWidget(self.A2_csvFilepath)
        self.gridLayout_6.addWidget(self.A_chooseCSV, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem9, 2, 0, 1, 1)
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
"    color: gray;\n"
"}\n"
"\n"
"\n"
"QGroupBox {\n"
"    border: transparent;\n"
"}\n"
"")
        self.B_refineCSV.setObjectName("B_refineCSV")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.B_refineCSV)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.B1_dragAndDrop = QtWidgets.QGroupBox(self.B_refineCSV)
        self.B1_dragAndDrop.setStyleSheet("")
        self.B1_dragAndDrop.setTitle("")
        self.B1_dragAndDrop.setObjectName("B1_dragAndDrop")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.B1_dragAndDrop)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.verticalLayout_24.addWidget(self.B1_dragAndDrop)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.option1Label = QtWidgets.QLabel(self.B_refineCSV)
        self.option1Label.setObjectName("option1Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.option1Label)
        self.option1LineEdit = QtWidgets.QLineEdit(self.B_refineCSV)
        self.option1LineEdit.setObjectName("option1LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.option1LineEdit)
        self.verticalLayout_24.addLayout(self.formLayout)
        self.pushButton_p3_4 = QtWidgets.QPushButton(self.B_refineCSV)
        self.pushButton_p3_4.setObjectName("pushButton_p3_4")
        self.verticalLayout_24.addWidget(self.pushButton_p3_4)
        self.pushButton_p3_5 = QtWidgets.QPushButton(self.B_refineCSV)
        self.pushButton_p3_5.setObjectName("pushButton_p3_5")
        self.verticalLayout_24.addWidget(self.pushButton_p3_5)
        self.pushButton_p3_6 = QtWidgets.QPushButton(self.B_refineCSV)
        self.pushButton_p3_6.setObjectName("pushButton_p3_6")
        self.verticalLayout_24.addWidget(self.pushButton_p3_6)
        self.B2_csvFilepath = QtWidgets.QGroupBox(self.B_refineCSV)
        self.B2_csvFilepath.setTitle("")
        self.B2_csvFilepath.setObjectName("B2_csvFilepath")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.B2_csvFilepath)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.lineEdit_p3_2 = QtWidgets.QLineEdit(self.B2_csvFilepath)
        self.lineEdit_p3_2.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_p3_2.setText("")
        self.lineEdit_p3_2.setDragEnabled(False)
        self.lineEdit_p3_2.setClearButtonEnabled(True)
        self.lineEdit_p3_2.setObjectName("lineEdit_p3_2")
        self.horizontalLayout_39.addWidget(self.lineEdit_p3_2)
        self.pushButton_p3_2 = QtWidgets.QPushButton(self.B2_csvFilepath)
        self.pushButton_p3_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_p3_2.setStyleSheet("/*border-image: url(:/icons/browsefilesicon.png);*/\n"
"background-color: white;\n"
"border-radius: 6;")
        self.pushButton_p3_2.setText("")
        self.pushButton_p3_2.setIcon(icon)
        self.pushButton_p3_2.setObjectName("pushButton_p3_2")
        self.horizontalLayout_39.addWidget(self.pushButton_p3_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem10)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/external-link-512.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_p3_3.setIcon(icon1)
        self.pushButton_p3_3.setObjectName("pushButton_p3_3")
        self.horizontalLayout_39.addWidget(self.pushButton_p3_3)
        self.verticalLayout_24.addWidget(self.B2_csvFilepath)
        self.gridLayout_6.addWidget(self.B_refineCSV, 3, 0, 1, 1)
        self.gridLayout_12.addWidget(self.baseLayer_3, 0, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem11, 1, 0, 1, 1)
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
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_5.addItem(spacerItem12, 0, 0, 1, 1)
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
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.A_datasetOptions)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.A1_featureLabels = QtWidgets.QGroupBox(self.A_datasetOptions)
        self.A1_featureLabels.setObjectName("A1_featureLabels")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.A1_featureLabels)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.treeWidget_p4 = QtWidgets.QTreeWidget(self.A1_featureLabels)
        self.treeWidget_p4.setStyleSheet("QTreeWidget::item {\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    background-color: #F0F0F0;\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background-color: #E0E0E0;\n"
"}")
        self.treeWidget_p4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.treeWidget_p4.setAlternatingRowColors(True)
        self.treeWidget_p4.setAnimated(True)
        self.treeWidget_p4.setObjectName("treeWidget_p4")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_p4)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_p4)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_p4)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.horizontalLayout_9.addWidget(self.treeWidget_p4)
        self.verticalLayout_14.addWidget(self.A1_featureLabels)
        self.pushButton_p4_3 = QtWidgets.QPushButton(self.A_datasetOptions)
        self.pushButton_p4_3.setObjectName("pushButton_p4_3")
        self.verticalLayout_14.addWidget(self.pushButton_p4_3)
        self.A2_cubeSize = QtWidgets.QGroupBox(self.A_datasetOptions)
        self.A2_cubeSize.setTitle("")
        self.A2_cubeSize.setObjectName("A2_cubeSize")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.A2_cubeSize)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_p4 = QtWidgets.QLabel(self.A2_cubeSize)
        self.label_p4.setObjectName("label_p4")
        self.horizontalLayout_10.addWidget(self.label_p4)
        self.lineEdit_p4 = QtWidgets.QLineEdit(self.A2_cubeSize)
        self.lineEdit_p4.setObjectName("lineEdit_p4")
        self.horizontalLayout_10.addWidget(self.lineEdit_p4)
        self.label_p4_2 = QtWidgets.QLabel(self.A2_cubeSize)
        self.label_p4_2.setObjectName("label_p4_2")
        self.horizontalLayout_10.addWidget(self.label_p4_2)
        self.lineEdit_p4_2 = QtWidgets.QLineEdit(self.A2_cubeSize)
        self.lineEdit_p4_2.setObjectName("lineEdit_p4_2")
        self.horizontalLayout_10.addWidget(self.lineEdit_p4_2)
        self.label_p4_3 = QtWidgets.QLabel(self.A2_cubeSize)
        self.label_p4_3.setObjectName("label_p4_3")
        self.horizontalLayout_10.addWidget(self.label_p4_3)
        self.lineEdit_p4_3 = QtWidgets.QLineEdit(self.A2_cubeSize)
        self.lineEdit_p4_3.setObjectName("lineEdit_p4_3")
        self.horizontalLayout_10.addWidget(self.lineEdit_p4_3)
        spacerItem13 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem13)
        self.verticalLayout_14.addWidget(self.A2_cubeSize)
        self.A3_advancedOptions = QtWidgets.QGroupBox(self.A_datasetOptions)
        self.A3_advancedOptions.setTitle("")
        self.A3_advancedOptions.setObjectName("A3_advancedOptions")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.A3_advancedOptions)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_p4 = QtWidgets.QPushButton(self.A3_advancedOptions)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.pushButton_p4.setFont(font)
        self.pushButton_p4.setStyleSheet("QPushButton {\n"
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
        self.pushButton_p4.setIcon(icon)
        self.pushButton_p4.setCheckable(False)
        self.pushButton_p4.setObjectName("pushButton_p4")
        self.horizontalLayout_5.addWidget(self.pushButton_p4)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.verticalLayout_14.addWidget(self.A3_advancedOptions)
        self.A4_generateDataset = QtWidgets.QGroupBox(self.A_datasetOptions)
        self.A4_generateDataset.setTitle("")
        self.A4_generateDataset.setObjectName("A4_generateDataset")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.A4_generateDataset)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
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
        font.setWeight(75)
        self.pushButton_p4_2.setFont(font)
        self.pushButton_p4_2.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background: #6668ad;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 6px solid transparent;\n"
"}")
        self.pushButton_p4_2.setObjectName("pushButton_p4_2")
        self.horizontalLayout_6.addWidget(self.pushButton_p4_2)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem16)
        self.verticalLayout_14.addWidget(self.A4_generateDataset)
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
        self.verticalLayout_14.addWidget(self.A5_progressDisplay)
        self.gridLayout_5.addWidget(self.A_datasetOptions, 1, 0, 1, 1)
        self.verticalLayout_18.addWidget(self.baseLayer_4)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem17)
        self.tabWidget.addTab(self.page4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.baseLayer_1.setTitle(_translate("MainWindow", "Quick Start"))
        self.textBrowser_p1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#ffffff;\">A valid query is a sample name followed by keywords. Available keywords shown in dropdown. Keywords are connected by boolean operators (AND, OR, NOT). Default is AND.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#ffffff;\">ex. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#00dfa4;\">spliceosome AND resolution:[1 TO 3]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#ffffff;\">ex. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#00dfa4;\">spliceosome OR ribosome</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#ffffff;\">ex. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#00dfa4;\">NOT spliceosome</span></p></body></html>"))
        self.A4_queryBox.setTitle(_translate("MainWindow", "Query"))
        self.lineEdit_p1.setPlaceholderText(_translate("MainWindow", "save path"))
        self.pushButton_p1_2.setText(_translate("MainWindow", "preview query"))
        self.pushButton_p1_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">this is limiting the window\'s thickness when shrinking btw, prob a better way to go about sizepolicys</span></p></body></html>"))
        self.pushButton_p1_3.setText(_translate("MainWindow", "Generate Dataset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page1), _translate("MainWindow", "Quick Start"))
        self.baseLayer_2.setTitle(_translate("MainWindow", "Query > CSV file"))
        self.B_enterQuery.setTitle(_translate("MainWindow", "Enter a query"))
        self.textBrowser_p2_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">Type in sample name followed by keywords. Common keywords available in dropdown. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">Hit </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:696; color:#000000;\">return</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\"> after each keyword. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-style:italic; color:#000000;\">Text not in the form of a tag (hitting return creates a tag) will NOT be read.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">ex. spliceosome </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#000000;\">[return]</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\"> resolution:2-5 </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#000000;\">[return]</span></p></body></html>"))
        self.label_p2.setText(_translate("MainWindow", "Query"))
        self.lineEdit_p2.setPlaceholderText(_translate("MainWindow", "save path"))
        self.pushButton_p2_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">this is limiting the window\'s thickness when shrinking btw, prob a better way to go about sizepolicys</span></p></body></html>"))
        self.pushButton_p2_2.setText(_translate("MainWindow", "Download CSV"))
        self.textBrowser_p2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:696; color:#616161;\">If you already have a CSV file, go to the next page.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:6pt; font-weight:696; color:#616161;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; text-decoration: underline; color:#616161;\">CSV file requirements (columns):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#616161;\">    emdb_id, resolution, fitted_pdbs, xref_UNIPROTKB, xref_ALPHAFOLD<br /></span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-style:italic; color:#616161;\">  </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-style:italic; color:#0000ff;\">*CSV files downloaded from EMDB</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page2), _translate("MainWindow", "Make Query"))
        self.baseLayer_3.setTitle(_translate("MainWindow", "Choose/Refine"))
        self.A_chooseCSV.setTitle(_translate("MainWindow", "Choose File (from page 1 or your own)"))
        self.lineEdit_p3.setToolTip(_translate("MainWindow", "type or browse (note to self: check that file exists, if not spit the error out to the statusbar)"))
        self.lineEdit_p3.setPlaceholderText(_translate("MainWindow", "CSV filepath"))
        self.pushButton_p3.setToolTip(_translate("MainWindow", "browse or type"))
        self.B_refineCSV.setTitle(_translate("MainWindow", "Refine file (Optional)"))
        self.option1Label.setText(_translate("MainWindow", "option1"))
        self.pushButton_p3_4.setText(_translate("MainWindow", "refine fxn 1"))
        self.pushButton_p3_5.setText(_translate("MainWindow", "..."))
        self.pushButton_p3_6.setText(_translate("MainWindow", "..."))
        self.lineEdit_p3_2.setPlaceholderText(_translate("MainWindow", "CSV filepath"))
        self.pushButton_p3_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select a CSV file first.</p></body></html>"))
        self.pushButton_p3_3.setText(_translate("MainWindow", "Open CSV editor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page3), _translate("MainWindow", "Choose File/Refine"))
        self.baseLayer_4.setTitle(_translate("MainWindow", "Generate Dataset"))
        self.A_datasetOptions.setTitle(_translate("MainWindow", "Dataset options"))
        self.A1_featureLabels.setTitle(_translate("MainWindow", "Labels:"))
        self.treeWidget_p4.headerItem().setText(0, _translate("MainWindow", "Type (REMOVE THIS AND PUT IN NEW WINDOW FOR POPUP)"))
        __sortingEnabled = self.treeWidget_p4.isSortingEnabled()
        self.treeWidget_p4.setSortingEnabled(False)
        self.treeWidget_p4.topLevelItem(0).setText(0, _translate("MainWindow", "Protein"))
        self.treeWidget_p4.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Residues"))
        self.treeWidget_p4.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_p4.topLevelItem(0).child(0).child(1).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_p4.topLevelItem(0).child(0).child(2).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_p4.topLevelItem(0).child(0).child(3).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_p4.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Key Atoms"))
        self.treeWidget_p4.topLevelItem(1).setText(0, _translate("MainWindow", "DNA"))
        self.treeWidget_p4.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Residues"))
        self.treeWidget_p4.topLevelItem(1).child(0).child(0).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_p4.topLevelItem(1).child(0).child(1).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_p4.topLevelItem(1).child(0).child(2).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_p4.topLevelItem(1).child(0).child(3).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_p4.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "Key Atoms"))
        self.treeWidget_p4.topLevelItem(2).setText(0, _translate("MainWindow", "RNA"))
        self.treeWidget_p4.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "Residues"))
        self.treeWidget_p4.topLevelItem(2).child(0).child(0).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_p4.topLevelItem(2).child(0).child(1).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_p4.topLevelItem(2).child(0).child(2).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_p4.topLevelItem(2).child(0).child(3).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_p4.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "Key Atoms"))
        self.treeWidget_p4.setSortingEnabled(__sortingEnabled)
        self.pushButton_p4_3.setText(_translate("MainWindow", "add a group of labels (REMOVE TREE WIDGET, will be popup)"))
        self.label_p4.setText(_translate("MainWindow", "Cube size:"))
        self.lineEdit_p4.setText(_translate("MainWindow", "64"))
        self.label_p4_2.setText(_translate("MainWindow", "x"))
        self.lineEdit_p4_2.setText(_translate("MainWindow", "64"))
        self.label_p4_3.setText(_translate("MainWindow", "x"))
        self.lineEdit_p4_3.setText(_translate("MainWindow", "64"))
        self.pushButton_p4.setText(_translate("MainWindow", "Advanced options"))
        self.pushButton_p4_2.setText(_translate("MainWindow", "Generate Dataset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page4), _translate("MainWindow", "Generate Dataset"))
import src.frontend_gui_assets.resources_rc as resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
