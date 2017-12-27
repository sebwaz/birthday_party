# playing with a sine wave
# what effects can i add to a sine wave

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

serv 		= Server( duplex = 0 ).boot().start()
serv.amp 	= 0.707

# Envelope
A = 0.5
D = 0.1
S = 0.5
R = 0.1
env = Adsr(attack=A, decay=D, sustain=S, release=R, dur=A+D+R, mul=0.5)

# simple sine
# s = Sine( freq=my_note_dict['A3'], mul= 0.5 )
# s = Sine( freq=CMajor4, mul= 0.5 )
s = Sine( freq=CMajor4, mul= env )
s.out()
env.play()

# # simple flanger
# lf  = Sine(freq=.2, mul=.0045, add=.005)        # low freq osc.
# flg = Delay(s, delay=lf, feedback= 0.7).out()
#

# check out this cool gui
serv.gui(locals())