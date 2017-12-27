# parallel audio effects
# each .out() plays the sine with an effect on top
# so 3 modded sines are playing

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code?
#-----------------------------------------------------------#

s = Server().boot()
s.start()
s.amp = 0.1 # turn down 20dB

# make a sine wave
a = Sine()

# pass sine wave thru harmonizer
hr = Harmonizer(a).out()

# pass thru chorus
ch = Chorus(a).out()

# thro freq shift
sh = FreqShift(a).out()

# check out this cool gui
s.gui(locals())

# s.stop()