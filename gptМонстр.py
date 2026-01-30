from openai import OpenAI
from gtts import gTTS
import pyglet
import time
import os
import speech_recognition as sr
while True:
    input()

    client = OpenAI(api_key="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")  # вставь свой ключ сюда
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

        try:
            text=recognizer.recognize_google(audio,language="ru-RU")
            print("Ты сказал:", text)
            response = client.chat.completions.create(
            model="gpt-4o-mini",  # можешь заменить на gpt-4o, если используешь другой
            messages=[
                {"role": "system", "content": "Ты — умный ассистент, отвечай понятно и коротко."},
                {"role": "user", "content": text}
            ]
        )
            
                    
        except sr.UnknownValueError:
            print("не удалось разрознать речь")
        except sr.RequestError:
            print("ошибка подключения к Google")

            

        answer = response.choices[0].message.content
        print("ChatGPT:", answer)
        tts=gTTS(answer ,lang='ru')
        tts.save("звук.mp3")
        music=pyglet.resource.media("звук.mp3")
        music.play()
