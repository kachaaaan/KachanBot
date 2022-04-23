import pyautogui
import time
from python_imagesearch.imagesearch import imagesearch
import movements

cursorposition = pyautogui.position()
time.sleep(2)
confidence = 0.9

for x in range(0, 10):
    pos = imagesearch("./trigos/trigo1.png", confidence)
    while pos[0] != -1:
        print("trigo 1 in position : ", pos)
        pyautogui.click(x=pos[0], y=pos[1], clicks=1, button='left')
        pyautogui.moveTo(cursorposition)
        time.sleep(6)
        if imagesearch("./trigos/trigo1.png", confidence) != pos:
            pos = imagesearch("./trigos/trigo1.png", confidence)
        else:
            break

    pos = imagesearch("./trigos/trigo2.png", confidence)
    while pos[0] != -1:
        print("trigo 2 in position : ", pos[0], pos[1])
        pyautogui.click(x=pos[0], y=pos[1], clicks=1, button='left')
        pyautogui.moveTo(cursorposition)
        time.sleep(6)
        if imagesearch("./trigos/trigo2.png", confidence) != pos:
            pos = imagesearch("./trigos/trigo2.png", confidence)
        else:
            break

    pos = imagesearch("./trigos/trigo3.png", confidence)
    while pos[0] != -1:
        print("trigo 3 in position : ", pos[0], pos[1])
        pyautogui.click(x=pos[0], y=pos[1], clicks=1, button='left')
        pyautogui.moveTo(cursorposition)
        time.sleep(6)
        if imagesearch("./trigos/trigo3.png", confidence) != pos:
            pos = imagesearch("./trigos/trigo3.png", confidence)
        else:
            break

    pos = imagesearch("./trigos/trigo4.png", confidence)
    while pos[0] != -1:
        print("trigo 4 in position : ", pos)
        pyautogui.click(x=pos[0], y=pos[1], clicks=1, button='left')
        pyautogui.moveTo(cursorposition)
        time.sleep(6)
        if imagesearch("./trigos/trigo4.png", confidence) != pos:
            pos = imagesearch("./trigos/trigo4.png", confidence)
        else:
            break

    movements.moveright()
    time.sleep(7)
print("image not found")
