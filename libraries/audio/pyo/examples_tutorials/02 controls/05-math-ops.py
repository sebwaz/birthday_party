# pyoobjects can be used inside arithmetic expressions

# multiplication, addition, division, subtraction

# returns dummy object htat outputs the result
# dummy is only placeholder to keep track of arithmetic operations

# can also be used with exponent, modulo, and negative

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from __future__ import print_function
from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

s = Server().boot().start()
s.amp = 0.1 # turn down 20dB

# create noise source?
n = Noise()

# full scale sine wave
a = Sine()

# create dummy object b with 'mul' attribute 0.5
# what does this mean?
# b = a * 0.5
# b.out()

# print(b)

# computes "ring" modulation between two pyoobjects
# and scales the amplitude of the result
c = Sine(freq=300)
d =  a* c * 0.3
d.out()

# pyo with exponent (does rectification?)
e = c ** 10 * 0.4
e.out(1)

# display ringmod and rectified signal
sp = Spectrum([d, e])
sc = Scope([d, e])

# check out this cool gui
s.gui(locals())

# s.stop()