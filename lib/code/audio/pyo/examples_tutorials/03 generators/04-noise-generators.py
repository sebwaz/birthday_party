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
n1 = Noise(0.3)

# pink noise
n2 = PinkNoise(0.3)

# Brown noise 
n3 = BrownNoise(0.3)

# interpolate bw input objects to produce single output
sel = Selector( [n1, n2, n3] ).out()
sel.ctrl(title="Input interpolator (0=white, 1 = pink, 2=brown)")

# display spectrum
sp = Spectrum(sel)

# check out this cool gui
s.gui(locals())

# s.stop()