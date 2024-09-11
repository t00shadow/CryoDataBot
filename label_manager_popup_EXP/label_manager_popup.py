# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/c/Users/noelu/CryoDataBot/label_manager_popup_EXP/label_manager_popup.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(686, 546)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addgroup_btn = QtWidgets.QPushButton(self.widget_3)
        self.addgroup_btn.setObjectName("addgroup_btn")
        self.horizontalLayout_2.addWidget(self.addgroup_btn)
        self.delgroup_btn = QtWidgets.QPushButton(self.widget_3)
        self.delgroup_btn.setObjectName("delgroup_btn")
        self.horizontalLayout_2.addWidget(self.delgroup_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget_3)
        self.listWidget_groups = QtWidgets.QListWidget(self.widget)
        self.listWidget_groups.setObjectName("listWidget_groups")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_groups.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_groups.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_groups.addItem(item)
        self.verticalLayout.addWidget(self.listWidget_groups)
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addlabel_btn = QtWidgets.QPushButton(self.widget_4)
        self.addlabel_btn.setObjectName("addlabel_btn")
        self.horizontalLayout_3.addWidget(self.addlabel_btn)
        self.dellabel_btn = QtWidgets.QPushButton(self.widget_4)
        self.dellabel_btn.setObjectName("dellabel_btn")
        self.horizontalLayout_3.addWidget(self.dellabel_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.listWidget_labels = QtWidgets.QListWidget(self.widget_2)
        self.listWidget_labels.setObjectName("listWidget_labels")
        self.verticalLayout_2.addWidget(self.listWidget_labels)
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.addgroup_btn.setText(_translate("Dialog", "+ Add group"))
        self.delgroup_btn.setText(_translate("Dialog", "- Delete group"))
        __sortingEnabled = self.listWidget_groups.isSortingEnabled()
        self.listWidget_groups.setSortingEnabled(False)
        item = self.listWidget_groups.item(0)
        item.setText(_translate("Dialog", "Group 1"))
        item = self.listWidget_groups.item(1)
        item.setText(_translate("Dialog", "Group 2"))
        item = self.listWidget_groups.item(2)
        item.setText(_translate("Dialog", "Group 3"))
        self.listWidget_groups.setSortingEnabled(__sortingEnabled)
        self.addlabel_btn.setText(_translate("Dialog", "+ Add label"))
        self.dellabel_btn.setText(_translate("Dialog", "- Delete label"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
