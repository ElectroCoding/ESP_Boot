# This file is executed on every boot (including wake-boot from deepsleep)
# 3/11/18 I uncommented the following two lines to stop errors
# 
import esp
esp.osdebug(None)
import gc
#import webrepl
#webrepl.start()
gc.collect()
