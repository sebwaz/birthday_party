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
bpm             = 130       # beats per minute
note            = 4
beat_time       = 1.0/( note*(bpm/60.0) )     # time b/w notes
print(beat_time)

# beat
# beat = Beat(time=.125, taps=16, w1=[90,80], w2=50, w3=35, poly=1).play()
preset = [16, 0, 1, 1, 1,
          0, 1, 1, 1,
          0, 1, 1, 1,
          0, 1, 1, 1 ]
beat = Beat(time=beat_time, taps=16, w1=[0], w2=50, w3=50, poly=1)
# beat.setPresets( preset )       # load a preset
# beat.recall(1)                  # set beat = loaded preset 0
beat.play()                     # start the beat stream
print('starting beat')


# trigger midi
# trmid = TrigXnoiseMidi(beat, dist=12, mrange=(60, 96))
trmid = TrigXnoiseMidi(beat, dist=12, mrange=(60, 72))

# trigger freq
# trhz = Snap(trmid, choice=[0,2,3,5,7,8,10], scale=1)
trhz = Snap(trmid, choice=[0,2], scale=1)

# trigger envelope
tr2 = TrigEnv(beat, table=t, dur=beat['dur'], mul=beat['amp'])

# make sound
# a = Sine(freq=trhz, mul=tr2*0.3).out()
# release = Adsr( attack=0, decay=0, sustain=.5, release=2, dur=0, mul=.5 )
# release.play()
# release.stop()
fader = Fader( fadein=0.0, fadeout=0.5, dur = 0.4, mul = 0.5)
a = Sine(freq=260, mul=fader )
fader.play()
a.out()
# release.play()
# release.stop()
# release.play()
# release.stop()

# display spectrum
# sp = Spectrum(a)

# check out this cool gui
s.gui(locals())