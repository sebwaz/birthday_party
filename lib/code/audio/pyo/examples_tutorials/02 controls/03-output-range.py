# the mul and add attributes
# default range of audio signal is -1 to 1
# add and mul change that range

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

s = Server().boot().start()
# s.amp = 0.1 # turn down 20dB

# mul multiples range
a = Sine(freq=100, mul=0.1).out()

# add adds offset to range
# multiplication happens first
b = Sine(freq=100, mul=0.5, add =0.5).out()

# using range(min, max) allows one to compute both mul
# and add
c = Sine(freq=100).range(-0.25,0.5).out()

# scope
sc = Scope([a, b, c])

# check out this cool gui
s.gui(locals())

# s.stop()