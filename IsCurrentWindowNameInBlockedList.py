from win32gui import GetWindowText, GetForegroundWindow
import globalVariables

# not used currently, don't delete


def IsCurrentWindowNameInBlockedList():
    for window in globalVariables.unwantedWindowTitles:
        if window in GetWindowText(GetForegroundWindow()):
            return True
    return False
