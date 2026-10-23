import tkinter as tk

import customtkinter as ctk
from PIL import Image, ImageTk

from dawia import state
from dawia.config import SPLASH_MS, TRANSPARENT


def load_clean_logo(path, size, threshold=128):

    img = Image.open(path).convert("RGBA")
    img = img.resize(size, Image.LANCZOS)

    # make every pixel either fully visible or fully transparent
    alpha = img.getchannel("A").point(lambda v: 255 if v > threshold else 0)
    img.putalpha(alpha)

    return img


def show_splash():

    app = state.app
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
