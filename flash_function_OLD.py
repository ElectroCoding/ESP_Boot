import time
from machine import Pin

led4 = Pin(4, Pin.OUT)


def flash_it():
    while True:
        led4(1)
        time.sleep(1)
        led4(0)
        time.sleep(1)




    