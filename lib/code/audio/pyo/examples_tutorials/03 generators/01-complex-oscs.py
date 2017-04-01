# Use the following four library objects to generate complex spectrums

# Blit: impulse train generator
# RCOsc: approx. of an RC series circuit (woah)
# SineLoop: Sine wave oscillator with feedback
# SuperSaw: Roland JP-8000 Supersaw emulator.

# Use the voice slider of the window input interpolator to
# interpolate between four waveforms. Each one has an LFO applied
# to the arg that changes the tone of the sound?


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

# band limited impulse train generator
# the lfo is applied tot he # of harmonics
lfo1 = Sine(0.1).range(1, 50)
osc1 = Blit(freq=freq0, harms = lfo1, mul = 0.3)

# RC circuit
lfo2 = Sine(freq = 0.1, mul = 0.5, add = 0.5)
osc2 = RCOsc( freq = freq0, sharp = lfo2, mul = 0.3 )

# Sine wave oscillator with feedback
lfo3 = Sine(0.1).range(0, 0.18)
osc3 = SineLoop( freq = freq0, feedback = lfo3, mul = 0.3)

# Roland jp8000 supersaw emu
lfo4 = Sine(0.1).range(0.1, 0.75)
osc4 = SuperSaw(freq = freq0, detune = lfo4, mul = 0.3)

# interpolates bw input objects to produce single output
sel = Selector([ osc1, osc2, osc3, osc4 ]).out()
# opens up controller gui
sel.ctrl(title = "input interpolator (0=Blit, 1 = RCOsc, 2=Sineloop, 3=SUperSaw)")

# display waveform
sc = Scope(sel)

# display spectrum
sp = Spectrum(sel)

# check out this cool gui
s.gui(locals())

# s.stop()