from dawia import state
from dawia.config import ACCENT, ACCENT_HOVER, BG


def show_page(name):

    for page in state.pages.values():
        page.pack_forget()

    state.pages[name].pack(fill="both", expand=True)

    for page_name, button in state.nav_buttons.items():
        if page_name == name:
            button.configure(fg_color=ACCENT, text_color=BG, hover_color=ACCENT_HOVER)
        else:
            button.configure(fg_color="transparent", text_color=ACCENT, hover_color="#2a2638")
