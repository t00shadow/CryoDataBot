# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/c/Users/noelu/Python Projects/PyQt GUI practice/QtDesigner_practice/dataset_gen_tool_GUI/dataset_gen_tool_v11_experimental.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1255, 886)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.custom_top_bar = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custom_top_bar.sizePolicy().hasHeightForWidth())
        self.custom_top_bar.setSizePolicy(sizePolicy)
        self.custom_top_bar.setMaximumSize(QtCore.QSize(16777215, 20))
        self.custom_top_bar.setStyleSheet("background-color: transparent;   /*darken this later for custom window bar*/")
        self.custom_top_bar.setObjectName("custom_top_bar")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.custom_top_bar)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_3 = QtWidgets.QLabel(self.custom_top_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("padding-left: 5px;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.gridLayout.addWidget(self.custom_top_bar, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.leftpanel = QtWidgets.QWidget(self.splitter)
        self.leftpanel.setMinimumSize(QtCore.QSize(65, 0))
        self.leftpanel.setMaximumSize(QtCore.QSize(135, 16777215))
        self.leftpanel.setStyleSheet("#leftpanel{\n"
"    background-color: transparent;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border-radius: 15px;\n"
"    text-align: left;\n"
"    padding-left: 12px;\n"
"    padding-right: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c2c2c2;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #90bcff;\n"
"}")
        self.leftpanel.setObjectName("leftpanel")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.leftpanel)
        self.verticalLayout_22.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(spacerItem1)
        self.sidebtn_0 = QtWidgets.QPushButton(self.leftpanel)
        self.sidebtn_0.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sidebtn_0.setFont(font)
        self.sidebtn_0.setStyleSheet("/*background: qlineargradient(spread:pad, x1:0.27, y1:0, x2:0.8, y2:1, \n"
"                                                stop:0 #AF40FF, stop:0.5 #5B42F3, stop:1 #00DDEB);*/")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/home-button-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sidebtn_0.setIcon(icon)
        self.sidebtn_0.setCheckable(True)
        self.sidebtn_0.setObjectName("sidebtn_0")
        self.verticalLayout_22.addWidget(self.sidebtn_0)
        self.sidebtn_1 = QtWidgets.QPushButton(self.leftpanel)
        self.sidebtn_1.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sidebtn_1.setFont(font)
        self.sidebtn_1.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/settings-1389-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sidebtn_1.setIcon(icon1)
        self.sidebtn_1.setCheckable(True)
        self.sidebtn_1.setObjectName("sidebtn_1")
        self.verticalLayout_22.addWidget(self.sidebtn_1)
        self.sidebtn_2_container = QtWidgets.QWidget(self.leftpanel)
        self.sidebtn_2_container.setObjectName("sidebtn_2_container")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.sidebtn_2_container)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem2)
        self.sidebtn_2 = QtWidgets.QPushButton(self.sidebtn_2_container)
        self.sidebtn_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sidebtn_2.setFont(font)
        self.sidebtn_2.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/settings-svgrepo-com (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sidebtn_2.setIcon(icon2)
        self.sidebtn_2.setCheckable(True)
        self.sidebtn_2.setObjectName("sidebtn_2")
        self.horizontalLayout_30.addWidget(self.sidebtn_2)
        self.verticalLayout_22.addWidget(self.sidebtn_2_container)
        self.sidebtn_3_container = QtWidgets.QWidget(self.leftpanel)
        self.sidebtn_3_container.setEnabled(True)
        self.sidebtn_3_container.setObjectName("sidebtn_3_container")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.sidebtn_3_container)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        spacerItem3 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem3)
        self.sidebtn_3 = QtWidgets.QPushButton(self.sidebtn_3_container)
        self.sidebtn_3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sidebtn_3.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/settings-svgrepo-com (2).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sidebtn_3.setIcon(icon3)
        self.sidebtn_3.setCheckable(True)
        self.sidebtn_3.setObjectName("sidebtn_3")
        self.horizontalLayout_31.addWidget(self.sidebtn_3)
        self.verticalLayout_22.addWidget(self.sidebtn_3_container)
        self.sidebtn_4_container = QtWidgets.QWidget(self.leftpanel)
        self.sidebtn_4_container.setObjectName("sidebtn_4_container")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.sidebtn_4_container)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        spacerItem4 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem4)
        self.sidebtn_4 = QtWidgets.QPushButton(self.sidebtn_4_container)
        self.sidebtn_4.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sidebtn_4.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/settings-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sidebtn_4.setIcon(icon4)
        self.sidebtn_4.setCheckable(True)
        self.sidebtn_4.setObjectName("sidebtn_4")
        self.horizontalLayout_32.addWidget(self.sidebtn_4)
        self.verticalLayout_22.addWidget(self.sidebtn_4_container)
        self.sidebtn_5 = QtWidgets.QPushButton(self.leftpanel)
        self.sidebtn_5.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sidebtn_5.setFont(font)
        self.sidebtn_5.setCheckable(True)
        self.sidebtn_5.setObjectName("sidebtn_5")
        self.verticalLayout_22.addWidget(self.sidebtn_5)
        self.sidebtn_6 = QtWidgets.QPushButton(self.leftpanel)
        self.sidebtn_6.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sidebtn_6.setFont(font)
        self.sidebtn_6.setCheckable(True)
        self.sidebtn_6.setObjectName("sidebtn_6")
        self.verticalLayout_22.addWidget(self.sidebtn_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_22.addItem(spacerItem5)
        self.stackedWidget = QtWidgets.QStackedWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setStyleSheet("QStackedWidget {\n"
"    background-color: white;\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidgetPage0 = QtWidgets.QWidget()
        self.stackedWidgetPage0.setObjectName("stackedWidgetPage0")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.stackedWidgetPage0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.stackedWidgetPage0)
        self.scrollArea_5.setStyleSheet("#scrollArea_5, #scrollAreaWidgetContents_5_{\n"
"    background-color: white;\n"
"    border: transparent;\n"
"}")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5_ = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5_.setGeometry(QtCore.QRect(0, 0, 758, 799))
        self.scrollAreaWidgetContents_5_.setObjectName("scrollAreaWidgetContents_5_")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5_)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.baseLayer_0 = QtWidgets.QWidget(self.scrollAreaWidgetContents_5_)
        self.baseLayer_0.setObjectName("baseLayer_0")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.baseLayer_0)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.main_save_path_container_2 = QtWidgets.QWidget(self.baseLayer_0)
        self.main_save_path_container_2.setObjectName("main_save_path_container_2")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.main_save_path_container_2)
        self.verticalLayout_24.setContentsMargins(10, 0, 50, 0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_20 = QtWidgets.QLabel(self.main_save_path_container_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_24.addWidget(self.label_20)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_24.addItem(spacerItem6)
        self.label_17 = QtWidgets.QLabel(self.main_save_path_container_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_24.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.main_save_path_container_2)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_24.addWidget(self.label_18)
        self.path_container = QtWidgets.QGroupBox(self.main_save_path_container_2)
        self.path_container.setStyleSheet("border: 0px;\n"
"border-radius: 8px;\n"
"background-color: #d5d7ff;\n"
"background-color: #6668ad;")
        self.path_container.setTitle("")
        self.path_container.setObjectName("path_container")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.path_container)
        self.horizontalLayout_41.setContentsMargins(20, 4, 4, 4)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.main_save_path_lineedit = QtWidgets.QLineEdit(self.path_container)
        self.main_save_path_lineedit.setEnabled(False)
        self.main_save_path_lineedit.setMinimumSize(QtCore.QSize(200, 0))
        self.main_save_path_lineedit.setStyleSheet("background-color: white;\n"
"padding-left: 4px;\n"
"padding-bottom: 2px;")
        self.main_save_path_lineedit.setText("")
        self.main_save_path_lineedit.setDragEnabled(False)
        self.main_save_path_lineedit.setClearButtonEnabled(False)
        self.main_save_path_lineedit.setObjectName("main_save_path_lineedit")
        self.horizontalLayout_41.addWidget(self.main_save_path_lineedit)
        self.main_save_path_btn = QtWidgets.QPushButton(self.path_container)
        self.main_save_path_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_save_path_btn.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.main_save_path_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/browsefilesicon_zoomed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_save_path_btn.setIcon(icon5)
        self.main_save_path_btn.setObjectName("main_save_path_btn")
        self.horizontalLayout_41.addWidget(self.main_save_path_btn)
        self.verticalLayout_24.addWidget(self.path_container)
        self.verticalLayout_25.addWidget(self.main_save_path_container_2)
        self.verticalLayout_31.addWidget(self.baseLayer_0)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_5_)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_31.addWidget(self.plainTextEdit_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 677, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_31.addItem(spacerItem7)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5_)
        self.verticalLayout_26.addWidget(self.scrollArea_5)
        self.stackedWidget.addWidget(self.stackedWidgetPage0)
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.stackedWidgetPage1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.stackedWidgetPage1)
        self.scrollArea_4.setStyleSheet("#scrollArea_4, #scrollAreaWidgetContents_4_{\n"
"    background-color: white;\n"
"    border: transparent;\n"
"}")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4_ = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4_.setGeometry(QtCore.QRect(0, 0, 758, 799))
        self.scrollAreaWidgetContents_4_.setObjectName("scrollAreaWidgetContents_4_")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4_)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.baseLayer_1 = QtWidgets.QWidget(self.scrollAreaWidgetContents_4_)
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
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.baseLayer_1)
        self.verticalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.page2TitleWidget_2 = QtWidgets.QWidget(self.baseLayer_1)
        self.page2TitleWidget_2.setObjectName("page2TitleWidget_2")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.page2TitleWidget_2)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.page2TitleLabel_2 = QtWidgets.QLabel(self.page2TitleWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.page2TitleLabel_2.setFont(font)
        self.page2TitleLabel_2.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    color: black;\n"
"}")
        self.page2TitleLabel_2.setObjectName("page2TitleLabel_2")
        self.horizontalLayout_33.addWidget(self.page2TitleLabel_2)
        self.qScoreInfo_btn_5 = QtWidgets.QPushButton(self.page2TitleWidget_2)
        self.qScoreInfo_btn_5.setStyleSheet("background-color: transparent;")
        self.qScoreInfo_btn_5.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/info-circle-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.qScoreInfo_btn_5.setIcon(icon6)
        self.qScoreInfo_btn_5.setIconSize(QtCore.QSize(20, 20))
        self.qScoreInfo_btn_5.setObjectName("qScoreInfo_btn_5")
        self.horizontalLayout_33.addWidget(self.qScoreInfo_btn_5)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem8)
        self.verticalLayout_14.addWidget(self.page2TitleWidget_2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_14.addItem(spacerItem9)
        self.A_quickStart = QtWidgets.QGroupBox(self.baseLayer_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A_quickStart.sizePolicy().hasHeightForWidth())
        self.A_quickStart.setSizePolicy(sizePolicy)
        self.A_quickStart.setStyleSheet("QGroupBox#A_quickStart {\n"
"    border-radius: 20px;\n"
"    background-color: rgba(102, 104, 173, 150);\n"
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
        self.A1_instructions.setMinimumSize(QtCore.QSize(0, 200))
        self.A1_instructions.setMaximumSize(QtCore.QSize(16777215, 250))
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_p1.sizePolicy().hasHeightForWidth())
        self.textBrowser_p1.setSizePolicy(sizePolicy)
        self.textBrowser_p1.setMaximumSize(QtCore.QSize(16777215, 400))
        self.textBrowser_p1.setStyleSheet("background-color: transparent;\n"
"border: transparent;")
        self.textBrowser_p1.setOpenExternalLinks(True)
        self.textBrowser_p1.setObjectName("textBrowser_p1")
        self.horizontalLayout_11.addWidget(self.textBrowser_p1)
        self.verticalLayout_2.addWidget(self.A1_instructions)
        self.label = QtWidgets.QLabel(self.A_quickStart)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.fancySearchBar_2 = QtWidgets.QWidget(self.A_quickStart)
        self.fancySearchBar_2.setStyleSheet("#fancySearchBar_2 {\n"
"    background-color: black;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"#fancySearchBar_2:hover {\n"
"    background-color: rgb(200, 200, 200);\n"
"}")
        self.fancySearchBar_2.setObjectName("fancySearchBar_2")
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout(self.fancySearchBar_2)
        self.horizontalLayout_60.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.fancySearchBar_2)
        self.lineEdit_15.setMaximumSize(QtCore.QSize(16777215, 24))
        self.lineEdit_15.setStyleSheet("background: white;\n"
"border: transparent;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"padding-left: 4px;\n"
"padding-bottom: 2px;")
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.horizontalLayout_60.addWidget(self.lineEdit_15)
        self.pushButton_19 = QtWidgets.QPushButton(self.fancySearchBar_2)
        self.pushButton_19.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        self.pushButton_19.setFont(font)
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_19.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_19.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
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
        self.pushButton_19.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/send-alt-2-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_19.setIcon(icon7)
        self.pushButton_19.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_60.addWidget(self.pushButton_19)
        self.verticalLayout_2.addWidget(self.fancySearchBar_2)
        self.quick_refine_container = QtWidgets.QWidget(self.A_quickStart)
        self.quick_refine_container.setObjectName("quick_refine_container")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.quick_refine_container)
        self.verticalLayout_23.setContentsMargins(0, 15, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_5 = QtWidgets.QLabel(self.quick_refine_container)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_23.addWidget(self.label_5)
        self.widget_14 = QtWidgets.QWidget(self.quick_refine_container)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
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
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/external-link-512.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon8)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_34.addWidget(self.pushButton_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem10)
        self.verticalLayout_23.addWidget(self.widget_14)
        self.verticalLayout_2.addWidget(self.quick_refine_container)
        self.widget_4 = QtWidgets.QWidget(self.A_quickStart)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setContentsMargins(0, 15, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget = QtWidgets.QWidget(self.A_quickStart)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
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
        self.pushButton.setIcon(icon8)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout_14.addWidget(self.A_quickStart)
        self.A5_generateDataset = QtWidgets.QGroupBox(self.baseLayer_1)
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
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem12)
        self.pushButton_p1_3 = QtWidgets.QPushButton(self.A5_generateDataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
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
"    background: rgba(193, 211, 239, 255);\n"
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
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem13)
        self.verticalLayout_14.addWidget(self.A5_generateDataset)
        self.widget_2 = QtWidgets.QWidget(self.baseLayer_1)
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
        self.verticalLayout_14.addWidget(self.widget_2)
        self.verticalLayout_30.addWidget(self.baseLayer_1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_30.addItem(spacerItem14)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4_)
        self.gridLayout_8.addWidget(self.scrollArea_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QtWidgets.QWidget()
        self.stackedWidgetPage2.setObjectName("stackedWidgetPage2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.stackedWidgetPage2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.stackedWidgetPage2)
        self.scrollArea_3.setStyleSheet("#scrollArea_3, #scrollAreaWidgetContents_3_{\n"
"    background-color: white;\n"
"    border: transparent;\n"
"}")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3_ = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3_.setGeometry(QtCore.QRect(0, 0, 758, 799))
        self.scrollAreaWidgetContents_3_.setObjectName("scrollAreaWidgetContents_3_")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3_)
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.baseLayer_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3_)
        self.baseLayer_2.setStyleSheet("QWidget#baseLayer_2 {\n"
"    font-size: 24pt;\n"
"    font-weight: bold;\n"
"    border: transparent;\n"
"    padding-top: 30px;\n"
"}")
        self.baseLayer_2.setObjectName("baseLayer_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.baseLayer_2)
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.page2TitleWidget = QtWidgets.QWidget(self.baseLayer_2)
        self.page2TitleWidget.setObjectName("page2TitleWidget")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.page2TitleWidget)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.page2TitleLabel = QtWidgets.QLabel(self.page2TitleWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.page2TitleLabel.setFont(font)
        self.page2TitleLabel.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    color: #6668ad;\n"
"}")
        self.page2TitleLabel.setObjectName("page2TitleLabel")
        self.horizontalLayout_25.addWidget(self.page2TitleLabel)
        self.qScoreInfo_btn_2 = QtWidgets.QPushButton(self.page2TitleWidget)
        self.qScoreInfo_btn_2.setStyleSheet("background-color: transparent;")
        self.qScoreInfo_btn_2.setText("")
        self.qScoreInfo_btn_2.setIcon(icon6)
        self.qScoreInfo_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.qScoreInfo_btn_2.setObjectName("qScoreInfo_btn_2")
        self.horizontalLayout_25.addWidget(self.qScoreInfo_btn_2)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem15)
        self.verticalLayout_15.addWidget(self.page2TitleWidget)
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_15.addItem(spacerItem16)
        self.rename_everything = QtWidgets.QWidget(self.baseLayer_2)
        self.rename_everything.setObjectName("rename_everything")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.rename_everything)
        self.verticalLayout_6.setContentsMargins(10, 0, 50, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.rename_everything)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.B1_csvFilepath = QtWidgets.QGroupBox(self.rename_everything)
        self.B1_csvFilepath.setStyleSheet("border: 0px;\n"
"border-radius: 8px;\n"
"background-color: #d5d7ff;\n"
"background-color: #6668ad;")
        self.B1_csvFilepath.setTitle("")
        self.B1_csvFilepath.setObjectName("B1_csvFilepath")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.B1_csvFilepath)
        self.horizontalLayout_40.setContentsMargins(20, 4, 4, 4)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.lineEdit_p2 = QtWidgets.QLineEdit(self.B1_csvFilepath)
        self.lineEdit_p2.setEnabled(False)
        self.lineEdit_p2.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_p2.setStyleSheet("background-color: white;\n"
"padding-left: 4px;\n"
"padding-bottom: 2px;")
        self.lineEdit_p2.setText("")
        self.lineEdit_p2.setDragEnabled(False)
        self.lineEdit_p2.setClearButtonEnabled(False)
        self.lineEdit_p2.setObjectName("lineEdit_p2")
        self.horizontalLayout_40.addWidget(self.lineEdit_p2)
        self.pushButton_p2 = QtWidgets.QPushButton(self.B1_csvFilepath)
        self.pushButton_p2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_p2.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.pushButton_p2.setText("")
        self.pushButton_p2.setIcon(icon5)
        self.pushButton_p2.setObjectName("pushButton_p2")
        self.horizontalLayout_40.addWidget(self.pushButton_p2)
        self.verticalLayout_6.addWidget(self.B1_csvFilepath)
        self.verticalLayout_15.addWidget(self.rename_everything)
        spacerItem17 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_15.addItem(spacerItem17)
        self.B_enterQuery = QtWidgets.QGroupBox(self.baseLayer_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B_enterQuery.sizePolicy().hasHeightForWidth())
        self.B_enterQuery.setSizePolicy(sizePolicy)
        self.B_enterQuery.setStyleSheet("QGroupBox#B_enterQuery {\n"
"    border-radius: 20px;\n"
"    background-color: rgba(193, 211, 239, 100);\n"
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.B_enterQuery)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_p2 = QtWidgets.QLabel(self.B2_queryBox)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_p2.setFont(font)
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
        self.validateQuery_btn.setIcon(icon7)
        self.validateQuery_btn.setObjectName("validateQuery_btn")
        self.horizontalLayout_20.addWidget(self.validateQuery_btn)
        self.verticalLayout_4.addWidget(self.widget_7)
        self.verticalLayout.addWidget(self.B2_queryBox)
        self.fancySearchBar = QtWidgets.QWidget(self.B_enterQuery)
        self.fancySearchBar.setStyleSheet("#fancySearchBar {\n"
"    background-color: gray;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"#fancySearchBar:hover {\n"
"    background-color: black;\n"
"}")
        self.fancySearchBar.setObjectName("fancySearchBar")
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout(self.fancySearchBar)
        self.horizontalLayout_58.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.fancySearchBar)
        self.lineEdit_12.setMaximumSize(QtCore.QSize(16777215, 24))
        self.lineEdit_12.setStyleSheet("background: white;\n"
"border: transparent;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"padding-left: 4px;\n"
"padding-bottom: 2px;")
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_58.addWidget(self.lineEdit_12)
        self.pushButton_16 = QtWidgets.QPushButton(self.fancySearchBar)
        self.pushButton_16.setMaximumSize(QtCore.QSize(16777215, 24))
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
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
        self.pushButton_16.setIcon(icon7)
        self.pushButton_16.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_58.addWidget(self.pushButton_16)
        self.verticalLayout.addWidget(self.fancySearchBar)
        self.textEdit = QtWidgets.QTextEdit(self.B_enterQuery)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout_15.addWidget(self.B_enterQuery)
        self.B4_downloadbtn = QtWidgets.QGroupBox(self.baseLayer_2)
        self.B4_downloadbtn.setStyleSheet("QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}\n"
"")
        self.B4_downloadbtn.setTitle("")
        self.B4_downloadbtn.setObjectName("B4_downloadbtn")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.B4_downloadbtn)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem18)
        self.pushButton_p2_2 = QtWidgets.QPushButton(self.B4_downloadbtn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p2_2.sizePolicy().hasHeightForWidth())
        self.pushButton_p2_2.setSizePolicy(sizePolicy)
        self.pushButton_p2_2.setMinimumSize(QtCore.QSize(232, 40))
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
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem19)
        self.verticalLayout_15.addWidget(self.B4_downloadbtn)
        self.B5_progressDisplay = QtWidgets.QGroupBox(self.baseLayer_2)
        self.B5_progressDisplay.setStyleSheet("QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}")
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
        self.verticalLayout_15.addWidget(self.B5_progressDisplay)
        self.verticalLayout_29.addWidget(self.baseLayer_2)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_29.addItem(spacerItem20)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3_)
        self.verticalLayout_7.addWidget(self.scrollArea_3)
        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.stackedWidgetPage3 = QtWidgets.QWidget()
        self.stackedWidgetPage3.setObjectName("stackedWidgetPage3")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.stackedWidgetPage3)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.stackedWidgetPage3)
        self.scrollArea_2.setStyleSheet("#scrollArea_2, #scrollAreaWidgetContents_2{\n"
"    background-color: white;\n"
"    border: transparent;\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 758, 799))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.baseLayer_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.baseLayer_3.setStyleSheet("QWidget#baseLayer_3 {\n"
"    font-size: 24pt;\n"
"    font-weight: bold;\n"
"    border: transparent;\n"
"    padding-top: 30px;\n"
"}")
        self.baseLayer_3.setObjectName("baseLayer_3")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.baseLayer_3)
        self.verticalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.page3TitleWidget = QtWidgets.QWidget(self.baseLayer_3)
        self.page3TitleWidget.setObjectName("page3TitleWidget")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.page3TitleWidget)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.page3TitleLabel = QtWidgets.QLabel(self.page3TitleWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.page3TitleLabel.setFont(font)
        self.page3TitleLabel.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    color: #6668ad;\n"
"}")
        self.page3TitleLabel.setObjectName("page3TitleLabel")
        self.horizontalLayout_26.addWidget(self.page3TitleLabel)
        self.qScoreInfo_btn_3 = QtWidgets.QPushButton(self.page3TitleWidget)
        self.qScoreInfo_btn_3.setStyleSheet("background-color: transparent;")
        self.qScoreInfo_btn_3.setText("")
        self.qScoreInfo_btn_3.setIcon(icon6)
        self.qScoreInfo_btn_3.setIconSize(QtCore.QSize(20, 20))
        self.qScoreInfo_btn_3.setObjectName("qScoreInfo_btn_3")
        self.horizontalLayout_26.addWidget(self.qScoreInfo_btn_3)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem21)
        self.verticalLayout_16.addWidget(self.page3TitleWidget)
        spacerItem22 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_16.addItem(spacerItem22)
        self.A_chooseCSV = QtWidgets.QGroupBox(self.baseLayer_3)
        self.A_chooseCSV.setStyleSheet("QGroupBox#A_chooseCSV {\n"
"    border-radius: 20px;\n"
"    background-color: rgba(193, 211, 239, 100);\n"
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
        self.lineEdit_p3.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: white;\n"
"    color: #525251;\n"
"    /*border: 1px solid #051a39;*/\n"
"    border-radius: 3px;\n"
"    padding : 2px;\n"
"}")
        self.lineEdit_p3.setText("")
        self.lineEdit_p3.setDragEnabled(False)
        self.lineEdit_p3.setClearButtonEnabled(True)
        self.lineEdit_p3.setObjectName("lineEdit_p3")
        self.horizontalLayout_19.addWidget(self.lineEdit_p3)
        self.resetDefaultVal_btn = QtWidgets.QPushButton(self.A2_csvFilepath)
        self.resetDefaultVal_btn.setStyleSheet("background-color: white;\n"
"border-radius: 3px;\n"
"padding : 2px;")
        self.resetDefaultVal_btn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/reset3-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetDefaultVal_btn.setIcon(icon9)
        self.resetDefaultVal_btn.setObjectName("resetDefaultVal_btn")
        self.horizontalLayout_19.addWidget(self.resetDefaultVal_btn)
        self.pushButton_p3 = QtWidgets.QPushButton(self.A2_csvFilepath)
        self.pushButton_p3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_p3.setStyleSheet("/*border-image: url(:/icons/browsefilesicon.png);*/\n"
"background-color: white;\n"
"border-radius: 3px;\n"
"padding : 2px;")
        self.pushButton_p3.setText("")
        self.pushButton_p3.setIcon(icon5)
        self.pushButton_p3.setObjectName("pushButton_p3")
        self.horizontalLayout_19.addWidget(self.pushButton_p3)
        self.verticalLayout_19.addWidget(self.A2_csvFilepath)
        self.verticalLayout_16.addWidget(self.A_chooseCSV)
        spacerItem23 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_16.addItem(spacerItem23)
        self.B_refineCSV = QtWidgets.QGroupBox(self.baseLayer_3)
        self.B_refineCSV.setStyleSheet("QGroupBox#B_refineCSV {\n"
"    border-radius: 20px;\n"
"    background-color: rgba(193, 211, 239, 100);\n"
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
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.widget1 = QtWidgets.QWidget(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setStyleSheet("QSpinBox, \n"
"QDoubleSpinBox\n"
"{\n"
"    background-color: #525251;\n"
"    color: #ffffff;\n"
"    border: 1px solid #051a39;\n"
"    border-radius: 3px;\n"
"    padding : 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::disabled, \n"
"QDoubleSpinBox::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox:hover, \n"
"QDoubleSpinBox::hover,\n"
"QDateTimeEdit::hover\n"
"{\n"
"    background-color: #626262;\n"
"    border: 1px solid #607cff;\n"
"    color:  #fff;\n"
"    padding: 2px\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button\n"
"{\n"
"    background-color: #607cff;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::disabled, \n"
"QDoubleSpinBox::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover,\n"
"QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover\n"
"{\n"
"    background-color: #8399ff;\n"
"    border: 1px solid #8399ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:disabled, QSpinBox::down-button:disabled,\n"
"QDoubleSpinBox::up-button:disabled, QDoubleSpinBox::down-button:disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed,\n"
"QDoubleSpinBox::up-button:pressed, QDoubleSpinBox::down-button::pressed\n"
"{\n"
"    background-color: #4969ff;\n"
"    border: 1px solid #4969ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"\n"
"}")
        self.widget1.setObjectName("widget1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.clearQScore_btn = QtWidgets.QPushButton(self.widget1)
        self.clearQScore_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearQScore_btn.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.clearQScore_btn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/refresh-cw-alt-3-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearQScore_btn.setIcon(icon10)
        self.clearQScore_btn.setObjectName("clearQScore_btn")
        self.gridLayout_4.addWidget(self.clearQScore_btn, 0, 2, 1, 1)
        self.clearMMF_btn = QtWidgets.QPushButton(self.widget1)
        self.clearMMF_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearMMF_btn.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.clearMMF_btn.setText("")
        self.clearMMF_btn.setIcon(icon10)
        self.clearMMF_btn.setObjectName("clearMMF_btn")
        self.gridLayout_4.addWidget(self.clearMMF_btn, 1, 2, 1, 1)
        self.widget_10 = QtWidgets.QWidget(self.widget1)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.qScoreLabel = QtWidgets.QLabel(self.widget_10)
        self.qScoreLabel.setObjectName("qScoreLabel")
        self.horizontalLayout_22.addWidget(self.qScoreLabel)
        self.qScoreInfo_btn = QtWidgets.QPushButton(self.widget_10)
        self.qScoreInfo_btn.setStyleSheet("background-color: transparent;")
        self.qScoreInfo_btn.setText("")
        self.qScoreInfo_btn.setIcon(icon6)
        self.qScoreInfo_btn.setObjectName("qScoreInfo_btn")
        self.horizontalLayout_22.addWidget(self.qScoreInfo_btn)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem24)
        self.gridLayout_4.addWidget(self.widget_10, 0, 0, 1, 1)
        self.clearSim_btn = QtWidgets.QPushButton(self.widget1)
        self.clearSim_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearSim_btn.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.clearSim_btn.setText("")
        self.clearSim_btn.setIcon(icon10)
        self.clearSim_btn.setObjectName("clearSim_btn")
        self.gridLayout_4.addWidget(self.clearSim_btn, 2, 2, 1, 1)
        self.similaritySpinBox = QtWidgets.QSpinBox(self.widget1)
        self.similaritySpinBox.setAccelerated(True)
        self.similaritySpinBox.setMaximum(100)
        self.similaritySpinBox.setProperty("value", 100)
        self.similaritySpinBox.setObjectName("similaritySpinBox")
        self.gridLayout_4.addWidget(self.similaritySpinBox, 2, 1, 1, 1)
        self.qScoreDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget1)
        self.qScoreDoubleSpinBox.setAccelerated(True)
        self.qScoreDoubleSpinBox.setMaximum(1.0)
        self.qScoreDoubleSpinBox.setSingleStep(0.01)
        self.qScoreDoubleSpinBox.setObjectName("qScoreDoubleSpinBox")
        self.gridLayout_4.addWidget(self.qScoreDoubleSpinBox, 0, 1, 1, 1)
        self.mapModelFitnessSpinBox = QtWidgets.QSpinBox(self.widget1)
        self.mapModelFitnessSpinBox.setAccelerated(True)
        self.mapModelFitnessSpinBox.setMaximum(100)
        self.mapModelFitnessSpinBox.setObjectName("mapModelFitnessSpinBox")
        self.gridLayout_4.addWidget(self.mapModelFitnessSpinBox, 1, 1, 1, 1)
        self.widget_11 = QtWidgets.QWidget(self.widget1)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.mapModelFitnessLabel = QtWidgets.QLabel(self.widget_11)
        self.mapModelFitnessLabel.setObjectName("mapModelFitnessLabel")
        self.horizontalLayout_24.addWidget(self.mapModelFitnessLabel)
        self.mmfInfo_btn = QtWidgets.QPushButton(self.widget_11)
        self.mmfInfo_btn.setStyleSheet("background-color: transparent;")
        self.mmfInfo_btn.setText("")
        self.mmfInfo_btn.setIcon(icon6)
        self.mmfInfo_btn.setObjectName("mmfInfo_btn")
        self.horizontalLayout_24.addWidget(self.mmfInfo_btn)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem25)
        self.gridLayout_4.addWidget(self.widget_11, 1, 0, 1, 1)
        self.widget_12 = QtWidgets.QWidget(self.widget1)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.similarityLabel = QtWidgets.QLabel(self.widget_12)
        self.similarityLabel.setObjectName("similarityLabel")
        self.horizontalLayout_23.addWidget(self.similarityLabel)
        self.simInfo_btn = QtWidgets.QPushButton(self.widget_12)
        self.simInfo_btn.setStyleSheet("background-color: transparent;")
        self.simInfo_btn.setText("")
        self.simInfo_btn.setIcon(icon6)
        self.simInfo_btn.setObjectName("simInfo_btn")
        self.horizontalLayout_23.addWidget(self.simInfo_btn)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem26)
        self.gridLayout_4.addWidget(self.widget_12, 2, 0, 1, 1)
        self.horizontalLayout_17.addWidget(self.widget1)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem27)
        self.verticalLayout_9.addWidget(self.widget_6)
        self.verticalLayout_16.addWidget(self.B_refineCSV)
        self.B4_downloadbtn_2 = QtWidgets.QGroupBox(self.baseLayer_3)
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
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem28)
        self.pushButton_p3_4 = QtWidgets.QPushButton(self.B4_downloadbtn_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p3_4.sizePolicy().hasHeightForWidth())
        self.pushButton_p3_4.setSizePolicy(sizePolicy)
        self.pushButton_p3_4.setMinimumSize(QtCore.QSize(232, 40))
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
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem29)
        self.verticalLayout_16.addWidget(self.B4_downloadbtn_2)
        self.verticalLayout_28.addWidget(self.baseLayer_3)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_28.addItem(spacerItem30)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_12.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.stackedWidgetPage3)
        self.stackedWidgetPage4 = QtWidgets.QWidget()
        self.stackedWidgetPage4.setObjectName("stackedWidgetPage4")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.stackedWidgetPage4)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.scrollArea = QtWidgets.QScrollArea(self.stackedWidgetPage4)
        self.scrollArea.setStyleSheet("#scrollArea, #scrollAreaWidgetContents{\n"
"    background-color: white;\n"
"    border: transparent;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 746, 940))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.baseLayer_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.baseLayer_4.setStyleSheet("QWidget#baseLayer_4 {\n"
"    font-size: 24pt;\n"
"    font-weight: bold;\n"
"    border: transparent;\n"
"    padding-top: 30px;\n"
"}")
        self.baseLayer_4.setObjectName("baseLayer_4")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.baseLayer_4)
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.page4TitleWidget = QtWidgets.QWidget(self.baseLayer_4)
        self.page4TitleWidget.setObjectName("page4TitleWidget")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.page4TitleWidget)
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.page4TitleLabel = QtWidgets.QLabel(self.page4TitleWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.page4TitleLabel.setFont(font)
        self.page4TitleLabel.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    color: #6668ad;\n"
"}")
        self.page4TitleLabel.setObjectName("page4TitleLabel")
        self.horizontalLayout_29.addWidget(self.page4TitleLabel)
        self.qScoreInfo_btn_6 = QtWidgets.QPushButton(self.page4TitleWidget)
        self.qScoreInfo_btn_6.setStyleSheet("background-color: transparent;")
        self.qScoreInfo_btn_6.setText("")
        self.qScoreInfo_btn_6.setIcon(icon6)
        self.qScoreInfo_btn_6.setIconSize(QtCore.QSize(20, 20))
        self.qScoreInfo_btn_6.setObjectName("qScoreInfo_btn_6")
        self.horizontalLayout_29.addWidget(self.qScoreInfo_btn_6)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem31)
        self.verticalLayout_17.addWidget(self.page4TitleWidget)
        self.A_chooseCSV_2 = QtWidgets.QGroupBox(self.baseLayer_4)
        self.A_chooseCSV_2.setStyleSheet("QGroupBox#A_chooseCSV_2 {\n"
"    border-radius: 20px;\n"
"    background-color: rgba(193, 211, 239, 100);\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    padding-top: 42px;\n"
"    padding-left: 12px;\n"
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
        self.A_chooseCSV_2.setObjectName("A_chooseCSV_2")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.A_chooseCSV_2)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_21 = QtWidgets.QLabel(self.A_chooseCSV_2)
        self.label_21.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_21.addWidget(self.label_21)
        self.A2_csvFilepath_2 = QtWidgets.QGroupBox(self.A_chooseCSV_2)
        self.A2_csvFilepath_2.setTitle("")
        self.A2_csvFilepath_2.setObjectName("A2_csvFilepath_2")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.A2_csvFilepath_2)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.lineEdit_p3_2 = QtWidgets.QLineEdit(self.A2_csvFilepath_2)
        self.lineEdit_p3_2.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_p3_2.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: white;\n"
"    color: #525251;\n"
"    /*border: 1px solid #051a39;*/\n"
"    border-radius: 3px;\n"
"    padding : 2px;\n"
"}")
        self.lineEdit_p3_2.setText("")
        self.lineEdit_p3_2.setDragEnabled(False)
        self.lineEdit_p3_2.setClearButtonEnabled(True)
        self.lineEdit_p3_2.setObjectName("lineEdit_p3_2")
        self.horizontalLayout_28.addWidget(self.lineEdit_p3_2)
        self.resetDefaultVal_btn_2 = QtWidgets.QPushButton(self.A2_csvFilepath_2)
        self.resetDefaultVal_btn_2.setStyleSheet("background-color: white;\n"
"border-radius: 3px;\n"
"padding : 2px;")
        self.resetDefaultVal_btn_2.setText("")
        self.resetDefaultVal_btn_2.setIcon(icon9)
        self.resetDefaultVal_btn_2.setObjectName("resetDefaultVal_btn_2")
        self.horizontalLayout_28.addWidget(self.resetDefaultVal_btn_2)
        self.pushButton_p3_2 = QtWidgets.QPushButton(self.A2_csvFilepath_2)
        self.pushButton_p3_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_p3_2.setStyleSheet("/*border-image: url(:/icons/browsefilesicon.png);*/\n"
"background-color: white;\n"
"border-radius: 3px;\n"
"padding : 2px;")
        self.pushButton_p3_2.setText("")
        self.pushButton_p3_2.setIcon(icon5)
        self.pushButton_p3_2.setObjectName("pushButton_p3_2")
        self.horizontalLayout_28.addWidget(self.pushButton_p3_2)
        self.verticalLayout_21.addWidget(self.A2_csvFilepath_2)
        self.verticalLayout_17.addWidget(self.A_chooseCSV_2)
        spacerItem32 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_17.addItem(spacerItem32)
        self.A_datasetOptions = QtWidgets.QGroupBox(self.baseLayer_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A_datasetOptions.sizePolicy().hasHeightForWidth())
        self.A_datasetOptions.setSizePolicy(sizePolicy)
        self.A_datasetOptions.setStyleSheet("QGroupBox#A_datasetOptions {\n"
"    border-radius: 20px;\n"
"    background-color: rgba(193, 211, 239, 100);\n"
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
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem33)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.A1_featureLabels = QtWidgets.QWidget(self.A_datasetOptions)
        self.A1_featureLabels.setMinimumSize(QtCore.QSize(0, 400))
        self.A1_featureLabels.setObjectName("A1_featureLabels")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.A1_featureLabels)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.treeWidget_p4 = QtWidgets.QTreeWidget(self.A1_featureLabels)
        self.treeWidget_p4.setStyleSheet("QTreeWidget {\n"
"    background-color: transparent;\n"
"    border: transparent;\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
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
        self.treeWidget_p4.setAlternatingRowColors(False)
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
        self.horizontalLayout_10.setContentsMargins(0, -1, -1, 25)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_p4 = QtWidgets.QLabel(self.A2_cubeSize)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_p4.setFont(font)
        self.label_p4.setObjectName("label_p4")
        self.horizontalLayout_10.addWidget(self.label_p4)
        self.spinBox_4 = QtWidgets.QSpinBox(self.A2_cubeSize)
        self.spinBox_4.setStyleSheet("QSpinBox, \n"
"QDoubleSpinBox\n"
"{\n"
"    background-color: #525251;\n"
"    color: #ffffff;\n"
"    border: 1px solid #051a39;\n"
"    border-radius: 3px;\n"
"    padding : 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::disabled, \n"
"QDoubleSpinBox::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox:hover, \n"
"QDoubleSpinBox::hover,\n"
"QDateTimeEdit::hover\n"
"{\n"
"    background-color: #626262;\n"
"    border: 1px solid #607cff;\n"
"    color:  #fff;\n"
"    padding: 2px\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button\n"
"{\n"
"    background-color: #607cff;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::disabled, \n"
"QDoubleSpinBox::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover,\n"
"QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover\n"
"{\n"
"    background-color: #8399ff;\n"
"    border: 1px solid #8399ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:disabled, QSpinBox::down-button:disabled,\n"
"QDoubleSpinBox::up-button:disabled, QDoubleSpinBox::down-button:disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed,\n"
"QDoubleSpinBox::up-button:pressed, QDoubleSpinBox::down-button::pressed\n"
"{\n"
"    background-color: #4969ff;\n"
"    border: 1px solid #4969ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"\n"
"}")
        self.spinBox_4.setAccelerated(True)
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(128)
        self.spinBox_4.setProperty("value", 64)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_10.addWidget(self.spinBox_4)
        self.label_p4_2 = QtWidgets.QLabel(self.A2_cubeSize)
        self.label_p4_2.setObjectName("label_p4_2")
        self.horizontalLayout_10.addWidget(self.label_p4_2)
        spacerItem34 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem34)
        self.verticalLayout_3.addWidget(self.A2_cubeSize)
        self.dataset_split_container = QtWidgets.QWidget(self.A_datasetOptions)
        self.dataset_split_container.setStyleSheet("QSpinBox, \n"
"QDoubleSpinBox\n"
"{\n"
"    background-color: #525251;\n"
"    color: #ffffff;\n"
"    border: 1px solid #051a39;\n"
"    border-radius: 3px;\n"
"    padding : 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::disabled, \n"
"QDoubleSpinBox::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox:hover, \n"
"QDoubleSpinBox::hover,\n"
"QDateTimeEdit::hover\n"
"{\n"
"    background-color: #626262;\n"
"    border: 1px solid #607cff;\n"
"    color:  #fff;\n"
"    padding: 2px\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button\n"
"{\n"
"    background-color: #607cff;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::disabled, \n"
"QDoubleSpinBox::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover,\n"
"QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover\n"
"{\n"
"    background-color: #8399ff;\n"
"    border: 1px solid #8399ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:disabled, QSpinBox::down-button:disabled,\n"
"QDoubleSpinBox::up-button:disabled, QDoubleSpinBox::down-button:disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed,\n"
"QDoubleSpinBox::up-button:pressed, QDoubleSpinBox::down-button::pressed\n"
"{\n"
"    background-color: #4969ff;\n"
"    border: 1px solid #4969ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"\n"
"}")
        self.dataset_split_container.setObjectName("dataset_split_container")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dataset_split_container)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.validation_label = QtWidgets.QLabel(self.dataset_split_container)
        self.validation_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.validation_label.setObjectName("validation_label")
        self.gridLayout_2.addWidget(self.validation_label, 1, 4, 1, 1)
        self.training_label = QtWidgets.QLabel(self.dataset_split_container)
        self.training_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.training_label.setObjectName("training_label")
        self.gridLayout_2.addWidget(self.training_label, 1, 0, 1, 1)
        self.training_spinBox = QtWidgets.QSpinBox(self.dataset_split_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.training_spinBox.sizePolicy().hasHeightForWidth())
        self.training_spinBox.setSizePolicy(sizePolicy)
        self.training_spinBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.training_spinBox.setMaximum(100)
        self.training_spinBox.setObjectName("training_spinBox")
        self.gridLayout_2.addWidget(self.training_spinBox, 1, 1, 1, 1)
        self.testing_label = QtWidgets.QLabel(self.dataset_split_container)
        self.testing_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.testing_label.setObjectName("testing_label")
        self.gridLayout_2.addWidget(self.testing_label, 1, 2, 1, 1)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem35, 1, 6, 1, 1)
        self.validation_spinBox = QtWidgets.QSpinBox(self.dataset_split_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validation_spinBox.sizePolicy().hasHeightForWidth())
        self.validation_spinBox.setSizePolicy(sizePolicy)
        self.validation_spinBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.validation_spinBox.setMaximum(100)
        self.validation_spinBox.setObjectName("validation_spinBox")
        self.gridLayout_2.addWidget(self.validation_spinBox, 1, 5, 1, 1)
        self.testing_spinBox = QtWidgets.QSpinBox(self.dataset_split_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testing_spinBox.sizePolicy().hasHeightForWidth())
        self.testing_spinBox.setSizePolicy(sizePolicy)
        self.testing_spinBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.testing_spinBox.setMaximum(100)
        self.testing_spinBox.setObjectName("testing_spinBox")
        self.gridLayout_2.addWidget(self.testing_spinBox, 1, 3, 1, 1)
        self.dataset_split_title = QtWidgets.QLabel(self.dataset_split_container)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.dataset_split_title.setFont(font)
        self.dataset_split_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dataset_split_title.setObjectName("dataset_split_title")
        self.gridLayout_2.addWidget(self.dataset_split_title, 0, 0, 1, 3)
        self.verticalLayout_3.addWidget(self.dataset_split_container)
        self.verticalLayout_17.addWidget(self.A_datasetOptions)
        self.A4_generateDataset = QtWidgets.QGroupBox(self.baseLayer_4)
        self.A4_generateDataset.setStyleSheet("QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}")
        self.A4_generateDataset.setTitle("")
        self.A4_generateDataset.setObjectName("A4_generateDataset")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.A4_generateDataset)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem36)
        self.pushButton_p4_2 = QtWidgets.QPushButton(self.A4_generateDataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_p4_2.sizePolicy().hasHeightForWidth())
        self.pushButton_p4_2.setSizePolicy(sizePolicy)
        self.pushButton_p4_2.setMinimumSize(QtCore.QSize(208, 40))
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
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem37)
        self.verticalLayout_17.addWidget(self.A4_generateDataset)
        self.A5_progressDisplay = QtWidgets.QGroupBox(self.baseLayer_4)
        self.A5_progressDisplay.setStyleSheet("QGroupBox{\n"
"    background: transparent;\n"
"    border: transparent;\n"
"}")
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
        self.verticalLayout_17.addWidget(self.A5_progressDisplay)
        self.verticalLayout_27.addWidget(self.baseLayer_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_18.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.stackedWidgetPage4)
        self.stackedWidgetPage5 = QtWidgets.QWidget()
        self.stackedWidgetPage5.setObjectName("stackedWidgetPage5")
        self.formLayoutWidget = QtWidgets.QWidget(self.stackedWidgetPage5)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 560, 160, 181))
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
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.adfasfLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.adfasfLabel.setObjectName("adfasfLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.adfasfLabel)
        self.adfasfDial = QtWidgets.QDial(self.formLayoutWidget)
        self.adfasfDial.setObjectName("adfasfDial")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.adfasfDial)
        self.layoutWidget = QtWidgets.QWidget(self.stackedWidgetPage5)
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
        self.widget_9 = QtWidgets.QWidget(self.stackedWidgetPage5)
        self.widget_9.setGeometry(QtCore.QRect(50, 10, 611, 421))
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
        self.pushButton_4.setIcon(icon7)
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
        self.pushButton_12.setIcon(icon7)
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
        self.pushButton_13.setIcon(icon7)
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
        self.pushButton_18.setIcon(icon7)
        self.pushButton_18.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_62.addWidget(self.pushButton_18)
        self.horizontalLayout_61.addWidget(self.widget_25)
        self.verticalLayout_11.addWidget(self.widget_24)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_11.addWidget(self.pushButton_5)
        self.checkBox = QtWidgets.QCheckBox(self.widget_9)
        self.checkBox.setTristate(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_11.addWidget(self.checkBox)
        self.widget_26 = QtWidgets.QWidget(self.stackedWidgetPage5)
        self.widget_26.setGeometry(QtCore.QRect(70, 480, 593, 20))
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
        self.pushButton_20.setIcon(icon7)
        self.pushButton_20.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_64.addWidget(self.pushButton_20)
        self.widget_27 = QtWidgets.QWidget(self.stackedWidgetPage5)
        self.widget_27.setGeometry(QtCore.QRect(70, 510, 593, 38))
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
        self.pushButton_21.setIcon(icon7)
        self.pushButton_21.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_66.addWidget(self.pushButton_21)
        self.horizontalLayout_65.addWidget(self.widget_28)
        self.label_27 = QtWidgets.QLabel(self.stackedWidgetPage5)
        self.label_27.setGeometry(QtCore.QRect(70, 450, 471, 21))
        self.label_27.setStyleSheet("background-color: #ababab;")
        self.label_27.setObjectName("label_27")
        self.comboBox = QtWidgets.QComboBox(self.stackedWidgetPage5)
        self.comboBox.setGeometry(QtCore.QRect(290, 570, 119, 22))
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: lightgray;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.stackedWidget.addWidget(self.stackedWidgetPage5)
        self.stackedWidgetPage6 = QtWidgets.QWidget()
        self.stackedWidgetPage6.setObjectName("stackedWidgetPage6")
        self.A_notesForUser_2 = QtWidgets.QGroupBox(self.stackedWidgetPage6)
        self.A_notesForUser_2.setGeometry(QtCore.QRect(10, 30, 728, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A_notesForUser_2.sizePolicy().hasHeightForWidth())
        self.A_notesForUser_2.setSizePolicy(sizePolicy)
        self.A_notesForUser_2.setMinimumSize(QtCore.QSize(0, 100))
        self.A_notesForUser_2.setMaximumSize(QtCore.QSize(16777215, 120))
        self.A_notesForUser_2.setStyleSheet("QGroupBox#A_notesForUser {\n"
"    border: gray;\n"
"    padding-top: 10px;\n"
"}")
        self.A_notesForUser_2.setTitle("")
        self.A_notesForUser_2.setObjectName("A_notesForUser_2")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.A_notesForUser_2)
        self.verticalLayout_20.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_20.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.textBrowser_p2_3 = QtWidgets.QTextBrowser(self.A_notesForUser_2)
        self.textBrowser_p2_3.setMaximumSize(QtCore.QSize(16777215, 180))
        self.textBrowser_p2_3.setStyleSheet("background-color: transparent;\n"
"border: transparent;")
        self.textBrowser_p2_3.setOpenExternalLinks(True)
        self.textBrowser_p2_3.setObjectName("textBrowser_p2_3")
        self.verticalLayout_20.addWidget(self.textBrowser_p2_3)
        self.qScoreInfo_btn_4 = QtWidgets.QPushButton(self.stackedWidgetPage6)
        self.qScoreInfo_btn_4.setGeometry(QtCore.QRect(90, 130, 32, 28))
        self.qScoreInfo_btn_4.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/icons/advanced_options_icon.png);")
        self.qScoreInfo_btn_4.setText("")
        self.qScoreInfo_btn_4.setIcon(icon6)
        self.qScoreInfo_btn_4.setIconSize(QtCore.QSize(20, 20))
        self.qScoreInfo_btn_4.setObjectName("qScoreInfo_btn_4")
        self.label_19 = QtWidgets.QLabel(self.stackedWidgetPage6)
        self.label_19.setGeometry(QtCore.QRect(40, 200, 645, 217))
        self.label_19.setOpenExternalLinks(True)
        self.label_19.setObjectName("label_19")
        self.stackedWidget.addWidget(self.stackedWidgetPage6)
        self.sidebar = QtWidgets.QWidget(self.splitter)
        self.sidebar.setObjectName("sidebar")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.sidebar)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.splitter_2 = QtWidgets.QSplitter(self.sidebar)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.logsWidget = QtWidgets.QWidget(self.splitter_2)
        self.logsWidget.setObjectName("logsWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.logsWidget)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.logsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_10.addWidget(self.label_13)
        self.logsViewBox = QtWidgets.QTextEdit(self.logsWidget)
        self.logsViewBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.logsViewBox.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.logsViewBox.setReadOnly(True)
        self.logsViewBox.setObjectName("logsViewBox")
        self.verticalLayout_10.addWidget(self.logsViewBox)
        self.tasksWidget = QtWidgets.QWidget(self.splitter_2)
        self.tasksWidget.setObjectName("tasksWidget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tasksWidget)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_15 = QtWidgets.QLabel(self.tasksWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_12.addWidget(self.label_15)
        self.tasksViewBox = QtWidgets.QTextEdit(self.tasksWidget)
        self.tasksViewBox.setObjectName("tasksViewBox")
        self.verticalLayout_12.addWidget(self.tasksViewBox)
        self.verticalLayout_13.addWidget(self.splitter_2)
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1255, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: #3e4348;\n"
"color: white;")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "CryoDataBot"))
        self.sidebtn_0.setText(_translate("MainWindow", "Home"))
        self.sidebtn_1.setText(_translate("MainWindow", "Quick Start"))
        self.sidebtn_2.setText(_translate("MainWindow", "Metadata"))
        self.sidebtn_3.setText(_translate("MainWindow", "Preprocess"))
        self.sidebtn_4.setText(_translate("MainWindow", "Datasets"))
        self.sidebtn_5.setText(_translate("MainWindow", "TEST"))
        self.sidebtn_6.setText(_translate("MainWindow", "Rich Style"))
        self.label_20.setText(_translate("MainWindow", "Home"))
        self.label_17.setText(_translate("MainWindow", "CryoDataBot data storage location:"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.main_save_path_lineedit.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">Valid query format: </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#000000;\">sample</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#ff6969;\">*</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#000000;\">,</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\"> keyword1, keyword2, ... <br/></span><span style=\" font-family:\'Segoe UI\'; font-size:6pt; font-weight:600; color:#ff6969;\">*required</span></p><p><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">Available keywords shown in dropdown. Keywords are connected by boolean operators (AND, OR, NOT). Default is AND.<br/><br/>ex. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#00007f;\">spliceosome AND resolution:[2 TO 4]<br/></span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">ex. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#00007f;\">(spliceosome OR ribonucleoprotein) AND NOT human AND xref_UNIPROTKB:[* TO *]</span></p></body></html>"))
        self.main_save_path_lineedit.setPlaceholderText(_translate("MainWindow", "select a folder"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "placeholder\n"
"\n"
"as\n"
"dfa\n"
"sd\n"
"fas\n"
"\n"
"FIXED HEIGHT scroll (QPlainTextEdit) in expanding scrollarea\n"
"\n"
"df\n"
"as\n"
"df\n"
"asfd\n"
"\n"
"\n"
"filling space"))
        self.baseLayer_1.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.page2TitleLabel_2.setText(_translate("MainWindow", "Quickstart"))
        self.textBrowser_p1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Enter a search term</span><span style=\" font-weight:600; color:#ff6969;\">*</span><span style=\" color:#000000;\"> followed by optional keywords. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; color:#ff6969;\">    </span><span style=\" font-size:6pt; font-weight:600; color:#ff6969;\">*required</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Keywords are connected by boolean operators (AND, OR, NOT). Default is AND.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.ebi.ac.uk/emdb/documentation/search\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; text-decoration: underline; color:#0000ff;\">Query follows EMDB search format.</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">ex.</span><span style=\" color:#007c82;\">  </span><span style=\" color:#00007f;\">spliceosome AND resolution:[2 TO 4]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">ex.  </span><span style=\" color:#00007f;\">(spliceosome OR ribonucleoprotein) AND NOT human AND xref_UNIPROTKB:[* TO *]</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Query"))
        self.lineEdit_15.setPlaceholderText(_translate("MainWindow", "[sample] AND [range_keyword: x TO y] AND [keyword]"))
        self.label_5.setText(_translate("MainWindow", "Refinement"))
        self.pushButton_2.setText(_translate("MainWindow", "refine options"))
        self.label_6.setText(_translate("MainWindow", "Labels"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>CHANGE THIS NAME</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Label manager"))
        self.pushButton_p1_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">this is limiting the window\'s thickness when shrinking btw, prob a better way to go about sizepolicys</span></p></body></html>"))
        self.pushButton_p1_3.setText(_translate("MainWindow", "Generate"))
        self.page2TitleLabel.setText(_translate("MainWindow", "Fetch Metadata"))
        self.label_4.setText(_translate("MainWindow", "CryoDataBot data storage location:"))
        self.lineEdit_p2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">Valid query format: </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#000000;\">sample</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#ff6969;\">*</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:600; color:#000000;\">,</span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\"> keyword1, keyword2, ... <br/></span><span style=\" font-family:\'Segoe UI\'; font-size:6pt; font-weight:600; color:#ff6969;\">*required</span></p><p><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">Available keywords shown in dropdown. Keywords are connected by boolean operators (AND, OR, NOT). Default is AND.<br/><br/>ex. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#00007f;\">spliceosome AND resolution:[2 TO 4]<br/></span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#000000;\">ex. </span><span style=\" font-family:\'Segoe UI\'; font-size:9pt; color:#00007f;\">(spliceosome OR ribonucleoprotein) AND NOT human AND xref_UNIPROTKB:[* TO *]</span></p></body></html>"))
        self.lineEdit_p2.setPlaceholderText(_translate("MainWindow", "select a folder"))
        self.B_enterQuery.setTitle(_translate("MainWindow", "Enter a Search Query"))
        self.textBrowser_p2_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Enter a search term</span><span style=\" font-weight:600; color:#ff6969;\">*</span><span style=\" color:#000000;\"> followed by optional keywords. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; color:#ff6969;\">    </span><span style=\" font-size:6pt; font-weight:600; color:#ff6969;\">*required</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Keywords are connected by boolean operators (AND, OR, NOT). Default is AND.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.ebi.ac.uk/emdb/documentation/search\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; text-decoration: underline; color:#0000ff;\">Query follows EMDB search format.</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">ex.</span><span style=\" color:#007c82;\">  </span><span style=\" color:#00007f;\">spliceosome AND resolution:[2 TO 4]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">ex.  </span><span style=\" color:#00007f;\">(spliceosome OR ribonucleoprotein) AND NOT human AND xref_UNIPROTKB:[* TO *]</span></p></body></html>"))
        self.label_p2.setText(_translate("MainWindow", "Query"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "[sample] AND [range_keyword: x TO y] AND [keyword]"))
        self.lineEdit_12.setPlaceholderText(_translate("MainWindow", "[sample] AND [range_keyword: x TO y] AND [keyword]"))
        self.pushButton_p2_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">this is limiting the window\'s thickness when shrinking btw, prob a better way to go about sizepolicys</span></p></body></html>"))
        self.pushButton_p2_2.setText(_translate("MainWindow", "Download CSV"))
        self.page3TitleLabel.setText(_translate("MainWindow", "Preprocessing"))
        self.A_chooseCSV.setTitle(_translate("MainWindow", "Choose Metadata File"))
        self.lineEdit_p3.setToolTip(_translate("MainWindow", "type or browse (note to self: check that file exists, if not spit the error out to the statusbar)"))
        self.lineEdit_p3.setPlaceholderText(_translate("MainWindow", "metadata file (*.csv)"))
        self.pushButton_p3.setToolTip(_translate("MainWindow", "browse or type"))
        self.B_refineCSV.setTitle(_translate("MainWindow", "[name TBD]"))
        self.qScoreLabel.setText(_translate("MainWindow", "Map Model Fitness (Q score cutoff)"))
        self.similaritySpinBox.setSuffix(_translate("MainWindow", "%"))
        self.mapModelFitnessSpinBox.setSuffix(_translate("MainWindow", "%"))
        self.mapModelFitnessLabel.setText(_translate("MainWindow", "Map Model Fitness (our calculated metric)"))
        self.similarityLabel.setText(_translate("MainWindow", "Similarity threshold:"))
        self.pushButton_p3_4.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">this is limiting the window\'s thickness when shrinking btw, prob a better way to go about sizepolicys</span></p></body></html>"))
        self.pushButton_p3_4.setText(_translate("MainWindow", "[name TBD]"))
        self.page4TitleLabel.setText(_translate("MainWindow", "Generate Dataset"))
        self.A_chooseCSV_2.setTitle(_translate("MainWindow", "Choose Maps and Models to Label"))
        self.label_21.setText(_translate("MainWindow", "Can ignore if did the previous step. Otherwise feel free to select your own list (.csv) of maps and models to download."))
        self.lineEdit_p3_2.setToolTip(_translate("MainWindow", "type or browse (note to self: check that file exists, if not spit the error out to the statusbar)"))
        self.lineEdit_p3_2.setPlaceholderText(_translate("MainWindow", "*.csv of downloaded maps and models"))
        self.pushButton_p3_2.setToolTip(_translate("MainWindow", "browse or type"))
        self.A_datasetOptions.setTitle(_translate("MainWindow", "Select Labels"))
        self.addgroup_btn.setText(_translate("MainWindow", "add group"))
        self.addlabel_btn.setText(_translate("MainWindow", "add label"))
        self.treeWidget_p4.headerItem().setText(1, _translate("MainWindow", "secondary structure"))
        self.treeWidget_p4.headerItem().setText(2, _translate("MainWindow", "residues"))
        self.treeWidget_p4.headerItem().setText(3, _translate("MainWindow", "atoms"))
        __sortingEnabled = self.treeWidget_p4.isSortingEnabled()
        self.treeWidget_p4.setSortingEnabled(False)
        self.treeWidget_p4.topLevelItem(0).setText(0, _translate("MainWindow", "Group 3"))
        self.treeWidget_p4.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Label 2"))
        self.treeWidget_p4.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Label 1"))
        self.treeWidget_p4.topLevelItem(1).setText(0, _translate("MainWindow", "Group 2"))
        self.treeWidget_p4.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Label 5"))
        self.treeWidget_p4.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "Label 4"))
        self.treeWidget_p4.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "Label 3"))
        self.treeWidget_p4.topLevelItem(1).child(3).setText(0, _translate("MainWindow", "Label 2"))
        self.treeWidget_p4.topLevelItem(1).child(4).setText(0, _translate("MainWindow", "Label 1"))
        self.treeWidget_p4.topLevelItem(2).setText(0, _translate("MainWindow", "Group 1"))
        self.treeWidget_p4.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "Label 2"))
        self.treeWidget_p4.topLevelItem(2).child(0).setText(1, _translate("MainWindow", "protein - sheet"))
        self.treeWidget_p4.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "Label 1"))
        self.treeWidget_p4.topLevelItem(2).child(1).setText(1, _translate("MainWindow", "protein - helix"))
        self.treeWidget_p4.topLevelItem(2).child(1).setText(2, _translate("MainWindow", "all"))
        self.treeWidget_p4.setSortingEnabled(__sortingEnabled)
        self.label_p4.setText(_translate("MainWindow", "Cube size:"))
        self.label_p4_2.setText(_translate("MainWindow", "^3"))
        self.validation_label.setText(_translate("MainWindow", "Validation:"))
        self.training_label.setText(_translate("MainWindow", "Training:"))
        self.training_spinBox.setSuffix(_translate("MainWindow", "%"))
        self.testing_label.setText(_translate("MainWindow", "Testing:"))
        self.validation_spinBox.setSuffix(_translate("MainWindow", "%"))
        self.testing_spinBox.setSuffix(_translate("MainWindow", "%"))
        self.dataset_split_title.setText(_translate("MainWindow", "Dataset Split"))
        self.pushButton_p4_2.setText(_translate("MainWindow", "Generate Dataset(s)"))
        self.option1Label_2.setText(_translate("MainWindow", "option 1"))
        self.option2Label.setText(_translate("MainWindow", "option 2"))
        self.option3Label.setText(_translate("MainWindow", "option 3"))
        self.label_2.setText(_translate("MainWindow", "map quality"))
        self.doubleSpinBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>uses qscore</p></body></html>"))
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
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.lineEdit_16.setText(_translate("MainWindow", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy"))
        self.lineEdit_17.setText(_translate("MainWindow", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy"))
        self.label_27.setText(_translate("MainWindow", "these 2 are just for templates (missing/empty base widget so may look weird in python)"))
        self.comboBox.setItemText(1, _translate("MainWindow", "dog"))
        self.comboBox.setItemText(2, _translate("MainWindow", "water"))
        self.textBrowser_p2_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:696; color:#616161;\">This step fetches metadata from EMDB. If you already have a .csv file with the columns: </span><span style=\" color:#616161;\">emdb_id, resolution, fitted_pdbs,</span><span style=\" font-weight:696; color:#616161;\"> you can </span><span style=\" font-weight:696; color:#0000ff;\">skip</span><span style=\" font-weight:696; color:#616161;\"> this step.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:696; color:#616161;\">wtfff u can put rich text in a qlabel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:696; color:#616161;\">steps to recreate:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:696; color:#616161;\">1. add a qlabel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:696; color:#616161;\">2. copy rich text from a qtextedit</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:696; color:#616161;\">3. paste it into the qlabel. now you get the option to edit rich text directly in the qlabel</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt; font-weight:696; color:#616161;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:696; color:#616161;\">convert textedits to labels? the ones that are only insturctions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.google.com/search?q=capybara&amp;rlz=1C1VDKB_enUS971US971&amp;oq=capybara&amp;gs_lcrp=EgZjaHJvbWUqBwgAEAAYjwIyBwgAEAAYjwIyDwgBEC4YQxixAxiABBiKBTINCAIQLhiDARixAxiABDIMCAMQABhDGIAEGIoFMgwIBBAAGEMYgAQYigUyEwgFEC4YgwEYrwEYxwEYsQMYgAQyDQgGEC4YgwEYsQMYgAQyDAgHEAAYQxiABBiKBTIMCAgQABhDGIAEGIoFMg0ICRAAGIMBGLEDGIAE0gEIMTE4N2owajeoAgCwAgA&amp;sourceid=chrome&amp;ie=UTF-8\"><span style=\" text-decoration: underline; color:#0000ff;\">links work too?</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9pt;\"><br /></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Logs"))
        self.label_15.setText(_translate("MainWindow", "Running Tasks"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
