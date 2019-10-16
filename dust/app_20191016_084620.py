from ahk import AHK, Hotkey

# from lk_utils.time_utils import generate_timestamp
# from lk_utils.toolbox import *

ahk = AHK(executable_path=r'D:\likianta\programs\auto_hotkey\AutoHotkey.exe')


def main():
    """
    flow: scrolllock -> f2 - type uid (aka timestamp (ymd hns)) - enter -> over
    """
    # listening to `scrolllock`
    key_evt = 'scrolllock'
    handle = Hotkey(ahk, key_evt, 'actions')
    handle.start()


def actions():
    # execute actions
    # ahk.key_press('f2')
    # ahk.type(generate_timestamp('ymd hns'))
    # ahk.key_press('enter')
    
    # TEST
    ahk.type('hello world')


if __name__ == "__main__":
    main()
