import threading
import sys, os
from pynput.keyboard import Controller, Key, Listener
import time

global keyNow 
keyNow = 'o'
def on_press(key):
    global keyNow
    try:
        print("正在按压：", format(key.char))
        keyNow = format(key.char)
    except AttributeError:
        print("正在按压：", format(key))
        keyNow = format(key)


def on_release(key):
    global keyNow
    keyNow = None
    print("已经释放：", format(key))
    

    

def start_listen():
    kb = Controller()
    with Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()


def showKey():
    global keyNow
    while 1:
        time.sleep(1)
        print('keyNow = ', keyNow)



if __name__ == "__main__":
    
    o = threading.Thread(target = start_listen,args = ())
    o.start()
    t = threading.Thread(target = showKey,args = ())
    t.start()

        

        