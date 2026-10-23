from dawia import state
from dawia.config import FIELDS


def validate():

    values = {key: state.entries[key].get().strip() for key, _ in FIELDS}

    for key, label in FIELDS:
        if not values[key]:
            return f"Please enter {label}"

    for key, _ in FIELDS:
        if not values[key].isdigit():
            return f"{key} must be a number"

    if state.stop_key is None:
        return "Please choose a stop key"
