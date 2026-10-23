import customtkinter as ctk

from dawia.config import ACCENT, ACCENT_HOVER, BG
from dawia.picker import pick_coords


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
