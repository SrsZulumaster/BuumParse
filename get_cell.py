import pyautogui
import pytesseract

# ÜlemistRocaJärv*õhPnuTKbjkNBIELP
# this clicks on the cell where the column and row intersect and returns the value
def get_cell_number(column, row):
    custom_config = r'--psm 6  -c tessedit_char_whitelist=0123456789,.'
    screen_shot = pyautogui.screenshot(region=(column[0],row[1],column[2],row[3]))
    screen_value = pytesseract.image_to_string(screen_shot, config=custom_config)
    screen_value = screen_value.strip()
    if screen_value == '':
        return None
    else:
        screen_value = float(screen_value.replace(',', '.'))
        print(screen_value)
        return int(screen_value)


def get_cell_string(column, row):
    custom_config = r'--psm 6'
    screen_shot = pyautogui.screenshot(region=(column[0],row[1],column[2],row[3]))
    screen_value = pytesseract.image_to_string(screen_shot, config=custom_config)
    screen_value = screen_value.strip()
    print(screen_value)
    return screen_value
