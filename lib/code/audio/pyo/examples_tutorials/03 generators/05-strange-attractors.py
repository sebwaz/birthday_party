# strange attractor = system of 3 nonlinear ODEs woah
# they exhibit chaotic dyanmics/fractal properties

# three strange attractors built into the library - Rossler, Lorenz, ChenLee

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

# boot
s = Server().boot()

# LFO applied to chaos attribute
lfo = Sine(freq=0.2).range(0,1)

# Rossler
n1 = Rossler( pitch=0.5, chaos=lfo, stereo=True)

# Lorenz
n2 = Lorenz(pitch=0.5, chaos = lfo, stereo=True)

# ChenLee
n3 = ChenLee(pitch=0.5, chaos=lfo, stereo=True)

# interpolate bw input objects to produce single output
sel = Selector( [n1, n2, n3] )
sel.ctrl(title="Input interpolator (0=Rossler, 1=Lorenz, 2=ChenLee)")

# display spectrum
sp = Spectrum(sel)

# Audio?
# lorenz with very low pitch value that acts as a LFO
freq = Lorenz(0.005, chaos=0.7, stereo=True, mul=250, add = 500)
a = Sine(freq, mul=0.3).out()

# check out this cool gui
s.gui(locals())