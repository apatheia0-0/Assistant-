# tts_process.py
import pyttsx3
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("rate", 177)
engine.setProperty('voice', voices[0].id)

text = " ".join(sys.argv[1:])  # get text from command line arguments, just making these 11 lines took 5 hours for me work
engine.say(text)               # cause it was not woking in a single file with main.py and its a bug but after it worked
engine.runAndWait()
