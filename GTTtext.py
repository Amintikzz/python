from gtts import gTTS
import time
import pyglet
import speech_recognition as sr
while True:
    time.sleep(2)
    print('Скажи чё нибудь')
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        
        
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language='ru-RU')
            print('Ты сказал:', text)
            tts = gTTS(text, lang = 'ru')
            tts.save('GTTtext.mp3')
            music = pyglet.resource.media('GTTtext.mp3')
            music.play()
        except sr.UnknownValueError:
            tts = gTTS('Моя твоя не понимать', lang = 'ru')
            tts.save('GTTtext.mp3')
            music = pyglet.resource.media('GTTtext.mp3')
            music.play()
        except sr.RequestError:
            print('Правильно')
         


