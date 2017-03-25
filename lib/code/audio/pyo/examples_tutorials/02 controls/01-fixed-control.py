# making a triangle wave?

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

s = Server().boot()
s.start()
s.amp = 0.1 # turn down 20dB

# "fundamental" frequency
freq = 200

# approx triangle waveform
# by adding amplitudes prop to inverse square of freq?
# i.e. sinc^2?
h1 = Sine(freq = freq, mul = 1).out()
h2 = Sine(freq = freq*3, phase = 0.5, mul = 1./pow(3,2)).out()
h3 = Sine(freq=freq*5, mul=1./pow(5,2)).out()
h4 = Sine(freq=freq*7, phase=0.5, mul=1./pow(7,2)).out()
h5 = Sine(freq=freq*9, mul=1./pow(9,2)).out()
h6 = Sine(freq=freq*11, phase=0.5, mul=1./pow(11,2)).out()

# Displays the final waveform
# only works if WxPython is installed... which only works for python 2
sp = Scope(h1+h2+h3+h4+h5+h6)

# check out this cool gui
s.gui(locals())

# s.stop()