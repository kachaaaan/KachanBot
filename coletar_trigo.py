import pyautogui
import time
from python_imagesearch.imagesearch import imagesearch, imagesearch_from_folder
import movements

cursorposition = pyautogui.position()
time.sleep(2)
confidence = 0.9
datafolder = "trigos/"

for x in range(0, 50):
    found_flag = False
    results = (imagesearch_from_folder(datafolder, 0.9))
    for i in results:
        if results[i] != [-1, -1]:
            found_flag = True
            break
    if found_flag:
        for i in results:
            if results[i] != [-1, -1]:
                print("trigo em", results[i])
                pos = results[i]
                pyautogui.click(x=pos[0], y=pos[1], clicks=1, button='left')
                pyautogui.moveTo(cursorposition)
                time.sleep(4)
                break
    else:
        movements.moveright()
        time.sleep(7)
print("image not found")
