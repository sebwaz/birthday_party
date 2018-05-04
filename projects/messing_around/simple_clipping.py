# simple clipping type distortion

# load dependencies
from pyo import *

# boot server
s = Server(duplex=0).boot()

# Infinite sustain for the global envelope.
globalamp = Fader(fadein=2, fadeout=2, dur=0).play()

# generate sine wave
a = Sine(freq = midiToHz( 70 ), mul=0.8)

# clipping sliders
min_clip = Sig( 0 )
min_clip.ctrl( title='Minimum clipping threshold' )                # start up slider
max_clip = Sig( 1.0 )
max_clip.ctrl( title='Maximum clipping threshold' )                # start up slider

# apply clipping
b = Clip( input=a, min= -1 * min_clip, max=max_clip, mul=1, add=0).out()

# display scope
sc = Scope(b)

# display spectrum

s.gui(locals())

