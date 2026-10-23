from threading import Thread

from dawia import state
from dawia.automation import process
from dawia.navigation import show_page
from dawia.settings import save_settings
from dawia.validation import validate


def start():

    error = validate()

    if error:
        state.status_label.configure(text=error)
        # most errors are about the fields, so jump to the settings page
        if state.stop_key is not None:
            show_page("settings")
        return

    save_settings()

    if not state.running:
        state.running = True
        state.status_label.configure(text="Running...")
        Thread(target=process, daemon=True).start()


def stop():

    state.running = False
    state.status_label.configure(text="Stopped")


def choose_stop_key():

    state.status_label.configure(text="Press the key you want to use...")
    state.app.bind("<KeyPress>", set_stop_key)


def set_stop_key(event):

    state.stop_key = event.keysym.lower()

    state.status_label.configure(
        text=f"Stop key: {event.keysym}"
    )

    state.app.unbind("<KeyPress>")


def on_key_press(key):

    if state.stop_key is None:
        return

    if hasattr(key, "name"):
        pressed_key = key.name.lower()

    elif hasattr(key, "char") and key.char:
        pressed_key = key.char.lower()

    else:
        return

    if pressed_key == state.stop_key:
        state.running = False
        state.app.after(0, stop)
