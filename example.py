# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      СашаНастя
#
# Created:     24.10.2019
# Copyright:   (c) СашаНастя 2019
# Licence:     <your licence>
# -------------------------------------------------------------------------------
from xlFile import xlLabel
import os
from openpyxl import load_workbook
from openpyxl import workbook, worksheet

def mains():
    wb = workbook.Workbook()
    ws = wb.active

    ws.cell(1, 1).value = 10

    wb.save("my.xlsx")


if __name__ == '__main__':
    mains()
