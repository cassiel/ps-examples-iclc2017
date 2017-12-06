# Let's assemble some pitches as a chain:
P = Assembler(c, 58, 60, 63, 53, 65)

# We need a pulse which will plant a pitch, and then emit a note:
fan = Sprayer(c, outputter.pitch, outputter.emit)

# We need a pulse which will take the clock messages and cycle along the fan:
main = Cycler(c, P, fan, firstIf=[0, 0], nextIf=[None, None], loopIf=[None, None])

# (Q: what happens if you send clocks directly to the fan?)

# Hint: we can modify firstIf, nextIf etc. to get different looping behaviour.

# Also, shortcuts: [0, 0] -> 0, [None, None] -> '..'.
