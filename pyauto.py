import pyautogui
import time
import random
pyautogui.hotkey('ctrl','n')
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('F5')
time.sleep(1)
pyautogui.press('Enter')
time.sleep(1)
pyautogui.typewrite(str(random.randint(1,100000000)))
time.sleep(1)
pyautogui.press('Enter')
time.sleep(1)




