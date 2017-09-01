# just foolin around testing things

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

# my note dictionary function
from note_dictionary import *

#-----------------------------------------------------------#
# Defs
#-----------------------------------------------------------#

# grab note dictionary
my_note_dict = note_dictionary( n_octs = 9 )

# frequency definitions
# C3 = 130.81
# E3 = 164.81
# G3 = 196.00
# C4 = C3*2.0
# E4 = E3*2.0
# G4 = G3*2.0
C3 = my_note_dict[ 'C3' ]
E3 = my_note_dict[ 'E3' ]
G3 = my_note_dict[ 'G3' ]
C4 = my_note_dict[ 'C4' ]
E4 = my_note_dict[ 'E4' ]
G4 = my_note_dict[ 'G4' ]
B3 = my_note_dict[ 'B3' ]

# chord definitions
CMajor3 = [C3, E3, G3]
CMajor4 = [C4, E4, G4]
Cdrop3  = [C3, E3, G3, B3]

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

s 		= Server( duplex = 0 ).boot().start()
s.amp 	= 0.1

# cmajorchord
a = Sine( freq=Cdrop3 )

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