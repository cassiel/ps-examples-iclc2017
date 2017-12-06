# ----- INTERFACING

def button(i, val): pass
def dial(i, val): pass
def note(p, v): pass

def clock(i):
    c.tick()
    main.fire(i)

import time
maxObject.outlet(2, "Loaded [...] at %s" % time.asctime(time.localtime(time.time())))
