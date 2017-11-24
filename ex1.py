# Starting example: simple sequencing.

# Wheel in the pulse sequencer itself:
import sys, os

PS_DIR = os.path.expanduser("~/GITHUB/cassiel/pulse-sequencer/python")
if not PS_DIR in sys.path:
    sys.path.append(PS_DIR)

from core.interfacing import Outputter
from core.basis import Context
from lib.chains import Assembler, Transposer, Ranger, Indexer, Selector, Atom
from lib.pulses import Sprayer, Cycler

# We need a "context" to do some book-keeping as we build chains and sequences:
c = Context()

# We need an outputter which generates notes (with default velocity and duration).
# The outputter is a set of pulses: pitch, velocity, duration, emit.
outputter = Outputter(maxObject, c, 0, 64, 100)

# Let's assemble some pitches as a chain:
P = Assembler(c, 58, 60, 63, 53, 65)

# We need a pulse which will plant a pitch, and then emit a note:
fan = Sprayer(c, outputter.pitch, outputter.emit)

# We need a pulse which will take the clock messages and cycle along the fan:
input = Cycler(c, P, fan, firstIf=0, nextIf='..', loopIf='..')

# (Q: what happens if you send clocks directly to the fan?)

# All done. Send the clock counter messages to the input pulse:
def clock(i):
    c.tick()
    input.fire(i)

# Put out a message (into the patcher) to confirm that we've loaded:
import time
maxObject.outlet(1, "Loaded ex1 at %s" % time.asctime(time.localtime(time.time())))

#for i in sys.path:
#    print i
