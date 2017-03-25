# can use lists of different lengths
# the longer list will set # of streams
# the smaller list will wrap around to fill the length

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

s = Server().boot().start()

# 12 streams diff combinations of stuff
# check out the paper where the guy talks about this
a = SumOsc( freq=[100, 150.2, 200.5, 250.7],
			ratio = [0.501, 0.753, 1.255], 
			index = [0.3, 0.4, 0.5, 0.6, 0.7, 0.4, 0.5, 0.3, 0.6, 0.7, 0.3, 0.5],
			mul = 0.05)

# add stereo reverb to signal
rev = Freeverb(a.mix(1), size=0.80, damp=0.7, bal=0.3).out()


# check out this cool gui
s.gui(locals())

# s.stop()