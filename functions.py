import pyautogui


# move right: x=1355 y=360
# move up:  x=897 y=38
# move left: x=492 y=360
# move down: x=910 y=641

def moveup():
    pyautogui.click(980, 29)


def movedown():
    pyautogui.click(908, 910)


def moveright():
    pyautogui.click(1634, 530)


def moveleft():
    pyautogui.click(200, 538)


def translate(i):
    number = ""
    for letter in str(i):
        if letter in ["1", "2", "3", "4", "5", "6", "7"]:
            number = letter
    return number
