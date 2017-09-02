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

# drums
drums_path  = '../../../../samples/OpenPathMusic44V1'
d1          =  "/drum-snare-tap.wav"
d2          =  "/drum-bass-lo-1.wav"
drums       = [ drums_path+d1, drums_path+d2 ]

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

s 		= Server( duplex = 0 ).boot().start()
s.amp 	= 0.1

# stereo playback with a slight shift between the two channels.
# sf = SfPlayer(fpath, speed=[1,1], loop=True, mul=1)

# pick speed
bpm             = 80       # beats per minute
note            = 2         # note fraction
beat_time       = 1.0/( note*(bpm/60.0) )     # time b/w notes

# create a random beat, OR load the preset
b = Beat(time=beat_time, w1=[90,30,30,20], w2=[30,90,50,40], w3=[0,30,30,40])
b.play()

# tt = TrigFunc(b['end'][0], function=ch)

# load the samples into a sound table
tabs = SndTable(drums)

# create the trigger envelope which plays?
# out = TrigEnv(b, table=tabs, dur=b['dur']*2, interp=4, mul=b['amp']*0.5)
out = TrigEnv(b, table=tabs, dur=beat_time*note, interp=4, mul=b['amp']*0.5)
out.out()

# check out this cool gui
s.gui(locals())

# s.stop()