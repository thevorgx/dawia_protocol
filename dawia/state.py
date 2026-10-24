# Shared state. Always use it as `from dawia import state` and then `state.running`,
# never `from dawia.state import running` (that would copy the value).

running = False
stop_key = None
picking = False

app = None            # the main CTk window
status_label = None   # the label at the bottom of the window

entries = {}          # "sword_x" -> CTkEntry, ...
pages = {}            # "controls" / "settings" -> frame
nav_buttons = {}      # "controls" / "settings" -> button
pairs = []   # (first_entry, second_entry, first khass ykon greater than second)
