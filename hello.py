# ----- BOILERPLATE

import sys, os

PS_DIR = os.path.expanduser("~/GITHUB/cassiel/pulse-sequencer/python")
# CHANGE THIS PART:          ^^^^^^^^^^^^^^^^^
if not PS_DIR in sys.path:
    sys.path.append(PS_DIR)

from core.interfacing import Outputter, CtrlOutput, KeyboardChain
from core.basis import Context
from lib.chains import Assembler, Transposer, Ranger, Indexer, Selector, Atom
from lib.pulses import Sprayer, Cycler

c = Context()
outputter = Outputter(maxObject, c, 0, 64, 100)
ctrl = CtrlOutput(maxObject, c, 0)

# Our pitches now randomly jump up a perfect 5th:
P0 = [60, 48, 62, 63, 65, 67]
P1 = Transposer(c, P0, 7)
P2 = Transposer(c, P0, 12)
pitches = Selector(c, Ranger(c, '13'), P0, P1, P2)

# We need a control pulse to drive the FX knob:
ctrlP = Cycler(c, [0, 64, 127], ctrl, firstIf='', nextIf='..', loopIf='..')

fan = Sprayer(c, outputter.pitch, outputter.emit, ctrlP)

pitcher = Cycler(c, pitches, fan, firstIf=0, nextIf='..', loopIf='..')

patt = Selector(c,
                Ranger(c, [1, 2]),
                '01.10.11',
                '1..11.11')

main = Cycler(c, patt, pitcher, firstIf=0, nextIf='..', loopIf='..')

# these are the same:
# [1, 2, 3, None, 1, 1]
# '123.11'


def button(i, val): pass
def dial(i, val): pass
def note(p, v): pass

def clock(i):
    c.tick()
    main.fire(i)

import time
maxObject.outlet(2, "Loaded [...] at %s" % time.asctime(time.localtime(time.time())))
