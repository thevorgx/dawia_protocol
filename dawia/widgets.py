import customtkinter as ctk

from dawia import state
from dawia.config import ACCENT, ACCENT_HOVER, BG
from dawia.picker import pick_coords, pick_region


def make_coords_row(parent, title, x, y):

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
        placeholder_text=x,
        width=69,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    x_entry.pack(side="left", padx=1)

    y_entry = ctk.CTkEntry(
        entries_frame,
        placeholder_text=y,
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



def make_region_wait_row(parent, title, x1, y1, x2, y2, wait_placeholder="wait time (s)"):

    frame = ctk.CTkFrame(parent, fg_color="transparent")
    frame.pack(pady=10)

    ctk.CTkLabel(
        frame,
        text=title,
        text_color=ACCENT,
    ).pack(side="top", anchor="w")

    # point 1
    entries_frame_1 = ctk.CTkFrame(frame, fg_color="transparent")
    entries_frame_1.pack(side="top")

    x1_entry = ctk.CTkEntry(
        entries_frame_1,
        placeholder_text=x1,
        width=69,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    x1_entry.pack(side="left", padx=1)

    y1_entry = ctk.CTkEntry(
        entries_frame_1,
        placeholder_text=y1,
        width=69,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    y1_entry.pack(side="right", padx=1)

    # point 2
    entries_frame_2 = ctk.CTkFrame(frame, fg_color="transparent")
    entries_frame_2.pack(side="top", pady=(4, 0))

    x2_entry = ctk.CTkEntry(
        entries_frame_2,
        placeholder_text=x2,
        width=69,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    x2_entry.pack(side="left", padx=1)

    y2_entry = ctk.CTkEntry(
        entries_frame_2,
        placeholder_text=y2,
        width=69,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    y2_entry.pack(side="right", padx=1)

    # wait time
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
        text="Pick region",
        width=142,
        height=24,
        text_color=BG,
        fg_color=ACCENT,
        hover_color=ACCENT_HOVER,
        command=lambda: pick_region(
            x1_entry, y1_entry, x2_entry, y2_entry, title.rstrip(":")
        )
    ).pack(side="top", pady=(4, 0))

    return x1_entry, y1_entry, x2_entry, y2_entry, wait_entry



def make_region_randwait_row(parent, title, x1, y1, x2, y2, time_min, time_max):

    frame = ctk.CTkFrame(parent, fg_color="transparent")
    frame.pack(pady=10)

    ctk.CTkLabel(
        frame,
        text=title,
        text_color=ACCENT,
    ).pack(side="top", anchor="w")

    # point 1
    entries_frame_1 = ctk.CTkFrame(frame, fg_color="transparent")
    entries_frame_1.pack(side="top")

    x1_entry = ctk.CTkEntry(
        entries_frame_1,
        placeholder_text="x1",
        width=69,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    x1_entry.pack(side="left", padx=1)

    y1_entry = ctk.CTkEntry(
        entries_frame_1,
        placeholder_text="y1",
        width=69,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    y1_entry.pack(side="right", padx=1)

    # point 2
    entries_frame_2 = ctk.CTkFrame(frame, fg_color="transparent")
    entries_frame_2.pack(side="top", pady=(4, 0))

    x2_entry = ctk.CTkEntry(
        entries_frame_2,
        placeholder_text="x2",
        width=69,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    x2_entry.pack(side="left", padx=1)

    y2_entry = ctk.CTkEntry(
        entries_frame_2,
        placeholder_text="y2",
        width=69,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    y2_entry.pack(side="right", padx=1)

    # wait time
    entries_frame_3 = ctk.CTkFrame(frame, fg_color="transparent")
    entries_frame_3.pack(side="top", pady=(4, 0))

    wait_entry_min = ctk.CTkEntry(
        entries_frame_3,
        placeholder_text="time_min",
        width=69,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    wait_entry_min.pack(side="left", padx=1)

    wait_entry_max = ctk.CTkEntry(
        entries_frame_3,
        placeholder_text="time_max",
        width=69,
        fg_color=BG,
        border_color=ACCENT,
        border_width=1
    )
    wait_entry_max.pack(side="right", padx=1)

    ctk.CTkButton(
        frame,
        text="Pick region",
        width=142,
        height=24,
        text_color=BG,
        fg_color=ACCENT,
        hover_color=ACCENT_HOVER,
        command=lambda: pick_region(
            x1_entry, y1_entry, x2_entry, y2_entry, title.rstrip(":")
        )
    ).pack(side="top", pady=(4, 0))

    state.pairs.append((x1_entry, x2_entry, True))               # x1 must be greater than x2
    state.pairs.append((y1_entry, y2_entry, True))               # y1 must be greater than y2
    state.pairs.append((wait_entry_min, wait_entry_max, False))  # min must be smaller than max

    return x1_entry, y1_entry, x2_entry, y2_entry, wait_entry_min, wait_entry_max