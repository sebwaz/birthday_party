# pyo's doc is stressing that these random generator objects can be used for a lot of things
# worth looking deeper into

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

# boot
s = Server().boot()

# 2 streams of midi pitches chosen randomly in a predefined list
# argument 'choice' of Choice can be a list of lists to list-expansion
# freq = frequency of polling, unsure what it means when freq is a list
mid = Choice(choice = [60,62,63,65,67,69,71,72], freq=[2,3])

# two small jitters applied on freq streams
# randi interpolates bw old and new values.
jit = Randi(min=0.993, max=1.007, freq=[4.3,3.5])

# converts midi pitches to frequencies and appplies the jitters
fr = MToF(mid, mul=jit)

# chooses new feedback value between 0 and 0.15 every 4 seconds
fd = Randi(min=0, max=0.15, freq=0.25)

# RandInt generates pseurorandom integer bw 0 and max
# values at a freq specified by freq parameter
# generates new lfo freq once per second
sp = RandInt(max=6, freq=1, add=8)

# create LFO oscillating between 0 and 0.4
amp = Sine(sp, mul=0.2, add=0.2)

# a simple synth...?
# a = SineLoop(freq=fr, feedback=fd, mul=amp).out()
a = SineLoop(freq=fr, feedback=0, mul=amp).out()

# display spectrum
sp = Spectrum(a)

# check out this cool gui
s.gui(locals())