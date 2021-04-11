from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import function
import time
import system

FORM_MAIN = -1
FORM_CLOCK = 0
FORM_REMOTE = 1
FORM_CCTV = 2
FORM_SETTING = 3

class QtUI(object) :
    def __init__(self) :

        self.app = QApplication([])
        self.form = uic.loadUiType("ui/main.ui")[0]()
        self.window = uic.loadUiType("ui/main.ui")[1]()
        self.setting_form = uic.loadUiType("ui/setting.ui")[0]()
        self.setting_window = uic.loadUiType("ui/setting.ui")[1]()
        self.clock_form = uic.loadUiType("ui/clock.ui")[0]()
        self.clock_window = uic.loadUiType("ui/clock.ui")[1]()
        self.form.setupUi(self.window)

        if system.is_raspi() :
            self.window.showFullScreen()
        else :
            self.window.show()

        self.form_index = FORM_MAIN
        

    def set_style_sheet(self):
        return
        self.window.setStyleSheet("background-color: blue")

    def connect_event(self, menu):
        self.form_index = menu
        if menu == FORM_MAIN:
            self.form.exitButton.clicked.connect(self.on_clicked_exit_button)
            self.form.menuButton0.clicked.connect(self.on_clicked_menu_button_0)
            self.form.menuButton1.clicked.connect(self.on_clicked_menu_button_1)
            self.form.menuButton2.clicked.connect(self.on_clicked_menu_button_2)
            self.form.menuButton3.clicked.connect(self.on_clicked_menu_button_3)
            self.form.menuButton4.clicked.connect(self.on_clicked_menu_button_4)
            self.form.menuButton5.clicked.connect(self.on_clicked_menu_button_5)
        elif menu == FORM_CLOCK :
            self.clock_form.backButton.clicked.connect(self.on_clicked_back_button)
        elif menu == FORM_SETTING :
            self.setting_form.backButton.clicked.connect(self.on_clicked_back_button)
        

    def on_clicked_exit_button(self):
        self.app.exit()

    def on_clicked_back_button(self):
        self.form.setupUi(self.window)
        self.window.setCentralWidget(self.form.frame)
        self.connect_event(FORM_MAIN)

    def on_clicked_menu_button_0(self):
        self.clock_form.setupUi(self.window)
        self.window.setCentralWidget(self.clock_form.frame)
        self.connect_event(0)

    def on_clicked_menu_button_1(self):
        self.setting_form.setupUi(self.window)
        self.window.setCentralWidget(self.setting_form.frame)
        self.connect_event(1)

    def on_clicked_menu_button_2(self):
        self.setting_form.setupUi(self.window)
        self.window.setCentralWidget(self.setting_form.frame)
        self.connect_event(2)

    def on_clicked_menu_button_3(self):
        self.setting_form.setupUi(self.window)
        self.window.setCentralWidget(self.setting_form.frame)
        self.connect_event(3)

    def on_clicked_menu_button_4(self):
        self.setting_form.setupUi(self.window)
        self.window.setCentralWidget(self.setting_form.frame)
        self.connect_event(4)

    def on_clicked_menu_button_5(self):
        self.setting_form.setupUi(self.window)
        self.window.setCentralWidget(self.setting_form.frame)
        self.connect_event(5)

    def update_ui(self):
        if self.form_index == FORM_CLOCK:
            self.update_clock()
    
    def update_clock(self):
        now = time.localtime()
        self.clock_form.lcdHour.display(now.tm_hour)
        self.clock_form.lcdMin.display(now.tm_min)
        self.clock_form.lcdSec.display(now.tm_sec)

    def thread_loop(self, delay):
        while True:
            self.update_ui()
            time.sleep(delay)
        

    def thread_start(self):
        self.set_style_sheet()
        self.connect_event(FORM_MAIN)
        function.asyncf(self.thread_loop, 0.4)
        self.app.exec()

    

qtui = QtUI()

if __name__ == "__main__" :
    qtui.thread_start()
