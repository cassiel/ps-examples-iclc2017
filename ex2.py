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
main = Cycler(c, P_all, fan, firstIf=0, nextIf='..', loopIf='..')
