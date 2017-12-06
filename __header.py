# ----- BOILERPLATE

import sys, os

PS_DIR = os.path.expanduser("~/GITHUB/cassiel/pulse-sequencer/python")
if not PS_DIR in sys.path:
    sys.path.append(PS_DIR)

from core.interfacing import Outputter, CtrlOutput, KeyboardChain
from core.basis import Context
from lib.chains import Assembler, Transposer, Ranger, Indexer, Selector, Atom
from lib.pulses import Sprayer, Cycler

c = Context()
outputter = Outputter(maxObject, c, 0, 64, 100)
ctrl = CtrlOutput(maxObject, c, 0)
