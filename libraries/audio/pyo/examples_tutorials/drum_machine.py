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

# beat presets
presets = [ [8, 1, 0, 0, 0, 0, 0, 0, 0],
            [8, 1, 0, 0, 0, 0, 0, 0, 0] ]

#-----------------------------------------------------------#
# Functions
#-----------------------------------------------------------#

# Function to choose a new sound and a new speed for the right player
def play_drums( sf ):
    sf.out()

#-----------------------------------------------------------#
# Main script
#-----------------------------------------------------------#

s 		= Server( duplex = 0 ).boot().start()
s.amp 	= 1.0

# pick speed
bpm             = 60.0        # beats per minute
note            = 1.0         # note fraction
beat_time       = 1.0/( note*(bpm/60.0) )     # time b/w notes

# create a random beat, OR load the preset
b = Beat(time=beat_time, w1=[90,30], w2=[30,90], w3=[0,30])
b.setPresets(presets)
b.recall(0)     # what does this do?
b.play()

# tt = TrigFunc(b['end'][0], function=ch)

# load the samples into a sound table
tabs = SndTable(drums)

# create the trigger envelope which plays?
# out = TrigEnv(b, table=tabs, dur=b['dur']*2, interp=4, mul=b['amp']*0.5)
out = TrigEnv(b, table=tabs, dur=tabs.getDur(all=True), interp=1, mul=b['amp']*0.5)
out.out()

s.gui(locals())

# # ---------------------------------------------------------------------------------------
# # ALTERNATIVE IMPLEMENTATION
# # Instead of using a sound table + trig env, load sounds into sf player and run trig func
#
# # SF player with stereo playback
# sf0 = SfPlayer(drums[0], loop=False, mul=0.4)
# sf1 = SfPlayer(drums[0], loop=False, mul=0.4)
#
# # The "end-of-file" signal triggers the function "newR"
# tf0 = TrigFunc( b[0], play_drums, sf0 )
#
# # check out this cool gui
# s.gui(locals())
#
# # s.stop()

