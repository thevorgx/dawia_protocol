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
