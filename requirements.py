import json
import subprocess
import shlex
from datetime import datetime
import os
import pyttsx3
from vosk import Model, KaldiRecognizer
import pyaudio
from colorama import init, Fore, Style