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

"""
# Envelope for discrete events, sharp attack, long release.
env = Adsr(attack=0.01, decay=0.1, sustain=0.0, release=0.1, dur=1, mul=2)

# cmajorchord
a       = Sine( freq=CMajor4, mul = env )

# mix down
b = a.mix(2)

# chorus
c = Chorus(input=b, feedback=0.5)
c.out()

# add stereo reverb to signal
rev = Freeverb(c, size=1.0, damp=0.9, bal=0.3).out()
rev.ctrl()      # open controller window

# add another reverb
rev2 = Freeverb( rev, size=1.0, damp=0.9, bal=0.3)
rev2.out()
rev2.ctrl()

# # play supersaw
# a_ssaw  = SuperSaw( freq=CMajor4, detune=0.5, bal=0.7, mul=env, add=0)
# b_ssaw = a_ssaw.mix(1)
# # b_ssaw = b_ssaw.out()
# a_ssaw.ctrl()   # open controller window
# b_ssaw = Freeverb(b_ssaw, size=1.0, damp=0.9, bal=0.3).out()
# b_ssaw.ctrl()

def play_note():
    # Start the envelope for the event.
    env.play()

# Periodically call a function.
pat = Pattern(play_note, time=2).play()
"""

# reading samples
snd_path = '../../../../samples/OpenPathMusic44V1'
fpath = snd_path + "/drum-snare-tap.wav"
fpath = snd_path + "/drum-bass-lo-1.wav"


# stereo playback with a slight shift between the two channels.
sf = SfPlayer(fpath, speed=[1,1], loop=True, mul=1).out()

# check out this cool gui
s.gui(locals())

# s.stop()