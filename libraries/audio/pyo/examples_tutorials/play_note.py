# play a solid note
# for tuning mah geetar

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
my_note_dict = note_dictionary( n_octs = 15 )

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

# pick note to play
note = 'E'

# start up server
serv 		= Server( duplex = 0 ).boot().start()

# simple tone with a few harmonics
fund_harm   = 4                    # fundamental harmonic to play
n_harms     = 10                     # number of harmonics to play
fund_note   = note + str(fund_harm)

# init the tone
decay_rate = 0.5;     # strength of decay
amp0    = 1.0
freqs   = [ my_note_dict[ fund_note ], my_note_dict[ fund_note ] ]
s       = Sine( freq = freqs, mul = amp0 ).out()
for ii in range(n_harms):
    cur_note    = note + str(fund_harm + ii + 1)
    freqs       = [my_note_dict[cur_note], my_note_dict[cur_note]]
    s           += Sine( freq = freqs, mul = amp0*( 10.0**( -decay_rate*ii ) ) ).out()

serv.gui(locals())