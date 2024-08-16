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
        MainWindow.resize(593, 784)
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
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget_2.setStyleSheet("")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.baseLayer_4 = QtWidgets.QGroupBox(self.tab)
        self.baseLayer_4.setStyleSheet("QGroupBox#baseLayer_4 {\n"
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
        self.baseLayer_4.setObjectName("baseLayer_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.baseLayer_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem, 2, 0, 1, 1)
        self.B_enterQuery_2 = QtWidgets.QGroupBox(self.baseLayer_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B_enterQuery_2.sizePolicy().hasHeightForWidth())
        self.B_enterQuery_2.setSizePolicy(sizePolicy)
        self.B_enterQuery_2.setStyleSheet("QGroupBox#B_enterQuery_2 {\n"
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
        self.B_enterQuery_2.setTitle("")
        self.B_enterQuery_2.setObjectName("B_enterQuery_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.B_enterQuery_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.B1_instructions_2 = QtWidgets.QGroupBox(self.B_enterQuery_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B1_instructions_2.sizePolicy().hasHeightForWidth())
        self.B1_instructions_2.setSizePolicy(sizePolicy)
        self.B1_instructions_2.setMinimumSize(QtCore.QSize(0, 124))
        self.B1_instructions_2.setStyleSheet("\n"
"QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}\n"
"")
        self.B1_instructions_2.setTitle("")
        self.B1_instructions_2.setObjectName("B1_instructions_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.B1_instructions_2)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.B1_instructions_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_4.sizePolicy().hasHeightForWidth())
        self.textBrowser_4.setSizePolicy(sizePolicy)
        self.textBrowser_4.setStyleSheet("background-color: transparent;\n"
"border: transparent;")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayout_11.addWidget(self.textBrowser_4)
        self.verticalLayout_2.addWidget(self.B1_instructions_2)
        self.B2_queryBox_2 = QtWidgets.QGroupBox(self.B_enterQuery_2)
        self.B2_queryBox_2.setStyleSheet("QGroupBox#B2_queryBox_2{\n"
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
        self.B2_queryBox_2.setObjectName("B2_queryBox_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.B2_queryBox_2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_2.addWidget(self.B2_queryBox_2)
        self.A2_csvFilepath_7 = QtWidgets.QGroupBox(self.B_enterQuery_2)
        self.A2_csvFilepath_7.setTitle("")
        self.A2_csvFilepath_7.setObjectName("A2_csvFilepath_7")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.A2_csvFilepath_7)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.A2_csvFilepath_7)
        self.lineEdit_22.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_22.setText("")
        self.lineEdit_22.setDragEnabled(False)
        self.lineEdit_22.setClearButtonEnabled(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.horizontalLayout_41.addWidget(self.lineEdit_22)
        self.pushButton_31 = QtWidgets.QPushButton(self.A2_csvFilepath_7)
        self.pushButton_31.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_31.setStyleSheet("/*border-image: url(:/icons/browsefilesicon.png);*/\n"
"background-color: white;\n"
"border-radius: 6;")
        self.pushButton_31.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/browsefilesicon_zoomed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_31.setIcon(icon)
        self.pushButton_31.setObjectName("pushButton_31")
        self.horizontalLayout_41.addWidget(self.pushButton_31)
        self.verticalLayout_2.addWidget(self.A2_csvFilepath_7)
        self.B3_downloadCSV_2 = QtWidgets.QGroupBox(self.B_enterQuery_2)
        self.B3_downloadCSV_2.setStyleSheet("\n"
"QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}\n"
"")
        self.B3_downloadCSV_2.setTitle("")
        self.B3_downloadCSV_2.setObjectName("B3_downloadCSV_2")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.B3_downloadCSV_2)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.pushButton_7 = QtWidgets.QPushButton(self.B3_downloadCSV_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background: #81cfd8;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 6px solid transparent;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_14.addWidget(self.pushButton_7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.B3_downloadCSV_2)
        self.gridLayout_7.addWidget(self.B_enterQuery_2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_7.addItem(spacerItem3, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.baseLayer_4, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab, "")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.baseLayer = QtWidgets.QGroupBox(self.page1)
        self.baseLayer.setStyleSheet("QGroupBox#baseLayer {\n"
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
        self.baseLayer.setObjectName("baseLayer")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.baseLayer)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.A_notesForUser = QtWidgets.QGroupBox(self.baseLayer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A_notesForUser.sizePolicy().hasHeightForWidth())
        self.A_notesForUser.setSizePolicy(sizePolicy)
        self.A_notesForUser.setMinimumSize(QtCore.QSize(0, 0))
        self.A_notesForUser.setMaximumSize(QtCore.QSize(16777215, 120))
        self.A_notesForUser.setBaseSize(QtCore.QSize(0, 150))
        self.A_notesForUser.setStyleSheet("QGroupBox#A_notesForUser {\n"
"    border: transparent;\n"
"    padding-top: 10px;\n"
"}")
        self.A_notesForUser.setTitle("")
        self.A_notesForUser.setObjectName("A_notesForUser")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.A_notesForUser)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.A_notesForUser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_5.sizePolicy().hasHeightForWidth())
        self.textBrowser_5.setSizePolicy(sizePolicy)
        self.textBrowser_5.setMinimumSize(QtCore.QSize(0, 120))
        self.textBrowser_5.setMaximumSize(QtCore.QSize(16777215, 120))
        self.textBrowser_5.setBaseSize(QtCore.QSize(0, 150))
        self.textBrowser_5.setStyleSheet("background-color: transparent;\n"
"border: transparent;")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.gridLayout_4.addWidget(self.textBrowser_5, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.A_notesForUser, 0, 0, 1, 1)
        self.B_enterQuery = QtWidgets.QGroupBox(self.baseLayer)
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
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.B1_instructions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_3.sizePolicy().hasHeightForWidth())
        self.textBrowser_3.setSizePolicy(sizePolicy)
        self.textBrowser_3.setStyleSheet("background-color: transparent;\n"
"border: transparent;")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayout_2.addWidget(self.textBrowser_3)
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
        self.label = QtWidgets.QLabel(self.B2_queryBox)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout.addWidget(self.B2_queryBox)
        self.A2_csvFilepath_6 = QtWidgets.QGroupBox(self.B_enterQuery)
        self.A2_csvFilepath_6.setTitle("")
        self.A2_csvFilepath_6.setObjectName("A2_csvFilepath_6")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.A2_csvFilepath_6)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.A2_csvFilepath_6)
        self.lineEdit_21.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_21.setText("")
        self.lineEdit_21.setDragEnabled(False)
        self.lineEdit_21.setClearButtonEnabled(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.horizontalLayout_40.addWidget(self.lineEdit_21)
        self.pushButton_30 = QtWidgets.QPushButton(self.A2_csvFilepath_6)
        self.pushButton_30.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_30.setStyleSheet("/*border-image: url(:/icons/browsefilesicon.png);*/\n"
"background-color: white;\n"
"border-radius: 6;")
        self.pushButton_30.setText("")
        self.pushButton_30.setIcon(icon)
        self.pushButton_30.setObjectName("pushButton_30")
        self.horizontalLayout_40.addWidget(self.pushButton_30)
        self.verticalLayout.addWidget(self.A2_csvFilepath_6)
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
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.pushButton_6 = QtWidgets.QPushButton(self.B3_downloadCSV)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background: #6668ad;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 6px solid transparent;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addWidget(self.B3_downloadCSV)
        self.gridLayout_3.addWidget(self.B_enterQuery, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.baseLayer, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.page1, "")
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page2)
        self.gridLayout_12.setObjectName("gridLayout_12")
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
        self.gridLayout_6 = QtWidgets.QGridLayout(self.baseLayer_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_6.addItem(spacerItem7, 0, 0, 1, 1)
        self.A_selectCSV_2 = QtWidgets.QGroupBox(self.baseLayer_2)
        self.A_selectCSV_2.setStyleSheet("QGroupBox#A_selectCSV_2 {\n"
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
        self.A_selectCSV_2.setObjectName("A_selectCSV_2")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.A_selectCSV_2)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.A1_dragAndDrop_2 = QtWidgets.QGroupBox(self.A_selectCSV_2)
        self.A1_dragAndDrop_2.setTitle("")
        self.A1_dragAndDrop_2.setObjectName("A1_dragAndDrop_2")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.A1_dragAndDrop_2)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_19.addWidget(self.A1_dragAndDrop_2)
        self.A2_csvFilepath_2 = QtWidgets.QGroupBox(self.A_selectCSV_2)
        self.A2_csvFilepath_2.setTitle("")
        self.A2_csvFilepath_2.setObjectName("A2_csvFilepath_2")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.A2_csvFilepath_2)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.A2_csvFilepath_2)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setDragEnabled(False)
        self.lineEdit_10.setClearButtonEnabled(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_19.addWidget(self.lineEdit_10)
        self.pushButton_15 = QtWidgets.QPushButton(self.A2_csvFilepath_2)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_15.setStyleSheet("/*border-image: url(:/icons/browsefilesicon.png);*/\n"
"background-color: white;\n"
"border-radius: 6;")
        self.pushButton_15.setText("")
        self.pushButton_15.setIcon(icon)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_19.addWidget(self.pushButton_15)
        self.verticalLayout_19.addWidget(self.A2_csvFilepath_2)
        self.gridLayout_6.addWidget(self.A_selectCSV_2, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem8, 2, 0, 1, 1)
        self.A_selectCSV_5 = QtWidgets.QGroupBox(self.baseLayer_2)
        self.A_selectCSV_5.setStyleSheet("QGroupBox#A_selectCSV_5 {\n"
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
        self.A_selectCSV_5.setObjectName("A_selectCSV_5")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.A_selectCSV_5)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.A1_dragAndDrop_5 = QtWidgets.QGroupBox(self.A_selectCSV_5)
        self.A1_dragAndDrop_5.setStyleSheet("")
        self.A1_dragAndDrop_5.setTitle("")
        self.A1_dragAndDrop_5.setObjectName("A1_dragAndDrop_5")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.A1_dragAndDrop_5)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.verticalLayout_24.addWidget(self.A1_dragAndDrop_5)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.option1Label = QtWidgets.QLabel(self.A_selectCSV_5)
        self.option1Label.setObjectName("option1Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.option1Label)
        self.option1LineEdit = QtWidgets.QLineEdit(self.A_selectCSV_5)
        self.option1LineEdit.setObjectName("option1LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.option1LineEdit)
        self.verticalLayout_24.addLayout(self.formLayout)
        self.pushButton = QtWidgets.QPushButton(self.A_selectCSV_5)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_24.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.A_selectCSV_5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_24.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.A_selectCSV_5)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_24.addWidget(self.pushButton_3)
        self.A2_csvFilepath_5 = QtWidgets.QGroupBox(self.A_selectCSV_5)
        self.A2_csvFilepath_5.setTitle("")
        self.A2_csvFilepath_5.setObjectName("A2_csvFilepath_5")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.A2_csvFilepath_5)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.A2_csvFilepath_5)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setDragEnabled(False)
        self.lineEdit_12.setClearButtonEnabled(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_39.addWidget(self.lineEdit_12)
        self.pushButton_28 = QtWidgets.QPushButton(self.A2_csvFilepath_5)
        self.pushButton_28.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_28.setStyleSheet("/*border-image: url(:/icons/browsefilesicon.png);*/\n"
"background-color: white;\n"
"border-radius: 6;")
        self.pushButton_28.setText("")
        self.pushButton_28.setIcon(icon)
        self.pushButton_28.setObjectName("pushButton_28")
        self.horizontalLayout_39.addWidget(self.pushButton_28)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem9)
        self.pushButton_29 = QtWidgets.QPushButton(self.A2_csvFilepath_5)
        self.pushButton_29.setStyleSheet("QPushButton {\n"
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
        self.pushButton_29.setIcon(icon1)
        self.pushButton_29.setObjectName("pushButton_29")
        self.horizontalLayout_39.addWidget(self.pushButton_29)
        self.verticalLayout_24.addWidget(self.A2_csvFilepath_5)
        self.gridLayout_6.addWidget(self.A_selectCSV_5, 3, 0, 1, 1)
        self.gridLayout_12.addWidget(self.baseLayer_2, 0, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem10, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.page2, "")
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.page3)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
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
        self.gridLayout_5 = QtWidgets.QGridLayout(self.baseLayer_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_5.addItem(spacerItem11, 0, 0, 1, 1)
        self.B_datasetOptions = QtWidgets.QGroupBox(self.baseLayer_3)
        self.B_datasetOptions.setStyleSheet("QGroupBox#B_datasetOptions {\n"
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
        self.B_datasetOptions.setObjectName("B_datasetOptions")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.B_datasetOptions)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.B1_featureLabels = QtWidgets.QGroupBox(self.B_datasetOptions)
        self.B1_featureLabels.setObjectName("B1_featureLabels")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.B1_featureLabels)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.B1_featureLabels)
        self.treeWidget_2.setStyleSheet("QTreeWidget::item {\n"
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
        self.treeWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.treeWidget_2.setAlternatingRowColors(True)
        self.treeWidget_2.setAnimated(True)
        self.treeWidget_2.setObjectName("treeWidget_2")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.horizontalLayout_9.addWidget(self.treeWidget_2)
        self.verticalLayout_14.addWidget(self.B1_featureLabels)
        self.pushButton_11 = QtWidgets.QPushButton(self.B_datasetOptions)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_14.addWidget(self.pushButton_11)
        self.B2_cubeSize = QtWidgets.QGroupBox(self.B_datasetOptions)
        self.B2_cubeSize.setTitle("")
        self.B2_cubeSize.setObjectName("B2_cubeSize")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.B2_cubeSize)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.B2_cubeSize)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.B2_cubeSize)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_10.addWidget(self.lineEdit_6)
        self.label_11 = QtWidgets.QLabel(self.B2_cubeSize)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.B2_cubeSize)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_10.addWidget(self.lineEdit_5)
        self.label_12 = QtWidgets.QLabel(self.B2_cubeSize)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.B2_cubeSize)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_10.addWidget(self.lineEdit_11)
        spacerItem12 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem12)
        self.verticalLayout_14.addWidget(self.B2_cubeSize)
        self.B3_advancedOptions = QtWidgets.QGroupBox(self.B_datasetOptions)
        self.B3_advancedOptions.setTitle("")
        self.B3_advancedOptions.setObjectName("B3_advancedOptions")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.B3_advancedOptions)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.B3_advancedOptions)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
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
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_5.addWidget(self.pushButton_9)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.verticalLayout_14.addWidget(self.B3_advancedOptions)
        self.groupBox_4 = QtWidgets.QGroupBox(self.B_datasetOptions)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem14)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QtCore.QSize(170, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background: #6668ad;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 6px solid transparent;\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_6.addWidget(self.pushButton_10)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
        self.verticalLayout_14.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.B_datasetOptions)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.progressBar_2 = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar_2.setMaximumSize(QtCore.QSize(16777215, 16))
        self.progressBar_2.setStyleSheet("QProgressBar {\n"
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
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_7.addWidget(self.progressBar_2)
        self.verticalLayout_14.addWidget(self.groupBox_5)
        self.gridLayout_5.addWidget(self.B_datasetOptions, 1, 0, 1, 1)
        self.verticalLayout_18.addWidget(self.baseLayer_3)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem16)
        self.tabWidget_2.addTab(self.page3, "")
        self.gridLayout.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setStyleSheet("background: transparent;")
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem17)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.baseLayer_4.setTitle(_translate("MainWindow", "Quick Start"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#ffffff;\">A valid query is a sample name followed by keywords. Available keywords shown in dropdown. Keywords are connected by boolean operators (AND, OR, NOT). Default is AND.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#ffffff;\">ex. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#00dfa4;\">spliceosome AND resolution:[1 TO 3]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#ffffff;\">ex. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#00dfa4;\">spliceosome OR ribosome</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#ffffff;\">ex. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#00dfa4;\">NOT spliceosome</span></p></body></html>"))
        self.B2_queryBox_2.setTitle(_translate("MainWindow", "Query"))
        self.lineEdit_22.setPlaceholderText(_translate("MainWindow", "save folder"))
        self.pushButton_7.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">this is limiting the window\'s thickness when shrinking btw, prob a better way to go about sizepolicys</span></p></body></html>"))
        self.pushButton_7.setText(_translate("MainWindow", "Generate Dataset"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Quick Start"))
        self.baseLayer.setTitle(_translate("MainWindow", "Query > CSV file"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:696; color:#616161;\">If you already have a CSV file, go to the next page.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:6pt; font-weight:696; color:#616161;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; text-decoration: underline; color:#616161;\">CSV file requirements (columns):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#616161;\">    emdb_id, title, resolution, fitted_pdbs, xref_UNIPROTKB, xref_ALPHAFOLD<br /></span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-style:italic; color:#616161;\">  </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-style:italic; color:#0000ff;\">*CSV files downloaded from EMDB</span></p></body></html>"))
        self.B_enterQuery.setTitle(_translate("MainWindow", "Enter a query"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">Type in sample name followed by keywords. Common keywords available in dropdown. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">Hit </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:696; color:#000000;\">return</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\"> after each keyword. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-style:italic; color:#000000;\">Text not in the form of a tag (hitting return creates a tag) will NOT be read.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">ex. spliceosome </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#000000;\">[return]</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\"> resolution:2-5 </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#000000;\">[return]</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Query"))
        self.lineEdit_21.setPlaceholderText(_translate("MainWindow", "save path"))
        self.pushButton_6.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">this is limiting the window\'s thickness when shrinking btw, prob a better way to go about sizepolicys</span></p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "Download CSV"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.page1), _translate("MainWindow", "Make Query"))
        self.baseLayer_2.setTitle(_translate("MainWindow", "Choose/Refine"))
        self.A_selectCSV_2.setTitle(_translate("MainWindow", "Choose File (from page 1 or your own)"))
        self.lineEdit_10.setToolTip(_translate("MainWindow", "type or browse (note to self: check that file exists, if not spit the error out to the statusbar)"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "CSV filepath"))
        self.pushButton_15.setToolTip(_translate("MainWindow", "browse or type"))
        self.A_selectCSV_5.setTitle(_translate("MainWindow", "Refine file (Optional)"))
        self.option1Label.setText(_translate("MainWindow", "option1"))
        self.pushButton.setText(_translate("MainWindow", "refine fxn 1"))
        self.pushButton_2.setText(_translate("MainWindow", "..."))
        self.pushButton_3.setText(_translate("MainWindow", "..."))
        self.lineEdit_12.setPlaceholderText(_translate("MainWindow", "CSV filepath"))
        self.pushButton_29.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select a CSV file first.</p></body></html>"))
        self.pushButton_29.setText(_translate("MainWindow", "Open CSV editor"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.page2), _translate("MainWindow", "Choose File/Refine"))
        self.baseLayer_3.setTitle(_translate("MainWindow", "Generate Dataset"))
        self.B_datasetOptions.setTitle(_translate("MainWindow", "Dataset options"))
        self.B1_featureLabels.setTitle(_translate("MainWindow", "Labels:"))
        self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "Type (REMOVE THIS AND PUT IN NEW WINDOW FOR POPUP)"))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("MainWindow", "Protein"))
        self.treeWidget_2.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Residues"))
        self.treeWidget_2.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_2.topLevelItem(0).child(0).child(1).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_2.topLevelItem(0).child(0).child(2).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_2.topLevelItem(0).child(0).child(3).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_2.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Key Atoms"))
        self.treeWidget_2.topLevelItem(1).setText(0, _translate("MainWindow", "DNA"))
        self.treeWidget_2.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Residues"))
        self.treeWidget_2.topLevelItem(1).child(0).child(0).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_2.topLevelItem(1).child(0).child(1).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_2.topLevelItem(1).child(0).child(2).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_2.topLevelItem(1).child(0).child(3).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_2.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "Key Atoms"))
        self.treeWidget_2.topLevelItem(2).setText(0, _translate("MainWindow", "RNA"))
        self.treeWidget_2.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "Residues"))
        self.treeWidget_2.topLevelItem(2).child(0).child(0).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_2.topLevelItem(2).child(0).child(1).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_2.topLevelItem(2).child(0).child(2).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_2.topLevelItem(2).child(0).child(3).setText(0, _translate("MainWindow", "TODO"))
        self.treeWidget_2.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "Key Atoms"))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.pushButton_11.setText(_translate("MainWindow", "add a group of labels (REMOVE TREE WIDGET, will be popup)"))
        self.label_10.setText(_translate("MainWindow", "Cube size:"))
        self.lineEdit_6.setText(_translate("MainWindow", "64"))
        self.label_11.setText(_translate("MainWindow", "x"))
        self.lineEdit_5.setText(_translate("MainWindow", "64"))
        self.label_12.setText(_translate("MainWindow", "x"))
        self.lineEdit_11.setText(_translate("MainWindow", "64"))
        self.pushButton_9.setText(_translate("MainWindow", "Advanced options"))
        self.pushButton_10.setText(_translate("MainWindow", "Generate Dataset"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.page3), _translate("MainWindow", "Generate Dataset"))
        self.dockWidget.setToolTip(_translate("MainWindow", "hi"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">exploring using a sidepanel. might move the tab buttons here. Or just use this to display info (logs, running jobs, files generated, summary stats, etc)</p></body></html>"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
