from math import isfinite

from dawia import state
from dawia.config import FIELDS


def is_number(value):
    try:
        return isfinite(float(value))
    except ValueError:
        return False


def validate():

    values = {key: state.entries[key].get().strip() for key, _ in FIELDS}

    for key, label in FIELDS:
        if not values[key]:
            return f"Please enter {label}"

    for key, _ in FIELDS:
        if not is_number(values[key]):
            return f"{key} must be a number"

    if state.stop_key is None:
        return "Please choose a stop key"


def fix_order():

    for first, second, first_must_be_greater in state.pairs:
        a = first.get().strip()
        b = second.get().strip()

        if first_must_be_greater:
            out_of_order = float(a) < float(b)
        else:
            out_of_order = float(a) > float(b)

        if out_of_order:
            first.delete(0, "end")
            first.insert(0, b)
            second.delete(0, "end")
            second.insert(0, a)