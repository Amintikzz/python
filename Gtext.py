from gtts import gTTS
import pyglet
f = open('gtext.txt', 'r')
t = f.read()
print(t)
f.close()
tts = gTTS(t, lang = 'ru')
tts.save('Gtext.mp3')
music = pyglet.resource.media('Gtext.mp3')
music.play()

