# how to add LFOs
# this shit is craaaazy

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

s = Server().boot().start()
# s.amp = 0.1 # turn down 20dB

# create noise source?
n = Noise()

# create LFO, wow this is a big oscillation...
# center frequency is 1khz, sweeping 0.5khz
lfo1 = Sine(freq=0.1, mul=500, add=1000)
# LFO oscillating between 2 and 8 (Q factor)
lfo2 = Sine(freq=0.4).range(2,8)
# creates a butterworth bandpass filter
# with the center frequency modded by lfo1 and the
# Q modded by lfo2!!
# bp1 = ButBP(input=n, freq=lfo1, q=lfo2).out()

# There is an LFO object htat provides even more waveforms

# ramp oscillatin +/1 1000 around 1.2khz
lfo3 = LFO(freq=0.25, type=1, mul=1000, add=1200)
# create square Q oscillating b/w 4 and 12
lfo4 = LFO(freq=0.4, type=2).range(4, 12)
# creates 2nd dynamic bp filter applied to noise source
# does this override the previous, or does this add to the previous?
# or does this cascade with the previous?
bp2 = ButBP(input=n, freq=lfo3, q=lfo4).out()

# check out this cool gui
s.gui(locals())

# s.stop()