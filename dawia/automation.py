from source.tools import *
from time import sleep

from dawia import state


def total_counter(pda_x, pda_y, pixel_distance, count):

    total_line_pda = 0

    for _ in range(7):
        check_pda = pixel_color(pda_x, pda_y)
        if check_pda == (178, 178, 178) or check_pda ==  (255, 255, 255):
            total_line_pda += 1
            print(total_line_pda)
        pda_x += pixel_distance

    print(f"found {total_line_pda}")
    empty_slots = 7 - total_line_pda
    total_count = count - empty_slots
    return(total_count)

def process():

    entries = state.entries

    orange_x = int(entries["sword_x"].get())
    orange_y = int(entries["sword_y"].get())
    pda_x = int(entries["mobs_x"].get())
    pda_y = int(entries["mobs_y"].get())
    scroll_x = int(entries["scroll_x"].get())
    scroll_y = int(entries["scroll_y"].get())
    pixel_distance = int(entries["pixel_distance"].get())

    mouse_move(scroll_x, scroll_y)
    sleep(0.02)
    left_click()
    count = 1

    while state.running:

        check_scroll = pixel_color(orange_x, orange_y)
        print(f"first check {check_scroll}")

        while check_scroll != (255, 102, 0) and check_scroll != (178, 71, 0):

            if not state.running:
                return

            mouse_scroll()
            count += 1

            sleep(0.2)
            check_scroll = pixel_color(orange_x, orange_y)

        print(f"last check, no more lines {check_scroll}")

        count = (count + 1) * 7
        print(f"count is: {count}")
        total_count = total_counter(pda_x, pda_y, pixel_distance, count)

        state.running = False
        state.app.after(0, lambda: state.status_label.configure(text=f"Finished\nnumber of pda is: {total_count}"))
        break
