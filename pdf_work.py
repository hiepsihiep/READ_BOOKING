import pdfplumber
import os
import variable_list

def extract_text(LINK_BOOKING):
    file_name = os.listdir(LINK_BOOKING)
    with pdfplumber.open(LINK_BOOKING+file_name[0]) as pdf:
        first_page = pdf.pages[0]
        booking_text = first_page.extract_text()

    VSLstart_index = booking_text.find("1st Vessel/Voyage :")
    VSLend_index = booking_text.find("T/S Port : Call Sign")
    variable_list.VESSEL = booking_text[VSLstart_index + 20: VSLend_index-6]

    NUMBERstart_index = booking_text.find("Booking Number")
    variable_list.BOOKING_NUMBER = booking_text[NUMBERstart_index + 17: NUMBERstart_index + 29]

    CONTSIZEstart_index = booking_text.find("Equipment Size")
    CONTSIZEend_index = booking_text.find("Equipment Qty")
    variable_list.CONT_SIZE = booking_text[CONTSIZEstart_index + 17: CONTSIZEend_index-1]

    ETDstart_index = booking_text.find("ETD")
    variable_list.ETD = booking_text[ETDstart_index + 6: ETDstart_index + 16]

    ETAstart_index = booking_text.find("ETA")
    variable_list.ETA = booking_text[ETAstart_index + 6: ETAstart_index + 16]

    DESTINATIONstart_index = booking_text.find("Port of Discharging")
    DESTINATIONend_index = booking_text.find("TML : GLOBAL TERMINAL")
    variable_list.DESTINATION = booking_text[DESTINATIONstart_index + 22: DESTINATIONend_index-1]

    CLOSINGstart_index = booking_text.find("Return Facility")
    variable_list.CLOSING_DATE = booking_text[CLOSINGstart_index + 22: CLOSINGstart_index + 32]
    variable_list.CLOSING_TIME = booking_text[CLOSINGstart_index + 33: CLOSINGstart_index + 38]