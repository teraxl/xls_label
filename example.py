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


def main():
    wb = load_workbook(filename='наклейки.xlsx', read_only=False, data_only=True)
    ws = wb.active
    print(ws.column_dimensions['A'].width)
    print(ws.row_dimensions[1].height)
    print(ws.page_setup)


if __name__ == '__main__':
    main()
