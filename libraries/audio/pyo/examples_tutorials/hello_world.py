# First pyo program

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code?
#-----------------------------------------------------------#

s = Server().boot()
s.start()

# play a sound
# a = Sine(freq=440, phase=0, mul=0.1).out()

# two ways to change attributes
# a.setFreq(1000)		# using a setter
# a.freq = 1000 		# directly

# can mod stuff
mod = Sine( freq=600, mul=0.1 ).out()
# a = Sine( freq=mod + 440, mul=0.1 ).out()

# add envelope to a sine wave
f = Adsr( 	attack=0.01, 
			decay=0.2, 
			sustain=0.5, 
			release=0.1, 
			dur=5, 
			mul=0.5 )
# a = Sine(mul=f).out()
# f.play() 				# why do i have to call this?


# check out this cool gui
s.gui(locals())

# s.stop()