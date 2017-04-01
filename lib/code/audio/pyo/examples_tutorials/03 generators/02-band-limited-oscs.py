# Now using LFO object, pick and choose what shape of waveform you want


#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

# boot 
s = Server().boot()

# fundamental freq
freq0 = 200

# this lfo will be applied to the "sharp" attribute
lfo = Sine(freq = 0.2, mul = 0.5, add = 0.5)

# Various band limited waveforms
osc = LFO(freq = freq0, sharp = lfo, mul=0.4).out()
osc.ctrl()

# display waveform
sc = Scope(osc)

# display spectrum
sp = Spectrum(osc)

# check out this cool gui
s.gui(locals())

# s.stop()