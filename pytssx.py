import pyttsx3
import pythoncom

engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
