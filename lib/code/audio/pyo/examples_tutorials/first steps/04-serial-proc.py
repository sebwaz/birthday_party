# parallel audio effects
# each .out() plays the sine with an effect on top
# so 3 modded sines are playing

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

s = Server().boot()
s.start()
s.amp = 0.1 # turn down 20dB

# make a sine wave
a = Sine().out()

# pass sine wave thru harmonizer
h = Harmonizer(a).out()

# pass sine wave thru harmonizer
h = Harmonizer(h).out()

for ii in range(5):
	h = Harmonizer(h).out()

# check out this cool gui
s.gui(locals())

# s.stop()