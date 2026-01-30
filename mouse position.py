import pyautogui
import random
import time

pyautogui.press("win")
pyautogui.typewrite("paint")
pyautogui.press("Enter")
time.sleep(2)
while True:
    x = random.randint(915,1822)
    y = random.randint(97,915)

    pyautogui.dragTo(x,y,1)



