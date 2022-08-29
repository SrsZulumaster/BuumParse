import pyautogui as pag
'''
I use this file to find solutions i can use in the main project and to test them out

Note: Pyautogui.locateOnScreen returns an Object
      pyautogui.click can click on Objects

'''

# this is what gets returned from max storage
stuffs =[[[], 8002620020408], [[['* Jarve kauplus', 'S46M', 1], ['* Kaubamajakas', 'S46M', 1], ['* Rocca kauplus', 'S46M', -1], ['* Tartu kauplus', 'S46M', 1], ['* Ulemiste kauplus', 'S46M', 1]], 7392158846696], [[], 7392158846771], [[], 7392158846818], [[], 7611160100207], [[], 835028001773], [[], 7331423011476], [[['* Rocca kauplus', '152', -1], ['* Ulemiste kauplus', '152', 1]], 4260641520411], [[['* Johvi kauplus', 'M', 1], ['', 'M', 1], ['* Rocca kauplus', 'M', -1], ['* Tartu kauplus', 'M', 1]], 8014044949913], [[], 40818114162]]

# this is how it gets unpacked into usable data
for i in stuffs:
    if i[0] != []:
        dicti = {i[1]:i[0]}
        print(dicti)
    else:
        continue
