# learning how to use the beat object

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

# load sounds
snds = ['./snds/alum1.wav', './snds/alum2.wav',
        './snds/alum3.wav', './snds/alum4.wav']

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

# boot
s = Server(duplex=0).boot()

# what does this do?
t = CosTable( [ (0,0), (100,1), (500,0.3), (8191,0) ], size = 8192 )
# t = CosTable( [ (0,0), (8191,1) ], size = 8192 )
# t = CosTable( [ (0,0), (100,1), (500,0), (8191,1) ], size = 8192 )
# print(t)

# Pick beat trigger duration
# random generator
# tm = Xnoise(dist=9, freq=2.34, x1=.5, x2=10, mul=.0025, add=.12)
bpm = 70;       # beats per minute
tm  = 1.0/( 4*(bpm/60.0) )

# beat
# beat = Beat(time=.125, taps=16, w1=[90,80], w2=50, w3=35, poly=1).play()
beat = Beat(time=tm, taps=16, w1=[100], w2=100, w3=0, poly=1).play()

# trigger midi
# trmid = TrigXnoiseMidi(beat, dist=12, mrange=(60, 96))
trmid = TrigXnoiseMidi(beat, dist=12, mrange=(60, 72))

# trigger freq
# trhz = Snap(trmid, choice=[0,2,3,5,7,8,10], scale=1)
trhz = Snap(trmid, choice=[0,2], scale=1)

# trigger envelope
tr2 = TrigEnv(beat, table=t, dur=beat['dur'], mul=beat['amp'])

# make sound
a = Sine(freq=trhz, mul=tr2*0.3).out()
print(tr2.get())

# display spectrum
sp = Spectrum(a)

# check out this cool gui
s.gui(locals())