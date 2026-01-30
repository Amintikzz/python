import requests
import base64

API_KEY = ""
url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={API_KEY}"

data = {
    "input": {"text": "Сәлеметсіз бе, достар! Бұл қазақша сөйлеу сынағы."},
    "voice": {"languageCode": "kk-KZ", "ssmlGender": "FEMALE"},
    "audioConfig": {"audioEncoding": "MP3"}
}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    audio_content = base64.b64decode(result["audioContent"])

    with open("output.mp3", "wb") as out:
        out.write(audio_content)

    print("Файл сохранен: output.mp3")
else:
    print("Ошибка:", response.text)

