from pynput.keyboard import Key, Listener
from pynput.mouse import Controller

from dawia import state

mouse = Controller()


def pick_coords(x_entry, y_entry, name):

    if state.picking:
        return

    state.picking = True
    state.status_label.configure(text=f"{name}: hover the target and press SPACE (Esc to cancel)")

    def fill(x, y):

        x_entry.delete(0, "end")
        x_entry.insert(0, str(int(x)))
        y_entry.delete(0, "end")
        y_entry.insert(0, str(int(y)))

        state.status_label.configure(text=f"{name} set: {int(x)}, {int(y)}")
        state.picking = False

    def cancel():
        state.status_label.configure(text="Pick cancelled")
        state.picking = False

    def on_press(key):
        if key == Key.space:
            x, y = mouse.position
            state.app.after(0, lambda: fill(x, y))
            return False  # stop this listener

        if key == Key.esc:
            state.app.after(0, cancel)
            return False

    Listener(on_press=on_press).start()




def pick_region(x1_entry, y1_entry, x2_entry, y2_entry, name):

    if state.picking:
        return

    state.picking = True
    state.status_label.configure(text=f"{name}: hover point 1 and press SPACE (Esc to cancel)")

    presses = []

    def fill(x_entry, y_entry, x, y):

        x_entry.delete(0, "end")
        x_entry.insert(0, str(int(x)))
        y_entry.delete(0, "end")
        y_entry.insert(0, str(int(y)))

    def first_point(x, y):
        fill(x1_entry, y1_entry, x, y)
        state.status_label.configure(text=f"Point 1 set: {int(x)}, {int(y)}\nnow hover point 2 and press SPACE")

    def second_point(x, y):
        fill(x2_entry, y2_entry, x, y)
        state.status_label.configure(text=f"{name} set")
        state.picking = False

    def cancel():
        state.status_label.configure(text="Pick cancelled")
        state.picking = False

    def on_press(key):
        if key == Key.space:
            x, y = mouse.position
            presses.append(1)

            if len(presses) == 1:
                state.app.after(0, lambda: first_point(x, y))
                return  # keep listening for the second press

            state.app.after(0, lambda: second_point(x, y))
            return False  # stop this listener

        if key == Key.esc:
            state.app.after(0, cancel)
            return False

    Listener(on_press=on_press).start()