
import tkinter
import system
import uiclock
import function
import uimenu
import uicleaner

class UIMain(object):

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Clock")
        self.window.geometry("480x320+0+0")
        self.window.configure(bg="black")
        self.window.resizable(False, False)
        if system.is_raspi() :
            self.window.attributes('-fullscreen', True)

        self.ui = uimenu.UIMenu(self.window)
        self.ui.callback(self.callback_menu)


    def update_view(self):
        self.ui.update_view()
        function.timerf(0.4, self.update_view)

    def callback_menu(self, menu):
        self.ui.place_forget()
        if menu == 0:
            self.ui = uimenu.UIMenu(self.window)
            self.ui.callback(self.callback_menu)
        elif menu == 1:
            self.ui = uiclock.UIClock(self.window)
            self.ui.callback(self.callback_menu)
        elif menu == 2:
            self.ui = uicleaner.UICleaner(self.window)
            self.ui.callback(self.callback_menu)

    def thread_start(self):
        self.update_view()
        self.window.mainloop()


uimain = UIMain()
if __name__ == '__main__':
    uimain.thread_start()