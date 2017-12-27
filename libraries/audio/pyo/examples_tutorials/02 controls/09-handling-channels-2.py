# changing which channel stuff comes out of

# chnl = # fo channels
# inc = increment channel #

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

# boot with 8 channels
s = Server(nchnls=6).boot()

# generate sine wave
a = Sine(freq = 500, mul=0.3)

# mix it up to four streams
# oh so you can up-mix
b = a.mix(4)

# output to channels 0 2 4 and 6
# whats the point fo this lol
b.out(chnl=0, inc=2)

# check out this cool gui
s.gui(locals())

# s.stop()