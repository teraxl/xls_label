#!/usr/bin/python3w
# coding=utf-8

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDir
from guiexcel import Ui_Form
import sys
import os
from xlFile import xlLabel

file = "test2.xlsx"

mOS = ['nt', 'posix']
slash = ''


class MyWidget(QtWidgets.QWidget):

    def __init__(self):
        super(MyWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        xl = xlLabel()
        xl.getValue(self.ui.lineEdit.text())
        dir_name = QDir.currentPath()
        message = "Файл был создан в данной директории:"
        if os.name in mOS:
            _SLASH_ = "/"
        else:
            _SLASH_ = "\\"

        str_all = str(message + '\n' + dir_name + _SLASH_ + file)
        msg = QMessageBox(QMessageBox.Warning, "Файл создан", str_all, QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec()

"""
        m = msg.exec()

        if m == QMessageBox.Ok:
           mmm = QMessageBox(QMessageBox.Warning, "Ok", "OKOKO", QMessageBox.Ok)
           mmm.exec()
        if m == QMessageBox.Cancel:
           mmm = QMessageBox(QMessageBox.Warning, "Cancel", "OKOKO", QMessageBox.Ok)
           mmm.exec()
"""

app = QtWidgets.QApplication([])
application = MyWidget()
application.show()

sys.exit(app.exec())
