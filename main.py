from tkinter import ttk
import threading
from Project import Project
from Sheet import Sheet
from ScreenWindow import ScreenWindow


# Control tabs
main_tab = None

# TODO: Load from file
active_project = Project()

# Threads
stop_event = threading.Event()
screen_thread = None
window = None

def screen_loop():
    global window
    window = ScreenWindow()
    window.start_screen()
    window.display_loop()

    # Kill threat when screen loop is closed
    stop_event.set()


def start_screen_loop():
    global stop_event, screen_thread, window
    # Start window thread
    stop_event.clear()
    screen_thread = threading.Thread(target=screen_loop)

    screen_thread.start()

def stop_screen_loop():
    stop_event.set()



def main():
    start_screen_loop()

    # Stop screen thread
    #stop_screen_loop()


if __name__ == "__main__":
    main()


























# † "For God so loved the world, that he gave his one and only Son, so that whoever believes in him should not perish, but get to live an everlasting life - John 3:16" †