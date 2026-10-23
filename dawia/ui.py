import customtkinter as ctk
from PIL import Image

from dawia import state
from dawia.actions import choose_stop_key, start, stop
from dawia.config import ACCENT, ACCENT_HOVER, BG
from dawia.navigation import show_page
from dawia.widgets import make_coords_row


def center_window(window, width, height):

    scale = window._get_window_scaling()  # Windows display scaling (1.0, 1.25, 1.5...)

    x = int((window.winfo_screenwidth() - width * scale) / 2)
    y = int((window.winfo_screenheight() - height * scale) / 2)

    window.geometry(f"{width}x{height}+{x}+{y}")


def build_ui():

    app = ctk.CTk()
    state.app = app

    app.configure(fg_color=BG)
    app.title("Dawia Quant")
    center_window(app, 201, 413)
    app.iconbitmap("assets/favicon.ico")
    ctk.set_appearance_mode("dark")

    # the order matters: nav, header, status (bottom), then the pages
    _build_nav(app)
    _build_header(app)
    _build_status(app)
    _build_pages(app)


def _build_nav(app):

    nav_frame = ctk.CTkFrame(app, fg_color="transparent")
    nav_frame.pack(pady=0)

    state.nav_buttons["controls"] = ctk.CTkButton(
        nav_frame,
        text="Controls",
        width=80,
        border_color=ACCENT,
        border_width=1,
        command=lambda: show_page("controls")
    )
    state.nav_buttons["settings"] = ctk.CTkButton(
        nav_frame,
        text="Settings",
        width=80,
        border_color=ACCENT,
        border_width=1,
        command=lambda: show_page("settings")
    )

    state.nav_buttons["controls"].pack(side="left", padx=2, pady=(10, 0))
    state.nav_buttons["settings"].pack(side="left", padx=2, pady=(10, 0))


def _build_header(app):

    app_name = ctk.CTkImage(
        light_image=Image.open("assets/ds.png"),
        dark_image=Image.open("assets/ds.png"),
        size=(130, 81)
    )
    app.header_image = app_name  # keep a reference so the image isn't garbage collected

    title_frame = ctk.CTkFrame(app, fg_color="transparent")
    title_frame.pack(pady=20)

    title_label = ctk.CTkLabel(
        title_frame,
        image=app_name,
        text=""
    )
    title_label.pack(side="left")


def _build_status(app):

    state.status_label = ctk.CTkLabel(
        app,
        text="No stop key selected",
        text_color=ACCENT
    )
    state.status_label.pack(side="bottom", pady=15)


def _build_pages(app):

    page_container = ctk.CTkFrame(app, fg_color="transparent")
    page_container.pack(fill="both", expand=True)

    controls_page = ctk.CTkFrame(page_container, fg_color="transparent")
    settings_page = ctk.CTkScrollableFrame(
        page_container,
        fg_color="transparent",
        scrollbar_button_color=ACCENT,
        scrollbar_button_hover_color=ACCENT_HOVER
    )

    state.pages["controls"] = controls_page
    state.pages["settings"] = settings_page

    _fill_controls_page(controls_page)
    _fill_settings_page(settings_page)


def _fill_controls_page(page):

    ctk.CTkButton(
        page,
        text="Choose Stop Key",
        text_color=BG,
        fg_color=ACCENT,
        hover_color=ACCENT_HOVER,
        command=choose_stop_key
    ).pack(pady=(20, 10))

    ctk.CTkButton(
        page,
        text="START",
        text_color=BG,
        fg_color=ACCENT,
        hover_color=ACCENT_HOVER,
        command=start
    ).pack(pady=10)

    ctk.CTkButton(
        page,
        text="STOP",
        text_color=BG,
        fg_color=ACCENT,
        hover_color=ACCENT_HOVER,
        command=stop
    ).pack(pady=5)


def _fill_settings_page(page):

    entries = state.entries

    entries["sword_x"], entries["sword_y"] = make_coords_row(
        page, "Sword Coordinates:", "sword x", "sword y"
    )

    entries["mobs_x"], entries["mobs_y"] = make_coords_row(
        page, "mobs Coordinates:", "mobs x", "mobs y"
    )

    entries["scroll_x"], entries["scroll_y"] = make_coords_row(
        page, "Scroll Coordinates:", "scroll x", "scroll y"
    )

    entries["pixel_distance"] = ctk.CTkEntry(
        page,
        placeholder_text="Pixel Distance",
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    entries["pixel_distance"].pack(pady=10)
