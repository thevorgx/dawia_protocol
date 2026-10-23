import json
import os

from dawia import state
from dawia.config import FIELDS, SETTINGS_FILE


def save_settings():

    settings = {key: state.entries[key].get() for key, _ in FIELDS}
    settings["stop_key"] = state.stop_key

    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)


def load_settings():

    if not os.path.exists(SETTINGS_FILE):
        return

    with open(SETTINGS_FILE, "r") as file:
        settings = json.load(file)

    for key, _ in FIELDS:
        state.entries[key].insert(0, settings.get(key, ""))

    state.stop_key = settings.get("stop_key")
    if state.stop_key:
        state.status_label.configure(
            text=f"Stop key: {state.stop_key}"
        )
