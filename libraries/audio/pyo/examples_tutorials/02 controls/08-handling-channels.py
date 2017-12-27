# cascading synths/filters can be cpu intensive if
# the synths are made of many streams

# so before filtering, mix shit down. that'll save
# number of streams and thus computational intensity

# this one re-uses the square wave example

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

s = Server().boot().start()

# set fundamental frequency and highest harmonic
freq = 100
high = 20

# generate list of odd harmonics
harms = [ freq * i for i in range(1, high) if i%2 ==1 ]
# generate list of harmonci amplitudes
amps = [ 0.33/i for i in range(1, high) if i%2 ==1 ]

# create square
a = Sine( freq=harms, mul=amps )
print('Number of sine streams: %d' % len(a))

# mix down
b = Chorus(a.mix(2), feedback=0.5).out()
print("Number of chorus streams: %d" %len(b))

# check out this cool gui
s.gui(locals())

# s.stop()