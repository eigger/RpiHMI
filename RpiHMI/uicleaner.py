import tkinter
from tkinter.simpledialog import askstring
import system
import time
import function
from time import strftime
from functools import partial
import ui
class UICleaner(ui.UI):

    def __init__(self, window):
        super().__init__(window)

        #480 320
        self.menu_frame = tkinter.Frame(self.main_frame)
        self.menu_frame.place(x=0, y=0, width=480, height=320/4)

        self.menu_frame = tkinter.Frame(self.main_frame)
        self.menu_frame.place(x=0, y=320/4*1, width=480, height=320/4)
        self.menu_button = tkinter.Button(self.menu_frame, bg="black", fg="white", width=15, text="FW", font = ("Graphic", 20, 'bold'), command=partial(self.clickCleaner, 0))
        self.menu_button.pack(side="left")
        self.menu_button = tkinter.Button(self.menu_frame, bg="black", fg="white", width=15, text="BW", font = ("Graphic", 20, 'bold'), command=partial(self.clickCleaner, 1))
        self.menu_button.pack(side="left")

        self.menu_frame = tkinter.Frame(self.main_frame)
        self.menu_frame.place(x=0, y=320/4*2, width=480, height=320/4)
        self.menu_button = tkinter.Button(self.menu_frame, bg="black", fg="white", width=15, text="STOP", font = ("Graphic", 20, 'bold'), command=partial(self.clickCleaner, 1))
        self.menu_button.pack(side="left")


        self.menu_frame = tkinter.Frame(self.main_frame)
        self.menu_frame.place(x=0, y=320/4*3, width=480, height=320/4)
        self.menu_button = tkinter.Button(self.menu_frame, bg="black", fg="white", width=15, text="Speed Up", font = ("Graphic", 20, 'bold'), command=partial(self.clickCleaner, 2))
        self.menu_button.pack(side="left")
        self.menu_button = tkinter.Button(self.menu_frame, bg="black", fg="white", width=15, text="Speed Down", font = ("Graphic", 20, 'bold'), command=partial(self.clickCleaner, 3))
        self.menu_button.pack(side="left")

        self.back_button = tkinter.Button(self.main_frame , bg="black", fg="white", text="Back", font = ("Graphic", 10, 'bold'), command=partial(self.clickMenu, 0))
        self.back_button.place(x=0, y=0, width=60, height=40)
    def clickCleaner(self, menu):
        return