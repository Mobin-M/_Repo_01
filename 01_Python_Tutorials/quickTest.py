# SuperFastPython.com
# example of executing a target task function in a separate thread
from time import sleep
from threading import Thread

b = 5
def func():
    print(b)

func()

