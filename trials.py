import pyautogui as pag
'''
I use this file to find solutions i can use in the main project and to test them out

Note: Pyautogui.locateOnScreen returns an Object
      pyautogui.click can click on Objects

'''


line = pag.locateOnScreen("py_auto_pics/arrow.png")
print(line)
column = pag.locateOnScreen("py_auto_pics/suurus.png")
size = pag.screenshot(region=(column[0], line[1], column[2], line[3]))
pag.click("py_auto_pics/lao_info.png")
pag.locateOnScreen(size)
top_corner = pag.locateOnScreen("py_auto_pics/artikkel-muutmine.png")
bottom_corner = pag.locateOnScreen("py_auto_pics/katkesta.png")
print(top_corner)
print(bottom_corner)
left_top_coord = [top_corner[0], top_corner[1]]
right_bottom_coord = [bottom_corner[0], bottom_corner[1]]
print(left_top_coord)
print(right_bottom_coord)
width = bottom_corner[0] - top_corner[0]
height = bottom_corner[1] - top_corner[1]
region = (left_top_coord[0], left_top_coord[1], width, height)

new_arrow = pag.locateOnScreen("py_auto_pics/arrow.png", region= region)
pag.click(new_arrow)
print(new_arrow)

