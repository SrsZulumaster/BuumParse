import pyautogui
import time

from get_cell import get_cell_value


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
    pyautogui.click('arrow.png')
    pyautogui.press('down', presses=30)

    # this selects the second to last line, temporary until I figure out file operations
    pyautogui.press('up')

    # these lines find the correct column and line for the sales yesterday
    date = pyautogui.locateOnScreen('date.png')
    sum_km = pyautogui.locateOnScreen('sales.png')
    bills = pyautogui.locateOnScreen('arveid.png')
    arrow_final = pyautogui.locateOnScreen('arrow.png')  # this is the final location of the line pointer arrow
    final_sales = get_cell_value(sum_km, arrow_final)
    time.sleep(0.5)
    final_bills = get_cell_value(bills, arrow_final)
    time.sleep(0.5)
    date_of_sale = get_cell_value(date, arrow_final)
    final_values = [final_sales, final_bills, date_of_sale]
    return final_values