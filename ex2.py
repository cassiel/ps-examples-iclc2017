# ex2: transposition; velocities and durations.

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
P = Assembler(c, 60, 62, 63, 65, 67)

# I want to transpose that down an octave:
P_12 = Transposer(c, P, -12)

# (Here, '-12' is a chain.)

# And just because we can, let's concatenate them:
P_all = Assembler(c, P, P_12)

# Now, let's look at velocities: we'll cycle these three values:
vels = [20, 60, 127]

# (In this simple case we can just write the list.)

# Here's a pulse which cycles them (regardless of what we send it):
vel_P = Cycler(c, vels, outputter.velocity, firstIf='', nextIf='..', loopIf='..')

# Ditto for durations:
durs = [50, 150]
dur_P = Cycler(c, durs, outputter.duration, firstIf='', nextIf='..', loopIf='..')

# (Note the '' for firstIf: never reset. '..' would be always reset.)

# We need a pulse which will plant a pitch, kick the velocity generator, and then emit a note:
fan = Sprayer(c, outputter.pitch, vel_P, dur_P, outputter.emit)

# We need a pulse which will take the clock messages and cycle along the fan:
input = Cycler(c, P_all, fan, firstIf=0, nextIf='..', loopIf='..')

# (Q: what happens if you send clocks directly to the fan?)

# Hint: we can modify firstIf, nextIf etc. to get different looping behaviour.

# All done. Send the clock counter messages to the input pulse:
def clock(i):
    c.tick()
    input.fire(i)

# Put out a message (into the patcher) to confirm that we've loaded:
import time
maxObject.outlet(1, "Loaded ex1 at %s" % time.asctime(time.localtime(time.time())))

#for i in sys.path:
#    print i
