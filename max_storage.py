import time

import pyautogui
import pytesseract

from get_cell import get_cell_number, get_cell_string

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\szimmerman\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def open_article():
    pyautogui.keyDown("ctrlleft")
    pyautogui.press("r")
    pyautogui.keyUp("ctrlleft")


def send_max_items():
    ''' Ladu-Ladu-kogus laos- <> -ok'''

    pyautogui.click("py_auto_pics/ladu.png")
    pyautogui.click("py_auto_pics/ladu.png")
    time.sleep(2)
    pyautogui.click("py_auto_pics/Kogus_laos.png")
    time.sleep(0.5)
    pyautogui.click("py_auto_pics/max_kogus.png")
    pyautogui.click("py_auto_pics/OK_sign.png")
    time.sleep(20)
    line = pyautogui.locateOnScreen("py_auto_pics/arrow.png")
    column = pyautogui.locateOnScreen("py_auto_pics/suurus.png")
    size = pyautogui.screenshot(region=(column[0], line[1], column[2], line[3]))
    EAN_cell = pyautogui.locateOnScreen("py_auto_pics/ribakood.png")
    EAN = get_cell_number(row=line, column=EAN_cell)
    open_article()
    time.sleep(2)
    pyautogui.click("py_auto_pics/lao_info.png")
    pyautogui.locateOnScreen(size)
    line = pyautogui.locateOnScreen("py_auto_pics/arrow.png")
    available_storage = pyautogui.locateOnScreen("py_auto_pics/kogus.png")
    maximum_allowed = pyautogui.locateOnScreen("py_auto_pics/maksimumkogus.png")
    storage_value = get_cell_number(row=line, column=available_storage)
    maximum_value = get_cell_number(row=line, column=maximum_allowed)
    send_amount = storage_value - maximum_value
    ladu = pyautogui.locateOnScreen("py_auto_pics/artikli_ladu.png")
    get_cell_string(ladu, line)
    if storage_value != maximum_value:
        send_amount = int(storage_value) - int(maximum_value)
        ladu = pyautogui.locateOnScreen("py_auto_pics/artikli_ladu.png")
        line = pyautogui.locateOnScreen("py_auto_pics/arrow.png",region=(100,100,100,100))
        get_cell_string(ladu, line)

    else:
        pass



print(pyautogui.locateOnScreen("py_auto_pics/arrow.png", region=(0, 100, 100, 100)))
# send_max_items()



def get_send_info():
    pass