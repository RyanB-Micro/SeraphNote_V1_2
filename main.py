
import threading

import tkinter as tk
from tkinter import ttk
import platform

from Project import Project
from Sheet import Sheet
from ScreenWindow import ScreenWindow





class SeraphNoteApp:
    def __init__(self, root):
        self.active_project = Project()
        self.screen_window = None

        # Threads
        self.stop_event = threading.Event()
        self.screen_thread = None
        self.screen_window = ScreenWindow()

        # TK window attributes
        self.root = root
        self.root.title("SeraphNote Project Manager")
        self.root.protocol("WM_DELETE_WINDOW", self.quit_all)
        self.root.geometry("400x300")

        # Create notebook for storing tabs
        self.notebook = ttk.Notebook(self.root)

        # Declare tab frames
        self.main_tab = tk.Frame(self.notebook)
        #bond_tab = Frame(notebook)
        #node_tab = Frame(notebook)
        #fact_tab = Frame(notebook)
        #source_tab = Frame(notebook)
        self.generate_tabs()
        self.build_notebook()
        self.create_menus()


    def generate_tabs(self):
        pass

    def build_notebook(self):
        self.notebook.add(self.main_tab, text="Main Control")
        self.notebook.pack(expand=1, fill="both")

    def create_menus(self):
        # Declare menus
        self.menu = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.info_menu = tk.Menu(self.menu, tearoff=False)

        # File menu options
        self.file_menu.add_command(label="Save Project", command=self.save_project)
        self.file_menu.add_command(label="Load Project", command=self.load_project)

        # Info menu options
        self.info_menu.add_command(label="Python Ver. " + str(platform.python_version()))
        self.info_menu.add_command(label="PyGame Ver. " + str(self.screen_window.pygame_version))

        # Add menus within eachother
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.menu.add_cascade(label="Info", menu=self.info_menu)

        # Add menu to window
        self.root.config(menu=self.menu)


    def save_project(self):
        pass

    def load_project(self):
        pass



    def start_screen(self):
        self.stop_event.clear()
        self.screen_thread = threading.Thread(target=self.screen_loop)

        self.screen_thread.start()

    def screen_loop(self):
        self.screen_window = ScreenWindow()
        self.screen_window.start_screen()
        self.screen_window.display_loop()

        # Kill threat when screen loop is closed
        self.stop_event.set()


    def stop_screen_loop(self):
        self.stop_event.set()
        self.screen_window.running = False
        self.screen_thread.join()
        self.screen_window = None

    def quit_all(self):
        # pygame thread stop
        self.stop_event.set()
        self.screen_window.running = False
        self.screen_thread.join()
        self.screen_window = None
        # root window stop
        self.root.quit()
        self.root.destroy()



def main():
    root = tk.Tk()
    app = SeraphNoteApp(root)
    app.start_screen()
    root.mainloop()


    # Stop screen thread
    app.quit_all()


if __name__ == "__main__":
    main()


























# † "For God so loved the world, that he gave his one and only Son, so that whoever believes in him should not perish, but get to live an everlasting life - John 3:16" †