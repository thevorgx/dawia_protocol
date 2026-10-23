from win32api import SetCursorPos, mouse_event
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP, MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP, MOUSEEVENTF_WHEEL
from pyautogui import pixel, keyDown, keyUp
from random import randint, uniform
from time import sleep


def left_click():
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    sleep(0.02)
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def righ_click():
    mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    sleep(0.02)
    mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

def rand_left_click(x1, y1, x2, y2):
    x = randint(x1, x2)
    y = randint(y1, y2)
    SetCursorPos((x, y))
    sleep(0.08)
    mouse_event(MOUSEEVENTF_LEFTDOWN, x, y)
    sleep(0.02)
    mouse_event(MOUSEEVENTF_LEFTUP, x, y)

def mouse_move(x, y):
    SetCursorPos((x, y))

def mouse_scroll():
    mouse_event(MOUSEEVENTF_WHEEL,0,0,-40,0)

def pixel_color(x, y):
    color = pixel(x, y)
    return(color)

def rand_wait(min, max):
    time = uniform(min, max)
    sleep(time)

def akey_press(key):
    keyDown(key)
    sleep(0.02)
    keyUp(key)