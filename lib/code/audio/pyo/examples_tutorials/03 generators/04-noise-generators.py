# white noise, pink noise, and brown noise

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

# boot
s = Server().boot()

# white noise
n1 = Noise(0.3).out()

# display spectrum
sp = Spectrum(n1)

# check out this cool gui
s.gui(locals())

# s.stop()