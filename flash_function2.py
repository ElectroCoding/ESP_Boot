import time
from machine import Pin

led4 = Pin(4, Pin.OUT)



def flash_it():
    x = 1
    while x < 10:
        led4(1)
        time.sleep(1)
        led4(0)
        time.sleep(1)
        x =+ 1