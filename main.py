import json
import subprocess
import shlex
from datetime import datetime
import os
import pyttsx3
from vosk import Model, KaldiRecognizer
import pyaudio
from colorama import init, Fore, Style

#my own moduel
from greet import greet
import shortcuts




init(autoreset=True)

# ================== TTS FUNCTION ==================
def speak(text):
    print(Fore.WHITE + f"Assistant says: {text}")  # Color for assistant output
    cmd = f'python "D:\\dev_v3\\tts.py" "{text}"'
    subprocess.Popen(shlex.split(cmd))


# ================== VOSK SPEECH RECOGNITION SETUP ==================
model_path = r"D:\dev_v3\vosk-model-small-en-us-0.15"  #change this path to the model you prefer I am using local vosk model
model = Model(model_path)
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=8000)
stream.start_stream()

def takeCommand():
    print(Fore.WHITE + "Listening...")  # Color for listening status
    while True:
        data = stream.read(4000, exception_on_overflow=False)

        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            command_text = result.get("text", "").strip()
            if command_text:
                print(Fore.GREEN + f"\nYou said:  {command_text}")  # Color for recognized user speech
                return command_text.lower()

        else:
            partial = json.loads(rec.PartialResult())
            if partial.get("partial"):
                print(Fore.BLUE + "\rListening: " + partial["partial"], end="")

apps = {
    "brave" : r"C:\Users\Unamused\Desktop\main._..lnk",
    "clock" : r"C:\Users\Unamused\Desktop\Clock.lnk",
    "whatsapp" : r"C:\Users\Unamused\Desktop\Whatsapp.lnk",
    "calculator" : r"C:\Users\Unamused\Desktop\Calculator.lnk",
    "music" : r"C:\Users\Unamused\Desktop\Media Player.lnk",
    "pass" : r"C:\Users\Unamused\Desktop\Proton Pass.lnk",
    "notepad" : "notepad.exe",   
}

# ================== MAIN ASSISTANT LOOP ==================
if __name__ == "__main__":
    speak(greet())

    sleeping = False

    while True:
        if not sleeping:
            print(Fore.YELLOW + "Say 'friday' to wake me up...")
        else:
            print(Fore.YELLOW + "Sleeping... Say 'friday' to wake me up.")

        query = takeCommand()


        if "friday" in query:
            sleeping = False
            speak(f"Yes sir")

            while True:
                command = takeCommand()


                if "go to sleep" in command:
                    sleeping = True
                    speak("ok sir call me anytime")
                    print(Fore.MAGENTA + "Assistant is going to sleep. Say 'friday' to wake me up.")
                    break

                elif "hello" in command:
                    speak("Hello sir, what can I do for you?")

                elif "how are you" in command:
                    speak("I am doing great, thank you!")

                elif "your name" in command:
                    speak("I am your friend sir, I am dev")

                elif "time" in command:
                    now = datetime.now().strftime("%I:%M %p")
                    speak(f"The time is {now}")

                elif "exit yourself" in command or "close yourself" in command or "bye friday" in command:
                    speak("Ok sir call me anytime")
                    exit()

                elif "day" in command:
                    today = datetime.now().strftime("%A, %d %B")
                    speak(f"Today is {today}")

                elif "okay" in command:
                    speak("hmmmm")

                elif "open" in command and "brave" in command:
                    os.startfile(apps["brave"])
                elif "open" in command and  "calculator" in command:
                    os.startfile(apps["calculator"])
                elif  "open"in command and "alarm" in command:
                    os.startfile(apps["clock"])
                elif "open" in command and  "messages" in command:
                    os.startfile(apps["whatsapp"])
                elif  "open" in command and "notes" in command:
                    os.startfile(apps["notepad"])
                elif  "open"in command and "music" in command:
                    os.startfile(apps["music"])
                elif "open" in command and "password manager" in command:
                    os.startfile(apps["pass"])
                elif "open" in command and "screenshot" in command:
                    shortcuts.ssfolder()

                elif "pause" in command or "stop" in command or "play" in command:
                    shortcuts.playpause()
                elif "next song" in command:
                    shortcuts.next()
                elif "previous song" in command:
                    shortcuts.prev()
                elif "screenshot" in command:
                    shortcuts.ss()

                elif "increase the volume" in command or "higher the volume" in command:
                    shortcuts.incvol()
                elif "decrease the volume" in command or "lower the volume" in command:
                    shortcuts.decvol()
                elif "minimize it" in command:
                    shortcuts.minimize()
                elif "maximize it" in command:
                    shortcuts.maximize()

                else:
                    print(Fore.RED + "Sorry, don't know what it means.")

        else:
            if not sleeping:
                print(Fore.BLUE + "Wake word not detected. Listening...")


