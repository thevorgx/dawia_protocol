from source.tools import *
from time import sleep

from dawia import state


def process():

    entries = state.entries

    x1 = int(float(entries["pda_x1"].get()))
    y1 = int(float(entries["pda_y1"].get()))
    x2 = int(float(entries["pda_x2"].get()))
    y2 = int(float(entries["pda_y2"].get()))
    wait_min = float(entries["pda_wait1"].get())
    wait_max = float(entries["pda_wait2"].get())

    click_number = 0

    while state.running:

        x = randint(x2, x1)  # x1 is the greater one
        y = randint(y2, y1)  # y1 is the greater one

        mouse_move(x, y)
        sleep(0.02)
        left_click()

        click_number += 1
        wait = uniform(wait_min, wait_max)
        print(f"click {click_number}: ({x}, {y}) | wait {wait:.3f}s")

        sleep(wait)

