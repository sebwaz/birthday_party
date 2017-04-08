# learning how to use the beat object

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

# boot
s = Server().boot()

# what does this do?
t = CosTable([(0,0), (100,1), (500,0.3), (8191,0)])

# beat
beat = Beat(time=.125, taps=16, w1=[90,80], w2=50, w3=35, poly=1).play()

# trigger midi???
trmid = TrigXnoiseMidi(beat, dist=12, mrange=(60, 96))

# trigger freq??
trhz = Snap(trmid, choice=[0,2,3,5,7,8,10], scale=1)

# trigger envelope
tr2 = TrigEnv(beat, table=t, dur=beat['dur'], mul=beat['amp'])

# make sound
a = Sine(freq=trhz, mul=tr2*0.3).out()

# display spectrum
sp = Spectrum(a)

# check out this cool gui
s.gui(locals())