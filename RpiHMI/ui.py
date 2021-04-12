import tkinter
class UI(object):

    def __init__(self, window):
        self.window = window
        self.main_frame = tkinter.Frame(window, bg="black")
        self.main_frame.place(x=0, y=0, width=480, height=320)

    def place_forget(self):
        self.main_frame.place_forget()

    def callback(self, func):
        self.callback = func
    
    def clickMenu(self, menu):
        self.callback(menu)

    def update_view(self):
        pass