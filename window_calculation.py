import pyautogui

line = pyautogui.locateOnScreen("py_auto_pics/arrow.png")
print(line)
column = pyautogui.locateOnScreen("py_auto_pics/suurus.png")
size = pyautogui.screenshot(region=(column[0], line[1], column[2], line[3]))
pyautogui.click("py_auto_pics/lao_info.png")
pyautogui.locateOnScreen(size)
top_corner = pyautogui.locateOnScreen("py_auto_pics/artikkel-muutmine.png")
bottom_corner = pyautogui.locateOnScreen("py_auto_pics/katkesta.png")
print(top_corner)
print(bottom_corner)
left_top_coord = [top_corner[0], top_corner[1]]
right_bottom_coord = [bottom_corner[0], bottom_corner[1]]
print(left_top_coord)
print(right_bottom_coord)
width = bottom_corner[0] - top_corner[0]
height = bottom_corner[1] - top_corner[1]
region = (left_top_coord[0], left_top_coord[1], width, height)

new_arrow = pyautogui.locateOnScreen("py_auto_pics/arrow.png", region= region)
pyautogui.click(new_arrow)
print(new_arrow)

