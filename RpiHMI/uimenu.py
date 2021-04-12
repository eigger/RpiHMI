import tkinter
from tkinter.simpledialog import askstring
import system
import time
import function
from time import strftime
from functools import partial
import ui
class UIMenu(ui.UI):

    def __init__(self, window):
        super().__init__(window)
        self.menu_button = tkinter.Button(self.main_frame, bg="black", fg="white", width=15, text="Clock", font = ("Graphic", 20, 'bold'), command=partial(self.clickMenu, 1))
        self.menu_button.pack(expand=True)
        self.menu_button = tkinter.Button(self.main_frame, bg="black", fg="white", width=15, text="Cleaner", font = ("Graphic", 20, 'bold'), command=partial(self.clickMenu, 2))
        self.menu_button.pack(expand=True)
        self.exit_button = tkinter.Button(self.main_frame, bg="black", fg="white", text="x", command=self.clickExitButton)
        self.exit_button.place(x=465, y=0, width=15, height=15)

    def clickExitButton(self):
        password = askstring('Password', 'Enter password:', show="*")
        if password == None:
            return
        self.window.destroy()
