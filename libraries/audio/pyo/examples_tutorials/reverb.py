#!/usr/bin/env python
# encoding: utf-8
"""
Simple reverb function

C:\Users\bzhang\git\birthday_party\lib\code\audio\pyo\examples_tutorials\reverb.py

Requires:
    pyo
    numpy (possibly)
"""

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# pyo
from pyo import *

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

def reverb( in_stream, delay_list, fb_list ):
    """
    Pass in the delays and the feedback amounts you want, and return heaaaavvyyy
    reverbbbbbb

    Inputs:

        in_stream:
            type: pyo object
            desc: the audio signal to apply reverb to

        delay_list:
            type: list of delays, scalar if mono, doublets if stereo
            desc: the # of delays to apply, each being an individual delay with
                units of seconds. Entries of list are either scalars for mono reverb
                or 1x2 lists (i.e. [ [0.5, 0.5] ] ) if stereo

    Outputs:

        out_stream:
            type: pyo object
            desc: the outputted audio signal
    """

    # create a list of delay streams
    out_stream_list = [ Delay(in_stream, delay=d, feedback=fb) \
                        for (d, fb) in zip(delay_list, fb_list) ]

    b1 = Allpass(in_stream, delay=[.0204,.02011], feedback=0.25)
    b2 = Allpass(b1, delay=[.06653,.06641], feedback=0.31)
    b3 = Allpass(b2, delay=[.035007,.03504], feedback=0.4)
    b4 = Allpass(b3, delay=[.023021 ,.022987], feedback=0.55)

    c1 = Tone(b1, 5000, mul=0.2).out()
    c2 = Tone(b2, 3000, mul=0.2).out()
    c3 = Tone(b3, 1500, mul=0.2).out()
    c4 = Tone(b4, 500, mul=0.2).out()

    # send multiplexed signal as output
    # out_stream = sum(out_stream_list)
    # return out_stream

# -----------------------------------------------------------------------------
# Main code
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # start up pyo
    s = Server(duplex=0).boot()

    # sound file to load
    sfile = './pyo_examples/snds/b.aif'

    # start a stream
    a = SfPlayer(sfile, loop=True, mul=0.3).mix(2).out()
    # a = SfPlayer( sfile, loop = True, mul = 0.3 )

    # list of delays
    BPM         = 200.0
    delaytime   = 60.0/BPM
    del1 = [ delaytime * ii for ii in range( 1, 10 ) ]
    del2 = del1
    delays = [ [d1, d2] for (d1, d2) in zip(del1, del2) ]
    # delays  = [ [ 0.05, 0.05 ], [ 0.07, 0.07 ] ]
    fbs     = [ (0.5-ii*0.05) for ii in range( 1, 10 ) ]

    # DEBUG
    print(del1)
    print(fbs)

    # pass stream to reverb
    # b = reverb(a, delays, fbs)
    # b.out()
    delay_time = 0.05
    # b1 = Allpass(a, delay=[delay_time, delay_time], feedback=0.5).out()
    # b2 = Allpass(b1, delay=[delay_time, delay_time], feedback=0.4).out()
    # b3 = Allpass(b2, delay=[delay_time, delay_time], feedback=0.3).out()
    # b4 = Allpass(b3, delay=[delay_time, delay_time], feedback=0.2).out()

    # c1 = Tone(b1, 5000, mul=0.2).out()
    # c2 = Tone(b2, 5000, mul=0.2).out()
    # c3 = Tone(b3, 5000, mul=0.2).out()
    # c4 = Tone(b4, 5000, mul=0.2).out()

    # combsum = a + comb1 + comb2 + comb3 + comb4
    #
    # all1 = Allpass(combsum, delay=[.005,.00507], feedback=0.75)
    # all2 = Allpass(all1, delay=[.0117,.0123], feedback=0.61)
    # lowp = Tone(all1, freq=3500, mul=.2).out()
    # spec = Spectrum(a, size=1024)

    s.gui(locals())
