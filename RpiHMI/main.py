
import time
import threading

from mqttclient import mqttclient
from qtui import qtui

#sudo apt install python3-paho-mqtt
def init():
    print("init")

def start():
    #mqttclient.thread_start()
    print("start")

def exit():
    print("exit")

def wait():
    qtui.thread_start()

if __name__ == '__main__':
    init()
    start()
    wait()
    exit()

