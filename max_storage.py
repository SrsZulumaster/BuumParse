import time
import pyautogui as pag
import pytesseract
from abc import ABC, abstractmethod
from get_cell import get_cell_number, get_cell_string, get_shot_string

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\szimmerman\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


class ISendMaxItems(ABC):
    @abstractmethod
    def open_article(self):
        pass

    @abstractmethod
    def send_max_items(self):
        pass

    @abstractmethod
    def get_send_info(self, size):
        pass

    @abstractmethod
    def open_max_items(self):
        pass

    @abstractmethod
    def get_window_region(self, size):
        pass


class SendMaxItems(ISendMaxItems, ABC):
    def __init__(self):
        self.Ylemiste = {}
        self.Rocca = {}
        self.Tartu = {}
        self.Jarve = {}
        self.Parnu = {}
        self.Johvi = {}
        self.Kaubamajakas = {}
        self.send_to_stores = []
        self.list_of_items_to_send = []
        self.send_max_items()

    def open_article(self):
        pag.keyDown("ctrlleft")
        pag.press("r")
        pag.keyUp("ctrlleft")

    def open_max_items(self):
        pag.click("py_auto_pics/ladu.png")
        time.sleep(0.5)
        pag.click("py_auto_pics/ladu.png")
        time.sleep(4)
        pag.click("py_auto_pics/Kogus_laos.png")
        time.sleep(0.5)
        pag.click("py_auto_pics/max_kogus.png")
        pag.click("py_auto_pics/OK_sign.png")
        time.sleep(20)

    # this would sort all the items into dictionaries for each store
    # key = EAN and value = how many items need to be sent
    def send_max_items(self):
        """ Ladu-Ladu-kogus laos- <> -ok"""

        i = 0  # for testing
        self.open_max_items()
        # while pag.locateOnScreen("py_auto_pics/final_line.png") is None:
        while i < 10:  # for testing
            i += 1  # for testing
            line = pag.locateOnScreen("py_auto_pics/arrow.png")
            column = pag.locateOnScreen("py_auto_pics/suurus.png")
            size = pag.screenshot(region=(column[0], line[1], column[2], line[3]))
            EAN_cell = pag.locateOnScreen("py_auto_pics/ribakood.png")
            EAN = get_cell_number(row=line, column=EAN_cell)
            self.open_article()
            time.sleep(2)
            send_info = [self.get_send_info(size), EAN]
            # values returned are what I expect but format might have to change
            self.list_of_items_to_send.append(send_info)
            time.sleep(0.5)
        print(self.list_of_items_to_send)

    def get_window_region(self, size):
        pag.click("py_auto_pics/lao_info.png")
        pag.locateOnScreen(size)
        top_corner = pag.locateOnScreen("py_auto_pics/artikkel-muutmine.png")
        bottom_corner = pag.locateOnScreen("py_auto_pics/katkesta.png")
        left_top_coord = [top_corner[0], top_corner[1]]
        width = bottom_corner[0] - top_corner[0]
        height = bottom_corner[1] - top_corner[1]
        return left_top_coord[0], left_top_coord[1], width, height

    # This would find all the stores that a certain item can be sent to
    # by checking how many items are in each store and how many is allowed
    def get_send_info(self, size):
        size_value = get_shot_string(size)
        time.sleep(1)
        region = (self.get_window_region(size))
        size_column = pag.locateOnScreen("py_auto_pics/suurus.png")
        line = pag.locateOnScreen("py_auto_pics/arrow.png", region=region)
        pag.click(line)
        # This loop checks each row and determines if the item needs to be sent anywhere
        while pag.locateOnScreen("py_auto_pics/grillsalong.png") is None:
            line = pag.locateOnScreen("py_auto_pics/arrow.png", region=region)
            art_size = pag.screenshot(region=(size_column[0] + 2, line[1] + 2, size_column[2], line[3]))
            art_size_value = get_shot_string(art_size)
            # This checks if the Size is correct, if it is then proceeds to check if there is a reason to send the item
            if art_size_value == size_value:
                available_storage = pag.locateOnScreen("py_auto_pics/kogus.png")
                maximum_allowed = pag.locateOnScreen("py_auto_pics/maksimumkogus.png")
                available_num = get_cell_number(available_storage, line)
                max_allowed_num = get_cell_number(maximum_allowed, line)
                # Because some cells can be empty if the max allowed amount hasn't been set
                # or the store has never had this item in store
                # This checks if anything is empty and if there is room to send it
                if available_num is not None and max_allowed_num is not None and max_allowed_num - available_num != 0:
                    check_store = pag.locateOnScreen("py_auto_pics/artikli_ladu.png")
                    send_amount = max_allowed_num - available_num
                    to_store = get_cell_string(check_store, line)
                    return_info = [to_store, size_value, send_amount]
                    self.send_to_stores.append(return_info)
                    pag.press('down')

                else:
                    pag.press('down')
            else:
                pag.press('down')
        return self.send_to_stores


send_max = SendMaxItems
send_max()
