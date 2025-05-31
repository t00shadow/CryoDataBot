# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/c/Users/noelu/CryoDataBot/quickstart_preprocessing_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(398, 293)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.B_refineCSV = QtWidgets.QGroupBox(Dialog)
        self.B_refineCSV.setStyleSheet("QGroupBox#B_refineCSV {\n"
"    border-radius: 20px;\n"
"    background-color: transparent;\n"
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
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.widget_2 = QtWidgets.QWidget(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet("QSpinBox, \n"
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
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.clearQScore_btn_2 = QtWidgets.QPushButton(self.widget_2)
        self.clearQScore_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearQScore_btn_2.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.clearQScore_btn_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/refresh-cw-alt-3-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearQScore_btn_2.setIcon(icon)
        self.clearQScore_btn_2.setObjectName("clearQScore_btn_2")
        self.gridLayout_5.addWidget(self.clearQScore_btn_2, 0, 2, 1, 1)
        self.widget_14 = QtWidgets.QWidget(self.widget_2)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.mapModelFitnessLabel_2 = QtWidgets.QLabel(self.widget_14)
        self.mapModelFitnessLabel_2.setObjectName("mapModelFitnessLabel_2")
        self.horizontalLayout_26.addWidget(self.mapModelFitnessLabel_2)
        self.mmfInfo_btn_2 = QtWidgets.QPushButton(self.widget_14)
        self.mmfInfo_btn_2.setStyleSheet("background-color: transparent;")
        self.mmfInfo_btn_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/info-circle-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mmfInfo_btn_2.setIcon(icon1)
        self.mmfInfo_btn_2.setObjectName("mmfInfo_btn_2")
        self.horizontalLayout_26.addWidget(self.mmfInfo_btn_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem)
        self.gridLayout_5.addWidget(self.widget_14, 2, 0, 1, 1)
        self.clearMMF_btn_2 = QtWidgets.QPushButton(self.widget_2)
        self.clearMMF_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearMMF_btn_2.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.clearMMF_btn_2.setText("")
        self.clearMMF_btn_2.setIcon(icon)
        self.clearMMF_btn_2.setObjectName("clearMMF_btn_2")
        self.gridLayout_5.addWidget(self.clearMMF_btn_2, 2, 2, 1, 1)
        self.widget_15 = QtWidgets.QWidget(self.widget_2)
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.similarityLabel_2 = QtWidgets.QLabel(self.widget_15)
        self.similarityLabel_2.setObjectName("similarityLabel_2")
        self.horizontalLayout_27.addWidget(self.similarityLabel_2)
        self.simInfo_btn_2 = QtWidgets.QPushButton(self.widget_15)
        self.simInfo_btn_2.setStyleSheet("background-color: transparent;")
        self.simInfo_btn_2.setText("")
        self.simInfo_btn_2.setIcon(icon1)
        self.simInfo_btn_2.setObjectName("simInfo_btn_2")
        self.horizontalLayout_27.addWidget(self.simInfo_btn_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem1)
        self.gridLayout_5.addWidget(self.widget_15, 1, 0, 1, 1)
        self.widget_13 = QtWidgets.QWidget(self.widget_2)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.qScoreLabel_2 = QtWidgets.QLabel(self.widget_13)
        self.qScoreLabel_2.setObjectName("qScoreLabel_2")
        self.horizontalLayout_25.addWidget(self.qScoreLabel_2)
        self.qScoreInfo_btn_2 = QtWidgets.QPushButton(self.widget_13)
        self.qScoreInfo_btn_2.setStyleSheet("background-color: transparent;")
        self.qScoreInfo_btn_2.setText("")
        self.qScoreInfo_btn_2.setIcon(icon1)
        self.qScoreInfo_btn_2.setObjectName("qScoreInfo_btn_2")
        self.horizontalLayout_25.addWidget(self.qScoreInfo_btn_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem2)
        self.gridLayout_5.addWidget(self.widget_13, 0, 0, 1, 1)
        self.qScoreDoubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.qScoreDoubleSpinBox_2.setAccelerated(True)
        self.qScoreDoubleSpinBox_2.setMaximum(1.0)
        self.qScoreDoubleSpinBox_2.setSingleStep(0.01)
        self.qScoreDoubleSpinBox_2.setObjectName("qScoreDoubleSpinBox_2")
        self.gridLayout_5.addWidget(self.qScoreDoubleSpinBox_2, 0, 1, 1, 1)
        self.mapModelFitnessSpinBox_2 = QtWidgets.QSpinBox(self.widget_2)
        self.mapModelFitnessSpinBox_2.setAccelerated(True)
        self.mapModelFitnessSpinBox_2.setMaximum(100)
        self.mapModelFitnessSpinBox_2.setObjectName("mapModelFitnessSpinBox_2")
        self.gridLayout_5.addWidget(self.mapModelFitnessSpinBox_2, 2, 1, 1, 1)
        self.similaritySpinBox_2 = QtWidgets.QSpinBox(self.widget_2)
        self.similaritySpinBox_2.setAccelerated(True)
        self.similaritySpinBox_2.setMaximum(100)
        self.similaritySpinBox_2.setProperty("value", 100)
        self.similaritySpinBox_2.setObjectName("similaritySpinBox_2")
        self.gridLayout_5.addWidget(self.similaritySpinBox_2, 1, 1, 1, 1)
        self.clearSim_btn_2 = QtWidgets.QPushButton(self.widget_2)
        self.clearSim_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearSim_btn_2.setStyleSheet("background-color: white;\n"
"border-radius: 4;")
        self.clearSim_btn_2.setText("")
        self.clearSim_btn_2.setIcon(icon)
        self.clearSim_btn_2.setObjectName("clearSim_btn_2")
        self.gridLayout_5.addWidget(self.clearSim_btn_2, 1, 2, 1, 1)
        self.horizontalLayout_18.addWidget(self.widget_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem3)
        self.verticalLayout_9.addWidget(self.widget_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.B_refineCSV)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.B_refineCSV.setTitle(_translate("Dialog", "Preprocessing Options"))
        self.mapModelFitnessLabel_2.setText(_translate("Dialog", "Map Model Fitness Threshold:"))
        self.similarityLabel_2.setText(_translate("Dialog", "Similarity Threshold:"))
        self.qScoreLabel_2.setText(_translate("Dialog", "Q-Score Threshold:"))
        self.mapModelFitnessSpinBox_2.setSuffix(_translate("Dialog", "%"))
        self.similaritySpinBox_2.setSuffix(_translate("Dialog", "%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
