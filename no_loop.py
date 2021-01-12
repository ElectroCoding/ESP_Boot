import time
from machine import Pin

led4 = Pin(4, Pin.OUT)

i = 1


led4(1)
time.sleep(1)
led4(0)
time.sleep(1)
print (i)
