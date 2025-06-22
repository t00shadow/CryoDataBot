# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/c/Users/noelu/CryoDataBot/quickstart_labels_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 464)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.A_datasetOptions = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A_datasetOptions.sizePolicy().hasHeightForWidth())
        self.A_datasetOptions.setSizePolicy(sizePolicy)
        self.A_datasetOptions.setStyleSheet("QGroupBox#A_datasetOptions {\n"
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
        self.A_datasetOptions.setObjectName("A_datasetOptions")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.A_datasetOptions)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_5 = QtWidgets.QWidget(self.A_datasetOptions)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_17.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.addgroup_btn_3 = QtWidgets.QPushButton(self.widget_5)
        self.addgroup_btn_3.setObjectName("addgroup_btn_3")
        self.horizontalLayout_17.addWidget(self.addgroup_btn_3)
        self.addlabel_btn_3 = QtWidgets.QPushButton(self.widget_5)
        self.addlabel_btn_3.setObjectName("addlabel_btn_3")
        self.horizontalLayout_17.addWidget(self.addlabel_btn_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.widget_5)
        self.A1_featureLabels_3 = QtWidgets.QWidget(self.A_datasetOptions)
        self.A1_featureLabels_3.setMinimumSize(QtCore.QSize(0, 200))
        self.A1_featureLabels_3.setObjectName("A1_featureLabels_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.A1_featureLabels_3)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.treeWidget_p4_3 = QtWidgets.QTreeWidget(self.A1_featureLabels_3)
        self.treeWidget_p4_3.setStyleSheet("QTreeWidget {\n"
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
        self.treeWidget_p4_3.setAlternatingRowColors(False)
        self.treeWidget_p4_3.setAnimated(True)
        self.treeWidget_p4_3.setObjectName("treeWidget_p4_3")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_p4_3)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_p4_3)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_p4_3)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.horizontalLayout_13.addWidget(self.treeWidget_p4_3)
        self.verticalLayout_5.addWidget(self.A1_featureLabels_3)
        self.A2_cubeSize_3 = QtWidgets.QGroupBox(self.A_datasetOptions)
        self.A2_cubeSize_3.setTitle("")
        self.A2_cubeSize_3.setObjectName("A2_cubeSize_3")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.A2_cubeSize_3)
        self.horizontalLayout_14.setContentsMargins(0, -1, -1, 25)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_p4_5 = QtWidgets.QLabel(self.A2_cubeSize_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_p4_5.setFont(font)
        self.label_p4_5.setObjectName("label_p4_5")
        self.horizontalLayout_14.addWidget(self.label_p4_5)
        self.spinBox_6 = QtWidgets.QSpinBox(self.A2_cubeSize_3)
        self.spinBox_6.setStyleSheet("QSpinBox, \n"
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
        self.spinBox_6.setAccelerated(True)
        self.spinBox_6.setMinimum(1)
        self.spinBox_6.setMaximum(128)
        self.spinBox_6.setProperty("value", 64)
        self.spinBox_6.setObjectName("spinBox_6")
        self.horizontalLayout_14.addWidget(self.spinBox_6)
        self.label_p4_6 = QtWidgets.QLabel(self.A2_cubeSize_3)
        self.label_p4_6.setObjectName("label_p4_6")
        self.horizontalLayout_14.addWidget(self.label_p4_6)
        spacerItem1 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.A2_cubeSize_3)
        self.dataset_split_container_3 = QtWidgets.QWidget(self.A_datasetOptions)
        self.dataset_split_container_3.setStyleSheet("QSpinBox, \n"
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
        self.dataset_split_container_3.setObjectName("dataset_split_container_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dataset_split_container_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 15)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.validation_label_3 = QtWidgets.QLabel(self.dataset_split_container_3)
        self.validation_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.validation_label_3.setObjectName("validation_label_3")
        self.gridLayout_4.addWidget(self.validation_label_3, 1, 4, 1, 1)
        self.training_label_3 = QtWidgets.QLabel(self.dataset_split_container_3)
        self.training_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.training_label_3.setObjectName("training_label_3")
        self.gridLayout_4.addWidget(self.training_label_3, 1, 0, 1, 1)
        self.training_spinBox_3 = QtWidgets.QSpinBox(self.dataset_split_container_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.training_spinBox_3.sizePolicy().hasHeightForWidth())
        self.training_spinBox_3.setSizePolicy(sizePolicy)
        self.training_spinBox_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.training_spinBox_3.setMaximum(100)
        self.training_spinBox_3.setObjectName("training_spinBox_3")
        self.gridLayout_4.addWidget(self.training_spinBox_3, 1, 1, 1, 1)
        self.testing_label_3 = QtWidgets.QLabel(self.dataset_split_container_3)
        self.testing_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.testing_label_3.setObjectName("testing_label_3")
        self.gridLayout_4.addWidget(self.testing_label_3, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 1, 6, 1, 1)
        self.validation_spinBox_3 = QtWidgets.QSpinBox(self.dataset_split_container_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validation_spinBox_3.sizePolicy().hasHeightForWidth())
        self.validation_spinBox_3.setSizePolicy(sizePolicy)
        self.validation_spinBox_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.validation_spinBox_3.setMaximum(100)
        self.validation_spinBox_3.setObjectName("validation_spinBox_3")
        self.gridLayout_4.addWidget(self.validation_spinBox_3, 1, 5, 1, 1)
        self.testing_spinBox_3 = QtWidgets.QSpinBox(self.dataset_split_container_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testing_spinBox_3.sizePolicy().hasHeightForWidth())
        self.testing_spinBox_3.setSizePolicy(sizePolicy)
        self.testing_spinBox_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.testing_spinBox_3.setMaximum(100)
        self.testing_spinBox_3.setObjectName("testing_spinBox_3")
        self.gridLayout_4.addWidget(self.testing_spinBox_3, 1, 3, 1, 1)
        self.dataset_split_title_3 = QtWidgets.QLabel(self.dataset_split_container_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.dataset_split_title_3.setFont(font)
        self.dataset_split_title_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dataset_split_title_3.setObjectName("dataset_split_title_3")
        self.gridLayout_4.addWidget(self.dataset_split_title_3, 0, 0, 1, 3)
        self.verticalLayout_5.addWidget(self.dataset_split_container_3)
        self.verticalLayout.addWidget(self.A_datasetOptions)
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
        self.A_datasetOptions.setTitle(_translate("Dialog", "Select Labels"))
        self.addgroup_btn_3.setText(_translate("Dialog", "add group"))
        self.addlabel_btn_3.setText(_translate("Dialog", "add label"))
        self.treeWidget_p4_3.headerItem().setText(1, _translate("Dialog", "secondary structure"))
        self.treeWidget_p4_3.headerItem().setText(2, _translate("Dialog", "residues"))
        self.treeWidget_p4_3.headerItem().setText(3, _translate("Dialog", "atoms"))
        __sortingEnabled = self.treeWidget_p4_3.isSortingEnabled()
        self.treeWidget_p4_3.setSortingEnabled(False)
        self.treeWidget_p4_3.topLevelItem(0).setText(0, _translate("Dialog", "Group 3"))
        self.treeWidget_p4_3.topLevelItem(0).child(0).setText(0, _translate("Dialog", "Label 2"))
        self.treeWidget_p4_3.topLevelItem(0).child(1).setText(0, _translate("Dialog", "Label 1"))
        self.treeWidget_p4_3.topLevelItem(1).setText(0, _translate("Dialog", "Group 2"))
        self.treeWidget_p4_3.topLevelItem(1).child(0).setText(0, _translate("Dialog", "Label 5"))
        self.treeWidget_p4_3.topLevelItem(1).child(1).setText(0, _translate("Dialog", "Label 4"))
        self.treeWidget_p4_3.topLevelItem(1).child(2).setText(0, _translate("Dialog", "Label 3"))
        self.treeWidget_p4_3.topLevelItem(1).child(3).setText(0, _translate("Dialog", "Label 2"))
        self.treeWidget_p4_3.topLevelItem(1).child(4).setText(0, _translate("Dialog", "Label 1"))
        self.treeWidget_p4_3.topLevelItem(2).setText(0, _translate("Dialog", "Group 1"))
        self.treeWidget_p4_3.topLevelItem(2).child(0).setText(0, _translate("Dialog", "Label 2"))
        self.treeWidget_p4_3.topLevelItem(2).child(0).setText(1, _translate("Dialog", "protein - sheet"))
        self.treeWidget_p4_3.topLevelItem(2).child(1).setText(0, _translate("Dialog", "Label 1"))
        self.treeWidget_p4_3.topLevelItem(2).child(1).setText(1, _translate("Dialog", "protein - helix"))
        self.treeWidget_p4_3.topLevelItem(2).child(1).setText(2, _translate("Dialog", "all"))
        self.treeWidget_p4_3.setSortingEnabled(__sortingEnabled)
        self.label_p4_5.setText(_translate("Dialog", "Cube size:"))
        self.label_p4_6.setText(_translate("Dialog", "^3"))
        self.validation_label_3.setText(_translate("Dialog", "Validation:"))
        self.training_label_3.setText(_translate("Dialog", "Training:"))
        self.training_spinBox_3.setSuffix(_translate("Dialog", "%"))
        self.testing_label_3.setText(_translate("Dialog", "Testing:"))
        self.validation_spinBox_3.setSuffix(_translate("Dialog", "%"))
        self.testing_spinBox_3.setSuffix(_translate("Dialog", "%"))
        self.dataset_split_title_3.setText(_translate("Dialog", "Dataset Split"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
