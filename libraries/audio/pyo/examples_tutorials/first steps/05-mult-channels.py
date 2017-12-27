# playing around with channels

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

# white noise
n = Noise()

# send bass to left (butterworth filter, lowpass)
lp = ButLP(n).out( chnl=0 )

# send treble to right (butterworth, highpass)
hp = ButHP(n).out( chnl=1 )



# check out this cool gui
s.gui(locals())

# s.stop()