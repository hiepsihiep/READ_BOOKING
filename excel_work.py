import openpyxl
import variable_list


def excel_open(link_form):
    wb = openpyxl.load_workbook(link_form)
    sheet = wb['SUMMARY INFO']
    sheet['C6'] = variable_list.VESSEL
    sheet['C3'] = variable_list.BOOKING_NUMBER
    sheet['C4'] = variable_list.BOOKING_NUMBER
    sheet['C7'] = variable_list.ETD
    sheet['C8'] = variable_list.ETA
    sheet['C9'] = variable_list.DESTINATION
    sheet['C11'] = variable_list.CLOSING_DATE
    sheet['E11'] = variable_list.CLOSING_TIME
    sheet['C5'] = variable_list.HBL
    if variable_list.CONT_SIZE == "4H":
        variable_list.CONT_SIZE = "40'HC"
    else:
        variable_list.CONT_SIZE = "40'DC"
    sheet['C10'] = variable_list.CONT_SIZE

    wb.save(link_form)
