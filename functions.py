import ctypes
import pyautogui

# monitor hd
# move right: x=1355 y=360
# move up:    x=897  y=38
# move left:  x=492  y=360
# move down:  x=910  y=641


def move(direction):
    pixels = {"left": (200, 538), "right": (1634, 530), "up": (980, 29), "down": (908, 910)}
    pyautogui.click(pixels[direction])


def translate(i):
    number = ""
    for letter in str(i):
        if letter in ["1", "2", "3", "4", "5", "6", "7"]:
            number = letter
    return number


def get_system_resolution():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
    return screensize
