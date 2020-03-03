# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\guiexcel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QIntValidator


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(302, 297)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 281, 200))
        self.lineEdit.setMaximumSize(QtCore.QSize(281, 200))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setMaxLength(6);
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(QIntValidator(0, 999999, Form))
        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 230, 281, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Сгенерировать xls файл")
        Form.setWindowTitle("Label")
        QtCore.QMetaObject.connectSlotsByName(Form)