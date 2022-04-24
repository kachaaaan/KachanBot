import pyautogui
import time
from python_imagesearch.imagesearch import imagesearch, imagesearch_from_folder
from functions import translate, move


time.sleep(2)
confidence = 0.9
datafolder = "trigos/"

for x in range(0, 50):
    found_flag = False
    results = (imagesearch_from_folder(datafolder, 0.9))
    for i in results:
        if results[i] != [-1, -1] and 1566 > (results[i][0] - 1920) > 353:
            found_flag = True
            break
    if found_flag:
        for i in results:
            if results[i] != [-1, -1]:
                print(f"trigo {translate(i)} em {results[i]}")
                pos = results[i]
                if 1566 > (pos[0] - 1920) > 353:
                    cursor_position = pyautogui.position()
                    pyautogui.click(x=(pos[0] - 1920), y=pos[1], clicks=1, button='left')
                    pyautogui.moveTo(cursor_position)
                    time.sleep(3)
                    break
    else:
        cursor_position = pyautogui.position()
        move("right")
        pyautogui.moveTo(cursor_position)
        time.sleep(7)
