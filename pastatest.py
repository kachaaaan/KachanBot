import pyautogui
import time
from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import imagesearch_from_folder
from pathlib import Path
datafolder = "trigos/"

results = str(imagesearch_from_folder(datafolder, 0.9))
print(results)
