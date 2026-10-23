import customtkinter as ctk
from source.tools import *
from threading import Thread
from time import sleep
from pynput.keyboard import Listener, Key
from PIL import Image, ImageTk
import json
import os
from pynput.mouse import Controller
import tkinter as tk


running = False
stop_key = None
SETTINGS_FILE = "settings.json"

ACCENT = "#F0A51E"
ACCENT_HOVER = "#b97b0c"
BG = "#1A1824"


def start():

    global running

    error = validate()

    if error:
        status_label.configure(text=error)
        # most errors are about the fields, so jump to the settings page
        if stop_key is not None:
            show_page("settings")
        return

    save_settings()

    if not running:
        running = True
        status_label.configure(text="Running...")
        Thread(target=process, daemon=True).start()

def validate():

    sword_x = sword_x_entry.get().strip()
    sword_y = sword_y_entry.get().strip()
    mobs_x = mobs_x_entry.get().strip()
    mobs_y = mobs_y_entry.get().strip()
    scroll_x = scroll_x_entry.get().strip()
    scroll_y = scroll_y_entry.get().strip()
    pixel_distance = pixel_distance_entry.get().strip()

    if not sword_x:
        return "Please enter X coordinate for sword"

    if not sword_y:
        return "Please enter Y coordinate for sword"

    if not mobs_x:
        return "Please enter X coordinate for mobs"

    if not mobs_y:
        return "Please enter Y coordinate for mobs"

    if not scroll_x:
        return "Please enter X coordinate for scroll"

    if not scroll_y:
        return "Please enter Y coordinate for scroll"

    if not pixel_distance:
        return "Please enter the pixel distance"


    if not sword_x.isdigit():
        return "sword_x must be a number"

    if not sword_y.isdigit():
        return "sword_y must be a number"

    if not mobs_x.isdigit():
        return "mobs_x must be a number"

    if not mobs_y.isdigit():
        return "mobs_y must be a number"

    if not scroll_x.isdigit():
        return "scroll_x must be a number"

    if not scroll_y.isdigit():
        return "scroll_y must be a number"

    if not pixel_distance.isdigit():
        return "pixel_distance must be a number"

    if stop_key is None:
        return "Please choose a stop key"

def stop():

    global running

    running = False
    status_label.configure(text="Stopped")

def choose_stop_key():

    status_label.configure(text="Press the key you want to use...")
    app.bind("<KeyPress>", set_stop_key)

def set_stop_key(event):

    global stop_key

    stop_key = event.keysym.lower()

    status_label.configure(
        text=f"Stop key: {event.keysym}"
    )

    app.unbind("<KeyPress>")

def on_key_press(key):

    global running

    if stop_key is None:
        return

    if hasattr(key, "name"):
        pressed_key = key.name.lower()

    elif hasattr(key, "char") and key.char:
        pressed_key = key.char.lower()

    else:
        return

    if pressed_key == stop_key:
        running = False
        app.after(0, stop)

def save_settings():

    settings = {
        "sword_x": sword_x_entry.get(),
        "sword_y": sword_y_entry.get(),
        "mobs_x": mobs_x_entry.get(),
        "mobs_y": mobs_y_entry.get(),
        "scroll_x": scroll_x_entry.get(),
        "scroll_y": scroll_y_entry.get(),
        "pixel_distance": pixel_distance_entry.get(),
        "stop_key": stop_key
    }

    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)

def load_settings():

    global stop_key

    if not os.path.exists(SETTINGS_FILE):
        return

    with open(SETTINGS_FILE, "r") as file:
        settings = json.load(file)

    sword_x_entry.insert(0, settings.get("sword_x", ""))
    sword_y_entry.insert(0, settings.get("sword_y", ""))
    mobs_x_entry.insert(0, settings.get("mobs_x", ""))
    mobs_y_entry.insert(0, settings.get("mobs_y", ""))
    scroll_x_entry.insert(0, settings.get("scroll_x", ""))
    scroll_y_entry.insert(0, settings.get("scroll_y", ""))
    pixel_distance_entry.insert(0, settings.get("pixel_distance", ""))

    stop_key = settings.get("stop_key")
    if stop_key:
        status_label.configure(
            text=f"Stop key: {stop_key}"
        )

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

    global running

    orange_x = int(sword_x_entry.get())
    orange_y = int(sword_y_entry.get())
    pda_x = int(mobs_x_entry.get())
    pda_y = int (mobs_y_entry.get())
    scroll_x = int(scroll_x_entry.get())
    scroll_y = int(scroll_y_entry.get())
    pixel_distance = int(pixel_distance_entry.get())

    mouse_move(scroll_x, scroll_y)
    sleep(0.02)
    left_click()
    count = 1

    while running:

        check_scroll = pixel_color(orange_x, orange_y)
        print(f"first check {check_scroll}")

        while check_scroll != (255, 102, 0) and check_scroll != (178, 71, 0):

            if not running:
                return

            mouse_scroll()
            count += 1

            sleep(0.2)
            check_scroll = pixel_color(orange_x, orange_y)

        print(f"last check, no more lines {check_scroll}")

        count = (count + 1) * 7
        print(f"count is: {count}")
        total_count = total_counter(pda_x, pda_y, pixel_distance, count)

        running = False
        app.after(0, lambda: status_label.configure(text=f"Finished\nnumber of pda is: {total_count}"))
        break


# ---------------------------------- page switching ----------------------------------

def show_page(name):

    for page in pages.values():
        page.pack_forget()

    pages[name].pack(fill="both", expand=True)

    for page_name, button in nav_buttons.items():
        if page_name == name:
            button.configure(fg_color=ACCENT, text_color=BG, hover_color=ACCENT_HOVER)
        else:
            button.configure(fg_color="transparent", text_color=ACCENT, hover_color="#2a2638")


# ---------------------------------- helpers ----------------------------------
mouse = Controller()
picking = False

def pick_coords(x_entry, y_entry, name):

    global picking

    if picking:
        return

    picking = True
    status_label.configure(text=f"{name}: hover the target and press SPACE (Esc to cancel)")

    def fill(x, y):
        global picking

        x_entry.delete(0, "end")
        x_entry.insert(0, str(int(x)))
        y_entry.delete(0, "end")
        y_entry.insert(0, str(int(y)))

        status_label.configure(text=f"{name} set: {int(x)}, {int(y)}")
        picking = False

    def cancel():
        global picking
        status_label.configure(text="Pick cancelled")
        picking = False

    def on_press(key):
        if key == Key.space:
            x, y = mouse.position
            app.after(0, lambda: fill(x, y))
            return False  # stop this listener

        if key == Key.esc:
            app.after(0, cancel)
            return False

    Listener(on_press=on_press).start()


def make_coords_row(parent, title, x_placeholder, y_placeholder):

    frame = ctk.CTkFrame(parent, fg_color="transparent")
    frame.pack(pady=10)

    ctk.CTkLabel(
        frame,
        text=title,
        text_color=ACCENT,
    ).pack(side="top", anchor="w")

    entries_frame = ctk.CTkFrame(frame, fg_color="transparent")
    entries_frame.pack(side="top")

    x_entry = ctk.CTkEntry(
        entries_frame,
        placeholder_text=x_placeholder,
        width=69,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    x_entry.pack(side="left", padx=1)

    y_entry = ctk.CTkEntry(
        entries_frame,
        placeholder_text=y_placeholder,
        width=69,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    y_entry.pack(side="right", padx=1)

    ctk.CTkButton(
        frame,
        text="Pick position",
        width=142,
        height=24,
        text_color=BG,
        fg_color=ACCENT,
        hover_color=ACCENT_HOVER,
        command=lambda: pick_coords(x_entry, y_entry, title.rstrip(":"))
    ).pack(side="top", pady=(4, 0))

    return x_entry, y_entry

def make_coords_wait_row(parent, title, x_placeholder, y_placeholder, wait_placeholder="wait time (s)"):

    frame = ctk.CTkFrame(parent, fg_color="transparent")
    frame.pack(pady=10)

    ctk.CTkLabel(
        frame,
        text=title,
        text_color=ACCENT,
    ).pack(side="top", anchor="w")

    entries_frame = ctk.CTkFrame(frame, fg_color="transparent")
    entries_frame.pack(side="top")

    x_entry = ctk.CTkEntry(
        entries_frame,
        placeholder_text=x_placeholder,
        width=69,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    x_entry.pack(side="left", padx=1)

    y_entry = ctk.CTkEntry(
        entries_frame,
        placeholder_text=y_placeholder,
        width=69,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    y_entry.pack(side="right", padx=1)

    wait_entry = ctk.CTkEntry(
        frame,
        placeholder_text=wait_placeholder,
        width=142,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    wait_entry.pack(side="top", pady=(4, 0))

    ctk.CTkButton(
        frame,
        text="Pick position",
        width=142,
        height=24,
        text_color=BG,
        fg_color=ACCENT,
        hover_color=ACCENT_HOVER,
        command=lambda: pick_coords(x_entry, y_entry, title.rstrip(":"))
    ).pack(side="top", pady=(4, 0))

    return x_entry, y_entry, wait_entry

def center_window(window, width, height):

    scale = window._get_window_scaling()  # Windows display scaling (1.0, 1.25, 1.5...)

    x = int((window.winfo_screenwidth() - width * scale) / 2)
    y = int((window.winfo_screenheight() - height * scale) / 2)

    window.geometry(f"{width}x{height}+{x}+{y}")


#app entry_______________________________________________________________
app = ctk.CTk()
app.configure(fg_color=BG)
app.title("Dawia Quant")
center_window(app, 201, 413)
app.iconbitmap("assets/favicon.ico")
ctk.set_appearance_mode("dark")

app_name = ctk.CTkImage(
    light_image=Image.open("assets/ds.png"),
    dark_image=Image.open("assets/ds.png"),
    size=(130, 81)
)

#__________________________________navigation__________________________________
nav_frame = ctk.CTkFrame(app, fg_color="transparent")
#nav_frame.pack(pady=(0, 10))
nav_frame.pack(pady=0)

nav_buttons = {
    "controls": ctk.CTkButton(
        nav_frame,
        text="Controls",
        width=80,
        border_color=ACCENT,
        border_width=1,
        command=lambda: show_page("controls")
    ),
    "settings": ctk.CTkButton(
        nav_frame,
        text="Settings",
        width=80,
        border_color=ACCENT,
        border_width=1,
        command=lambda: show_page("settings")
    ),
}
nav_buttons["controls"].pack(side="left", padx=2, pady=(10, 0))
nav_buttons["settings"].pack(side="left", padx=2, pady=(10, 0))

#__________________________________header (always visible)__________________________________

title_frame = ctk.CTkFrame(app, fg_color="transparent")
title_frame.pack(pady=20)



title_label = ctk.CTkLabel(
    title_frame,
    image=app_name,
    text=""
)
title_label.pack(side="left")

#__________________________________status label (always visible, packed at bottom)__________________________________

status_label = ctk.CTkLabel(
    app,
    text="No stop key selected",
    text_color=ACCENT
)
status_label.pack(side="bottom", pady=15)

#__________________________________pages__________________________________

page_container = ctk.CTkFrame(app, fg_color="transparent")
page_container.pack(fill="both", expand=True)

controls_page = ctk.CTkFrame(page_container, fg_color="transparent")
settings_page = ctk.CTkScrollableFrame(
    page_container,
    fg_color="transparent",
    scrollbar_button_color=ACCENT,
    scrollbar_button_hover_color=ACCENT_HOVER
)

pages = {
    "controls": controls_page,
    "settings": settings_page,
}

#__________________________________page 1: buttons__________________________________

ctk.CTkButton(
    controls_page,
    text="Choose Stop Key",
    text_color=BG,
    fg_color=ACCENT,
    hover_color=ACCENT_HOVER,
    command=choose_stop_key
).pack(pady=(20, 10))

ctk.CTkButton(
    controls_page,
    text="START",
    text_color=BG,
    fg_color=ACCENT,
    hover_color=ACCENT_HOVER,
    command=start
).pack(pady=10)

ctk.CTkButton(
    controls_page,
    text="STOP",
    text_color=BG,
    fg_color=ACCENT,
    hover_color=ACCENT_HOVER,
    command=stop
).pack(pady=5)

#__________________________________page 2: coords + pixel distance__________________________________

sword_x_entry, sword_y_entry = make_coords_row(
    settings_page, "Sword Coordinates:", "sword x", "sword y"
)

mobs_x_entry, mobs_y_entry = make_coords_row(
    settings_page, "mobs Coordinates:", "mobs x", "mobs y"
)

scroll_x_entry, scroll_y_entry = make_coords_row(
    settings_page, "Scroll Coordinates:", "scroll x", "scroll y"
)

pixel_distance_entry = ctk.CTkEntry(
    settings_page,
    placeholder_text="Pixel Distance",
    fg_color=BG,
    border_color=ACCENT,
    border_width=1
)
pixel_distance_entry.pack(pady=10)

#__________________________________start__________________________________
SPLASH_MS = 2000
TRANSPARENT = "#010101"

def load_clean_logo(path, size, threshold=128):

    img = Image.open(path).convert("RGBA")
    img = img.resize(size, Image.LANCZOS)

    #make pixel visible or trans
    alpha = img.getchannel("A").point(lambda v: 255 if v > threshold else 0)
    img.putalpha(alpha)

    return img

def show_splash():

    app.withdraw()

    splash = ctk.CTkToplevel(app)
    splash.overrideredirect(True)
    splash.configure(fg_color=TRANSPARENT)
    splash.attributes("-topmost", True)
    splash.attributes("-transparentcolor", TRANSPARENT)
    logo_size = (442, 275)

    width, height = logo_size[0] + 20, logo_size[1] + 20
    x = (splash.winfo_screenwidth() - width) // 2
    y = (splash.winfo_screenheight() - height) // 2
    splash.geometry(f"{width}x{height}+{x}+{y}")

    splash.logo_image = ImageTk.PhotoImage(
        #load_clean_logo("assets/DawiaDS.png", (184, 240))
        #load_clean_logo("assets/ds.png", (280, 174))
        load_clean_logo("assets/ds.png", logo_size)
    )

    tk.Label(
        splash,
        image=splash.logo_image,
        bg=TRANSPARENT,
        borderwidth=0
    ).pack(expand=True)

    def finish():
        splash.destroy()
        app.deiconify()

    app.after(SPLASH_MS, finish)

show_page("controls")
load_settings()
show_splash()

listener = Listener(
    on_press=on_key_press
)

listener.start()

app.mainloop()