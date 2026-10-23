from pynput.keyboard import Listener
from dawia import state
from dawia.actions import on_key_press
from dawia.navigation import show_page
from dawia.settings import load_settings
from dawia.splash import show_splash
from dawia.ui import build_ui



def main():

    build_ui()
    show_page("controls")
    load_settings()
    show_splash()

    listener = Listener(
        on_press=on_key_press
    )
    listener.start()

    state.app.mainloop()

if __name__ == "__main__":
    main()
