import time

import pyautogui
from datetime import timedelta, date
from PIL import Image
from pyperclip import paste

'''
Buum- a retail program built on Firebird 3.0 - restricted to only use client side application
Sensmax- a website that tracks how many visitors visit the store gets count from a sensor in store
Pyautogui is used to interact with Buum
Pytesseract is used to locate the correct line on screen will be used to read the date
Future of the project might include web scraping to get info from Sensmax
'''


# this clicks on the cell where the column and row intersect and returns the value
def get_cell_value(column, row):
    pyautogui.click(column[0] + 10, row[1] + 5, clicks=3)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    return paste()


def get_yesterday_sales():
    # these lines find buttons on the pictures and click them on
    # these lines open the report needed to get the value
    pyautogui.click('clickON.png')
    pyautogui.click('sale_rep.png')
    pyautogui.click('aruanded.png')

    # sometimes it takes a few seconds to open the report this should compensate for that
    time.sleep(5)

    # this block uses the line marker arrow and gets to the bottom of the table
    arrow_start = pyautogui.locateOnScreen('arrow.png')
    pyautogui.click('arrow.png')
    pyautogui.press('down', presses=30)
    arrow_end = pyautogui.locateOnScreen('arrow.png')
    while arrow_start != arrow_end:
        arrow_start = pyautogui.locateOnScreen('arrow.png')
        pyautogui.press('down')
        arrow_end = pyautogui.locateOnScreen('arrow.png')

    # this selects the second to last line
    if arrow_start == arrow_end:
        pyautogui.press('up')

    # these lines find the correct column and line for the sales yesterday
    sum_km = pyautogui.locateOnScreen('sales.png')
    arrow_final = pyautogui.locateOnScreen('arrow.png')
    final_sales = get_cell_value(sum_km, arrow_final)
    return final_sales


