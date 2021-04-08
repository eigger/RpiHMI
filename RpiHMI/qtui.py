from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import function
import time
import system



class QtUI(object) :
    def __init__(self) :

        self.app = QApplication([])
        self.form = uic.loadUiType("main.ui")[0]()
        self.window = uic.loadUiType("main.ui")[1]()
        self.setting_form = uic.loadUiType("setting.ui")[0]()
        self.setting_window = uic.loadUiType("setting.ui")[1]()
        self.form.setupUi(self.window)
        if system.is_raspi() :
            self.window.showFullScreen()
        else :
            self.window.show()

        
        

    def set_style_sheet(self):
        self.window.setStyleSheet("background-color: blue")

    def connect_event(self):
        self.form.exitButton.clicked.connect(self.on_clicked_exit_button)
        self.form.settingButton.clicked.connect(self.on_clicked_setting_button)

    def on_clicked_exit_button(self):
        self.app.exit()

    def on_clicked_setting_button(self):
        self.setting_form.setupUi(self.window)
        self.window.setcentralwidget = self.setting_form
        self.window.show()

    def update_ui(self):
        self.form.lcdNumber.display(1)

    def thread_loop(self, delay):
        while True:
            self.update_ui()
            time.sleep(delay)
        

    def thread_start(self):
        self.set_style_sheet()
        self.connect_event()
        function.asyncf(self.thread_loop, 0.4)
        self.app.exec()

    

qtui = QtUI()

if __name__ == "__main__" :
    qtui.thread_start()
