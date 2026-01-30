import random
from gtts import gTTS
import time
import pyglet
import speech_recognition as sr
while True:
    a = random.randint(1,10)
    b = random.randint(1,10)
    tts = gTTS('Сколько будет ' + str(a)+ ' умножить на  ' +str(b), lang = 'ru')

    tts.save('GTtext.mp3')
    music = pyglet.resource.media('GTtext.mp3')
    music.play()
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        time.sleep(2) 
        print('Сколько будет ' + str(a)+ ' умножить на ' +str(b))
        
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language='ru-RU')
            print('Ты сказал:', text)

            if a*b == int(text):
                tts = gTTS('Молодец', lang = 'ru')
                tts.save('GTtext.mp3')
                music = pyglet.resource.media('GTtext.mp3')
                music.play()
            else:
                tts = gTTS('Ляя какой тупой', lang = 'ru')
                tts.save('GTtext.mp3')
                music = pyglet.resource.media('GTtext.mp3')
                music.play()
        except sr.UnknownValueError:
            tts = gTTS('Скажи заново', lang = 'ru')
            tts.save('GTtext.mp3')
            music = pyglet.resource.media('GTtext.mp3')
            music.play()
        except sr.RequestError:
            print('Правильно')
         
