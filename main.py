import pyautogui
import pytesseract as pt
from PIL import Image

'''
Buum- a retail program built on Firebird 3.0 - restricted to only use client side application
Sensmax- a website that tracks how many visitors visit the store gets count from a sensor in store
Pyautogui is used to interact with Buum
Pytesseract is used to locate the correct line on screen will be used to read the date
Future of the project might include web scraping to get info from Sensmax
'''

# this line is absolutely necessary for Pytesseract to work DO NOT EDIT
pt.pytesseract.tesseract_cmd = r'C:\Users\szimmerman\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# prints out available languages
print(pt.pytesseract.get_languages(config=''))
# reads and prints out words on the pictures. lang='est' necessary to get correct output
print(pt.image_to_string('müük.png', lang='est'))
print(pt.image_to_string('aruanded.png', lang='est')) # aruanded.png cropped to small

# these lines find buttons on the pictures and click them on screen
# pyautogui.click('clickON.png')
# pyautogui.click('müük.png')
# pyautogui.click('aruanded.png')


# these lines will be used to locate the necessary value in the table
# summaKM = pyautogui.locateOnScreen()
# KP = pyautogui.locateOnScreen()
