import pytesseract
from yesterday_sales import get_yesterday_sales

'''
Buum- a retail program built on Firebird 3.0 - restricted to only use client side application
Pyautogui is used to interact with Buum
Pytesseract is used to locate the correct line on screen will be used to read the date
'''
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\szimmerman\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


if __name__ == "__main__":
    sales = get_yesterday_sales()
    print(sales)
