from win32api import SetCursorPos, mouse_event
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP, MOUSEEVENTF_WHEEL
from time import sleep
from pyautogui import pixel


def left_click():
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    sleep(0.02)
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def mouse_move(x, y):
    SetCursorPos((x, y))

def mouse_scroll():
    mouse_event(MOUSEEVENTF_WHEEL,0,0,-40,0)

def pixel_color(x, y):
    color = pixel(x, y)
    return(color)