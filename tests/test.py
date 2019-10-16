from ahk import AHK, Hotkey

ahk = AHK(executable_path=r'D:\likianta\programs\auto_hotkey\AutoHotkey.exe')

key_combo = '#n'  # Define an AutoHotkey key combonation
script = 'Run Notepad'  # Define an ahk script
hotkey = Hotkey(ahk, key_combo, script)  # Create Hotkey
hotkey.start()  # Start listening for hotkey
