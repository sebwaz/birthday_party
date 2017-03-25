# just foolin around testing things

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Defs
#-----------------------------------------------------------#

# frequency definitions
C3 = 130.81
E3 = 164.81
G3 = 196.00
C4 = C3*2.0
E4 = E3*2.0
G4 = G3*2.0

# chord definitions
CMajor3 = [C3, E3, G3]
CMajor4 = [C4, E4, G4]

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

s 		= Server().boot().start()
s.amp 	= 0.1

# cmajorchord
a = Sine( freq=CMajor4 )

# mix down
b = a.mix(1)

# chorus
c = Chorus(input=b, feedback=0.5)

# add stereo reverb to signal
rev = Freeverb(c, size=1.0, damp=0.9, bal=0.3).out()

# # create square
# a = Sine( freq=harms, mul=amps )
# print('Number of sine streams: %d' % len(a))

# # mix down
# b = Chorus(a.mix(2), feedback=0.5).out()
# print("Number of chorus streams: %d" %len(b))

# check out this cool gui
s.gui(locals())

# s.stop()