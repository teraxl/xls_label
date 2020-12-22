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
        QtGui.QFontDatabase.addApplicationFont("fonts/NovaFlat-Regular.ttf")
        font = QtGui.QFont("Nova Flat")
        # font.setBold(True)
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
        self.lineEdit.setStyleSheet(
            "QLineEdit {"
            "color: darkslategrey;"
            "background-color: #e1e2e3;"
            "border: 4px solid grey;"
            "border-radius: 5px;"
            "border-width:2px;"
            "}"
        )

        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 230, 281, 51))
        self.pushButton.setObjectName("pushButton")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setText("СГЕНЕРИРОВАТЬ ФАЙЛ")
        self.pushButton.setStyleSheet(
            "QPushButton {"
            "color: darkslategrey;"
            "background-color: #05B8CC;"
            "border: 2px solid grey;"
            "border-radius: 5px;"
            "border-width:2px;"
            "}"
        )
        Form.setWindowTitle("Наклейки")
        QtCore.QMetaObject.connectSlotsByName(Form)
