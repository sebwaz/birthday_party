#!/usr/bin/env python
# encoding: utf-8
"""
Returns a dictionary with standard piano notes

"""

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# # pyo
# from pyo import *

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

def note_dictionary( n_octs ):
    """
    Returns a dictionary with standard piano notes

    The returned dictionary has keys which are the names of the notes, i.e.:
        mydict          = note_dictionary( 8 )
        freq_C0         = mydict[ 'C0' ]
        freq_Csharp0    = mydict[ 'C#0' ]
    The key is of the form '<A-F><(optional for sharps)#><Octave #>'

    Calculates frequencies based on formula found here:
        https://en.wikipedia.org/wiki/Piano_key_frequencies

    Inputs:
        n_octs
            type: integer
            desc: # of octaves to return, starting from C0 (on a standard piano)

    Outputs:
        dictionary of notes and frequencies

    """

    print('helloooo')

    # number of octaves/notes to use
    n_octs  = 9
    n_notes = n_octs*12

    # list of frequencies on a standard 8 octave piano
    offset = -8     # 'C0' is located at index -8 for whatever reason
    freq_list = [ 440.0 * ( 2**( (n-49.0)/12.0 ) ) for n in range( offset, n_notes + 1 + offset) ]

    # list of note names
    note_names = [ 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B' ]

    # create note dictionary
    note_dict = { ( note_names[ n % 12 ] + str( n/12 ) ):freq_list[n] for n in range(0, n_notes) }

    return note_dict

# -----------------------------------------------------------------------------
# Main code
# -----------------------------------------------------------------------------

if __name__ == "__main__":

    # run function
    my_note_dict = note_dictionary( n_octs = 9 )

    # DEBUG
    for key in sorted( my_note_dict.iterkeys() ):
        print "%s: %s" % (key, my_note_dict[ key ])
    print('')
    # DEBUG
    for key, value in sorted( my_note_dict.iteritems(), key=lambda(k,v): (v,k) ):
        print "%s: %s" % (key, value)