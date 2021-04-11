import threading
import time
def asyncf(func, *args):
    thread = threading.Thread(target=func, args=(args))
    thread.daemon = True
    thread.start()

def timerf(interval, func, *args):
    thread = threading.Timer(interval, func, args)
    thread.daemon = True
    thread.start()

if __name__ == '__main__':
    print("start")
