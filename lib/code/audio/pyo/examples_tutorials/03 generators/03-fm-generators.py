# FM modulation syntehsis!

# These 2 objects implement freq. modulation algorithms
# YOu can also build your own - seems like there's another tutorial for this


#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

# boot
s = Server().boot()

# FM implements basic Chowning alg
fm1 = FM( carrier = 250, ratio = [1.5, 1.49], index = 10, mul = 0.3)
fm1.ctrl()

# CrossFM implements fm synthesis where output of both oscs modulates
# the freq of the other one woah
fm2 = CrossFM(carrier=250, ratio=[1.5,1.49], ind1 = 10, ind2 = 2, mul=0.3)
fm2.ctrl()

# interpolates between input objects to produce single output
sel = Selector([fm1, fm2]).out()
sel.ctrl(title="Input interpolator (0 =FM, 1 = CrossFM")

# display spectrum
sp = Spectrum(sel)

# check out this cool gui
s.gui(locals())

# s.stop()