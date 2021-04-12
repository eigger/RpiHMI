import tkinter
from tkinter.simpledialog import askstring
import system
import time
import function
from time import strftime
from functools import partial
import ui
class UIClock(ui.UI):

    def __init__(self, window):
        super().__init__(window)
        self.back_button = tkinter.Button(self.main_frame , bg="black", fg="white", text="Back", font = ("Graphic", 10, 'bold'), command=partial(self.clickMenu, 0))
        self.back_button.place(x=0, y=0, width=60, height=40)
        self.date_label = tkinter.Label(self.main_frame , bg="black", fg="white", font = ("Graphic", 20, 'bold'), relief='flat')
        self.date_label.pack(expand=True)
        self.time_label = tkinter.Label(self.main_frame , bg="black", fg="white", font = ("Graphic", 45, 'bold'), relief='flat')
        self.time_label.pack(expand=True)
        self.text_label = tkinter.Label(self.main_frame , bg="black", fg="white", font = ("Graphic", 45, 'bold'), relief='flat')
        self.text_label.pack(expand=True)
        self.time_label.bind("<Button>", self.clickTimeLabel)
        self.display_index = 0
        self.display_str = ""
        self.display_queue = []
        self.easter_eggs_flag = 0

    def update_label(self):
        self.update_date()
        self.update_time()
        self.update_text()

    def update_date(self):
        current_date = strftime("%Y년 %m월 %d일")
        self.date_label.configure(text = current_date)

    def update_time(self):
        current_time = strftime('%H시 %M분 %S초')
        self.time_label.configure(text = current_time)

    def update_text(self):
        if len(self.display_str) <= 0:
            return
        end = self.display_index
        start = end - 9
        if start < 0:
            start = 0
        self.text_label.configure(text = "%s" % self.display_str[start:end], anchor = "e")
        self.display_index += 1
        if start >= len(self.display_str):
            self.display_index = 0
            self.display_str = ""

    def update_easter_eggs(self):
        self.easter_eggs_flag -= 1
        if self.easter_eggs_flag > 1:
            self.easter_eggs_flag = 0
            self.add_text("안나 희성")
        elif self.easter_eggs_flag < 0:
            self.easter_eggs_flag = 0
        

    def pop_text(self):
        if len(self.display_str) > 0:
            return
        if len(self.display_queue) == 0:
            return
        self.display_str = self.display_queue.pop(0)
        #print("Pop %d" %(len(self.display_queue)))


    def add_text(self, text):
        self.display_queue.append(text)
        #print("Add %d" %(len(self.display_queue)))

    def clickTimeLabel(self, event) :
        self.easter_eggs_flag += 1
        print(self.easter_eggs_flag)

    def update_view(self):
        self.pop_text()
        self.update_label()
        self.update_easter_eggs()
