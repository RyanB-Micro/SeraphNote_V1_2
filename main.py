
import threading
import os

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import platform

from Project import Project
from Sheet import Sheet
from ScreenWindow import ScreenWindow

import file_control as files




class SeraphNoteApp:
    def __init__(self, root):
        self.active_project = Project()
        self.sheet_selected = False
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


        self.sheet_listbox = None
        self.sheet_name_entry = None

        # Declare tab frames
        self.main_tab = tk.Frame(self.notebook)
        #bond_tab = Frame(notebook)
        #node_tab = Frame(notebook)
        #fact_tab = Frame(notebook)
        #source_tab = Frame(notebook)
        self.generate_tabs()
        self.build_notebook()
        self.create_menus()


    def gen_main_tab(self):
        # Sheet List
        tk.Label(self.main_tab, text="Available Work Sheets").pack()
        self.sheet_listbox = tk.Listbox(self.main_tab)
        self.sheet_listbox.pack()

        # Sheet naming
        tk.Label(self.main_tab, text="Sheet Name: ").pack(side=tk.LEFT)
        self.sheet_name_entry = tk.Entry(self.main_tab, width=30)
        self.sheet_name_entry.pack(side=tk.LEFT, padx=7)

        # Sheet control
        add_sheet_button = tk.Button(self.main_tab, text="Add Sheet")
        add_sheet_button.config(command=lambda: self.add_sheet())
        add_sheet_button.pack()

        remove_sheet_button = tk.Button(self.main_tab, text="Remove Sheet")
        remove_sheet_button.config(command=lambda: self.delete_sheet())
        remove_sheet_button.pack()

        load_sheet_button = tk.Button(self.main_tab, text="Load Sheet")
        load_sheet_button.config(command=lambda: self.load_sheet())
        load_sheet_button.pack()


    def generate_tabs(self):
        self.gen_main_tab()

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

    def update_sheet_list(self):
        self.sheet_listbox.delete(0, tk.END)
        for sheet in self.active_project.project_sheets:
            if sheet.sheet_name not in self.sheet_listbox.get(0, tk.END):
                self.sheet_listbox.insert(tk.END, sheet.sheet_name)

    def add_sheet(self):
        sheet_name = self.sheet_name_entry.get()
        self.active_project.create_sheet(sheet_name)
        self.update_sheet_list()

    def delete_sheet(self):
        selected_list_index = self.sheet_listbox.curselection()
        if selected_list_index:
            index = selected_list_index[0]
            selection = self.sheet_listbox.get(index)
            self.active_project.delete_sheet(selection)
            self.update_sheet_list()

    def load_sheet(self):
        selected_list_index = self.sheet_listbox.curselection()
        if selected_list_index:
            index = selected_list_index[0]
            selection = self.sheet_listbox.get(index)
            for sheet_index, sheet in enumerate(self.active_project.project_sheets):
                if sheet.sheet_name == selection:
                    self.active_project.active_sheet_indx = sheet_index
                    self.sheet_selected = True

                    # Setup screen
                    self.screen_window.project_name = self.active_project.name
                    self.screen_window.sheet_name = self.active_project.project_sheets[self.active_project.active_sheet_indx].sheet_name

                    # Start screen
                    self.screen_window.running = True
                    #self.screen_loop()


    def save_project(self):
        # create directory if doest exist
        os.makedirs("SeraphNote_Saves\\", exist_ok=True)

        # Ensure a name wass entered
        if len(self.active_project.name) < 1:
            project_name = "SeraphNote__New_File__.pk1"
        else:
            project_name = self.active_project.name

        # Open file location window to save project
        file_name = filedialog.asksaveasfilename(initialfile=project_name, initialdir="SeraphNote_Saves\\",
                                            defaultextension=".pk1", filetypes=[("Project File", ".pk1")])

        files.save_project(self.active_project, file_name)


    def load_project(self):
            pass



    def start_screen(self):
        self.stop_event.clear()
        self.screen_thread = threading.Thread(target=self.screen_loop)

        self.screen_thread.start()

    def screen_loop(self):
        while not self.stop_event.is_set():
            if self.sheet_selected:
                #self.screen_window = ScreenWindow()
                while not self.stop_event.is_set():
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