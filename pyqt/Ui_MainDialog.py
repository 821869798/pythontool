# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainDialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.setEnabled(True)
        MainDialog.resize(580, 347)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainDialog.sizePolicy().hasHeightForWidth())
        MainDialog.setSizePolicy(sizePolicy)
        MainDialog.setSizeGripEnabled(False)
        self.button = QtWidgets.QPushButton(MainDialog)
        self.button.setGeometry(QtCore.QRect(390, 270, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.lineEdit = QtWidgets.QLineEdit(MainDialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 140, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(MainDialog)
        self.label.setGeometry(QtCore.QRect(290, 140, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        _translate = QtCore.QCoreApplication.translate
        MainDialog.setWindowTitle(_translate("MainDialog", "主窗口"))
        self.button.setText(_translate("MainDialog", "更新"))
        self.label.setText(_translate("MainDialog", "TextLabel"))

