import datetime
import time
import pyautogui
from datetime import timedelta, date
import re
import pytesseract
from PIL import Image
from pyperclip import paste

'''
Buum- a retail program built on Firebird 3.0 - restricted to only use client side application
Sensmax- a website that tracks how many visitors visit the store gets count from a sensor in store
Pyautogui is used to interact with Buum
Pytesseract is used to locate the correct line on screen will be used to read the date
Future of the project might include web scraping to get info from Sensmax
'''
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\szimmerman\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


# Use this function to strip all unnecessary symbols that pytesseract might pick up
# Pytesseract is very specific about what symbols it picks up
def get_value_without_symbols(value):
    value = value.replace(' ', '')
    value = value.replace('¢', '')
    value = value.replace('€', '')
    value = value.strip()
    return value


# this clicks on the cell where the column and row intersect and returns the value
def get_cell_value(column, row):
    shot = pyautogui.screenshot(region=(column[0]+2, row[1]+4, column[2]+4, row[3]+4))
    screen_value = pytesseract.image_to_string(shot)
    screen_value = get_value_without_symbols(screen_value)
    return screen_value


def get_yesterday_sales():
    # these lines find buttons on the pictures and click them on
    # these lines open the report needed to get the value
    pyautogui.click('clickON.png')
    time.sleep(0.1)
    pyautogui.click('sale_rep.png')
    pyautogui.click('aruanded.png')

    # sometimes it takes a few seconds to open the report this should compensate for that
    time.sleep(5)

    # this block uses the line marker arrow and gets to the bottom of the table
    arrow_start = pyautogui.locateOnScreen('arrow.png')
    pyautogui.click('arrow.png')
    pyautogui.press('down', presses=30)
    
    # this selects the second to last line

    pyautogui.press('up')

    # these lines find the correct column and line for the sales yesterday
    sum_km = pyautogui.locateOnScreen('sales.png')
    bills = pyautogui.locateOnScreen('arveid.png')
    arrow_final = pyautogui.locateOnScreen('arrow.png')
    date_yesterday = get_date_yesterday(arrow_final)
    final_sales = get_cell_value(sum_km, arrow_final)
    final_bills = get_cell_value(bills, arrow_final)
    final_values = [final_sales, final_bills, date_yesterday]
    return final_values


sales = get_yesterday_sales()
print(sales)
