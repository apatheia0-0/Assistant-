import pyautogui
from datetime import datetime
import os
import time

def playpause():
    pyautogui.press('playpause')

def next():
    pyautogui.press('nexttrack')

def prev():
    pyautogui.press('prevtrack')

def ss():
    sstime = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    ssfolder = "ss"
    ssname = f"ss_{sstime}.png"
    sspath = os.path.join(ssfolder, ssname)
    screenshot = pyautogui.screenshot()
    screenshot.save(sspath)

def ssfolder():
    ssfolder = r"D:\dev_v3\ss"
    os.startfile(ssfolder)

def decvol():
    pyautogui.press('volumedown')

def incvol():
    pyautogui.press('volumeup')

def minimize():
    pyautogui.hotkey('alt','space')
    time.sleep(0.3)
    pyautogui.press('n')

def maximize():
    pyautogui.hotkey('alt', 'space')
    time.sleep(0.3)
    pyautogui.press('m')


