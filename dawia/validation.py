from dawia import state
from dawia.config import FIELDS


from dawia import state
from dawia.config import FIELDS


def is_decimal_field(key):
    return key.endswith("_min") or key.endswith("_max")


def is_number(value, decimal):
    if decimal:
        return value.replace(".", "", 1).isdigit()  # allows 0.02
    return value.isdigit()


def validate():

    values = {key: state.entries[key].get().strip() for key, _ in FIELDS}

    for key, label in FIELDS:
        if not values[key]:
            return f"Please enter {label}"

    for key, _ in FIELDS:
        decimal = is_decimal_field(key)

        if not is_number(values[key], decimal):
            return f"{key} must be {'a number' if decimal else 'a whole number'}"

    # every X_min must not be greater than its X_max
    for key in values:
        if key.endswith("_min"):
            max_key = key[:-4] + "_max"

            if max_key in values and float(values[key]) > float(values[max_key]):
                return f"{key} must not be greater than {max_key}"

    if state.stop_key is None:
        return "Please choose a stop key"
