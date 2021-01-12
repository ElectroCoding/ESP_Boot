import time
from machine import Pin

led4 = Pin(4, Pin.OUT)


def flash_it():
    print ('this is printed from inside flash_it function')