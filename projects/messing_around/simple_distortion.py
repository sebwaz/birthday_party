# simple distortion, with sliders for playing around with distortion in real time

# load dependencies
from pyo import *

# boot server
s = Server(duplex=0).boot()

# Infinite sustain for the global envelope.
globalamp = Fader(fadein=2, fadeout=2, dur=0).play()

# generate sine wave
a = Sine(freq=midiToHz( 60 ), mul=0.8)

# general drive value signal
drive_val = Sig( 0.75 )
drive_val.ctrl()                # start up slider

# generate slope value signal
slope_val = Sig( 0.5 )
slope_val.ctrl()

# apply distortion
# b = Disto( input=a, drive=drive_val, slope=slope_val, mul=0.5, add=0).out()

# apply clipping instead
b = Clip( input=a, min=-0.5, max=0.5, mul=globalamp*1, add=0).out()

# display scope
sc = Scope(b)

s.gui(locals())

