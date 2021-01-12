import time
from machine import Pin

led4 = Pin(4, Pin.OUT)

def flash_10():
    x = 1
    while x < 11:
        led4(1)
        time.sleep(.5)
        led4(0)
        time.sleep(.5)
        x += 1

def flash_fast():
    x = 1
    while x < 11:
        led4(1)
        time.sleep(.1)
        led4(0)
        time.sleep(.1)
        x += 1


def flash_sos():
    z = 1
    
    while z < 4:
        x = 1
        while x < 4:
            
            led4(1)
            time.sleep(.3)
            led4(0)
            time.sleep(.3)
            x += 1
        
        x = 1
        while x < 7:
            
            led4(0)
            time.sleep(.3)
            x += 1

        x = 1
        while x < 4:
            
            led4(1)
            time.sleep(.3)
            led4(0)
            time.sleep(.3)
            x += 1

        x = 1
        while x < 14:
            
            led4(0)
            time.sleep(.3)
            x += 1

        z += 1