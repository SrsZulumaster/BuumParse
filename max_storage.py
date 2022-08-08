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
    Ylemiste = {}
    Rocca = {}
    Tartu = {}
    Jarve = {}
    Parnu = {}
    Johvi = {}
    Kaubamajakas = {}
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
    send_info = get_send_info(size, EAN)
    if send_info is not None:
        print(send_info)
        if send_info[2] == "Ülemiste kauplus":
            Ylemiste[send_info[0]] = send_info[1]
        elif send_info[2] == "Rocca kauplus":
            Rocca[send_info[0]] = send_info[1]
        elif send_info[2] == "Tartu kauplus":
            Tartu[send_info[0]] = send_info[1]
        elif send_info[2] == "Järve kauplus":
            Jarve[send_info[0]] = send_info[1]
        elif send_info[2] == "Jõvhi kauplus":
            Parnu[send_info[0]] = send_info[1]
        elif send_info[2] == "Pärnu Keskus":
            Johvi[send_info[0]] = send_info[1]
        elif send_info[2] == "Kaubamajaks":
            Kaubamajakas[send_info[0]] = send_info[1]
        else:
            return ValueError
    else:
        pyautogui.click("py_auto_pics/katkesta.png")
        pyautogui.press('down')



def get_send_info(size, EAN):
    pyautogui.click("py_auto_pics/lao_info.png")
    pyautogui.locateOnScreen(size)
    print(pyautogui.locateOnScreen("py_auto_pics/artikkel-muutmine.png"))
    top_corner = pyautogui.locateOnScreen("py_auto_pics/artikkel-muutmine.png")
    bottom_corner = pyautogui.locateOnScreen("py_auto_pics/katkesta.png")
    left_top_coord = [top_corner[0], top_corner[1]]
    right_bottom_coord = [top_corner[0], bottom_corner[1]]
    region = (left_top_coord[0], left_top_coord[1], right_bottom_coord[0], right_bottom_coord[1])
    while True:
        line = pyautogui.locateOnScreen("py_auto_pics/arrow.png", region=region)
        available_storage = pyautogui.locateOnScreen("py_auto_pics/kogus.png")
        maximum_allowed = pyautogui.locateOnScreen("py_auto_pics/maksimumkogus.png")
        available_num = get_cell_number(available_storage, line)
        max_allowed_num = get_cell_number(maximum_allowed, line)
        if available_num != '' or max_allowed_num != '':
            available_num = float(available_num.replace(',','.'))
            max_allowed_num = float(max_allowed_num.replace(',', '.'))
            if available_num > max_allowed_num:
                check_store = pyautogui.locateOnScreen("py_auto_pics/artikli_ladu.png")
                send_amount = available_num - max_allowed_num
                to_store = get_cell_string(check_store, line)
                return_info = [EAN, send_amount, to_store]
                return return_info
        else:
            pyautogui.press('down')
            continue


send_max_items()
