from win32gui import GetWindowText, GetForegroundWindow
import globalVariables

#not used currently, don't delete

def IsCurrentWindowNameInBlockedList():
    currentActiveWindowTitle = GetWindowText(GetForegroundWindow())
    for window in globalVariables.unwantedWindowTitles:
        if window in currentActiveWindowTitle:
            return True
    return False
