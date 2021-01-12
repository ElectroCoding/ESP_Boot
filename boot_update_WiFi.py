# This file is executed on every boot (including wake-boot from deepsleep)
# This was Updated on 3/22/18 by Rob
# I uncommented the 2 esp commands to see if it resolves
# the errors that show up the first time I run commands at the Windows prompt.
# It also has the WebREPL commands enabled

import esp
esp.osdebug(None)
import gc
import webrepl
webrepl.start()
gc.collect()