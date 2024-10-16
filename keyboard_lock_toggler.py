import ctypes

""" 
Checks if button_lock is activated
"""


def is_lock_active(button_lock) -> bool:
    # caps lock 0x14
    if button_lock == "caps":
        return ctypes.windll.user32.GetKeyState(0x14) & 0x0001 != 0 and print('caps on')

    # num lock 0x90
    if button_lock == "num":
        return ctypes.windll.user32.GetKeyState(0x90) & 0x0001 != 0 and print('num on')

    # scroll lock 0x91
    if button_lock == "scroll":
        return ctypes.windll.user32.GetKeyState(0x91) & 0x0001 != 0 and print('scroll on')
