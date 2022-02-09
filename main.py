import openpyxl

from pdf_work import extract_text
import variable_list
from excel_work import excel_open
import easygui


variable_list.HBL = easygui.enterbox("ANALINK HBL NUMBER: ")
#print(variable_list.HBL)

LINK_BOOKING = 'BOOKING/'
extract_text(LINK_BOOKING)
#print(variable_list.BOOKING_NUMBER)
#print(variable_list.VESSEL)

link_form = 'FORM/FORM_BINEX.xlsx'
excel_open(link_form)
#print(variable_list.CONT_SIZE)
#print(variable_list.ETD)
#print(variable_list.ETA)
#print(variable_list.DESTINATION)
#print(variable_list.CLOSING_DATE)
#print(variable_list.CLOSING_TIME)

#ko hiểu sao dòng này ko mở được file, ko biết làm sao để mở file
#open(link_form)
#open("D:\\DATA\HOC_PYTHON\READ_BOOKING\BOOKING\\SGNM72961600.pdf")

#khi save file excel kết quả làm header trong sheet DRAFT bị xóa, ko hiểu tại sao... nên phải tạo file final excel để copy từ file đã save qua