
import time
import threading

from mqttclient import mqttclient
from ui import ui

#sudo apt install python3-paho-mqtt
def init():
    print("init")

def start():
    #mqttclient.thread_start()
    print("start")

def exit():
    print("exit")

def wait():
    ui.thread_start()

if __name__ == '__main__':
    init()
    start()
    wait()
    exit()

