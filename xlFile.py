from openpyxl.styles import Font, colors, Border, Side, Alignment
from openpyxl.worksheet.page import PageMargins, PrintOptions, PrintPageSetup
from openpyxl import load_workbook, Workbook
from openpyxl.worksheet import worksheet


class xlLabel(object):

    def __init__(self):
        pass

    def getValue(self, name=''):
        # value = [59.75, 19.14]
        # value = [59.55, 107.74]
        value = [59.55, 15.38]
        colsVal = ['A', 'B', 'C', 'D', 'E']
        rowVal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        fontType = Font(name='Calibri', sz=11, color=colors.BLACK, bold=True)
        filename = 'наклейки.xlsx'
        wb = Workbook()
        sheet = wb.active
        rutilink = "\nРуТиЛинк\n +7 (961) 518-33-65"
        vvod = name

        _dict_ = {
            1: "RTL00000",
            2: "RTL0000",
            3: "RTL000",
            4: "RTL00",
            5: "RTL0",
            6: "RTL",
        }

        temp = int(vvod)

        if len(vvod) in _dict_:
            for i in range(1, 14):
                for j in range(1, 6):
                    sheet.cell(i, j).value = _dict_[len(vvod)] + str(temp) + rutilink
                    temp = (temp + 1)

        word_wrap_string = Alignment(wrapText=True, horizontal="center", vertical='center')
        double_border_side = Side(border_style='dotted')
        square_border = Border(top=double_border_side,
                               right=double_border_side,
                               bottom=double_border_side,
                               left=double_border_side)

        margins_tblr = 0.1968  # 0.393701/2

        sheet.page_margins = PageMargins(left=margins_tblr, right=margins_tblr, top=margins_tblr, bottom=margins_tblr)
        sheet.sheet_properties.pageSetUpPr.fitToPage = True
        sheet.print_area = "A1:E13"
        sheet.page_setup = PrintPageSetup(worksheet=sheet, orientation='portrait', paperSize=sheet.PAPERSIZE_A4,
                                          fitToHeight=1, fitToWidth=1, scale=100, horizontalDpi=300, verticalDpi=300)
        sheet.page_setup = PrintOptions(horizontalCentered=True, verticalCentered=True)

        for i in range(1, 6):
            for j in range(1, 14):
                sheet.cell(j, i).border = square_border
                sheet.cell(j, i).font = fontType
                sheet.cell(j, i).alignment = word_wrap_string

        for cols in colsVal:
            for row in rowVal:
                sheet.column_dimensions[cols].width = value[1]
                sheet.row_dimensions[row].height = value[0]

        wb.save(filename)
