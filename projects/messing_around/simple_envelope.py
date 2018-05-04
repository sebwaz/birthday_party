"""
04-simple-envelopes.py - ASR and ADSR envelopes.

The Fader object is a simple way to setup an Attack/Sustain/Release envelope.
This envelope allows to apply fadein and fadeout on audio streams.

If the `dur` argument of the Fader object is set to 0 (the default), the
object waits for a stop() command before activating the release part of
the envelope. Otherwise, the sum of `fadein` and `fadeout` must be less
than or egal to `dur` and the envelope runs to the end on a play() command.

The Adsr object (Attack/Decay/Sustain/Release) acts exactly like the Fader
object, with a more flexible (and so common) kind of envelope.

"""
from pyo import *
import random
import time         # for pythons pause function

s = Server(duplex=0).boot()

# # Infinite sustain for the global envelope.
# # globalamp = Fader(fadein=2, fadeout=2, dur=0).play()
#
# # Envelope for discrete events, sharp attack, long release.
# env = Adsr(attack=0.01, decay=0.1, sustain=0.5, release=1.5, dur=2, mul=0.5)
# # setExp method can be used to create exponential or logarithmic envelope.
# env.setExp(0.75)
#
# # Initialize  a simple wave player and apply envelope
# # m = Metro( 0.125, poly=2 ).play()
# # te = TrigEnv(m, table=env, dur=0.25, mul=0.2)
# delays = [ 0.0, .5, 1.0 ]
# sig = SuperSaw(freq=[100,101], detune=0.6, bal=0.8, mul=env).out( delay = delays )
#
# # play envelope
# env.play()
#
#
# # Envelope for discrete events, sharp attack, long release.
# env2 = Adsr(attack=0.01, decay=0.1, sustain=0.5, release=1.5, dur=2, mul=0.5)
# # setExp method can be used to create exponential or logarithmic envelope.
# env2.setExp(0.75)

# Initialize  a simple wave player and apply envelope
# m = Metro( 0.125, poly=2 ).play()
# # te = TrigEnv(m, table=env, dur=0.25, mul=0.2)
# sig2 = SuperSaw(freq=[100,101], detune=0.6, bal=0.8, mul=env2).out( delay = 2.0 )
#
# # play envelope
# env2.play( delay = 2.0 )


# what the heck does this do?
# env = CosTable([(0,1),(300,1),(1000,-1),(8191,-1)])
env = SquareTable( order = 3 )
env.graph()
seq = Seq(time=.125, seq=[2,2,2,2], poly=1).play()
# tr = TrigRand(seq, min=250, max=500, port=.005)
freq = midiToHz( 70 )
amp = TrigEnv(seq, table=env, dur=.25, mul=.25)
a = SineLoop(freq, feedback=0.07, mul=amp).out()


# # play envelope
# sig.out()
# env.play()
# # play envelope
# env.play()
# # play envelope
# env.play()
# # play envelope
# env.play()
# # play envelope
# env.play()
#
# # pause for a bit
# time.sleep( 2.0 )
#
# # play envelope
# env.attack = 0.01
# env.play()
#
# def play_note():
#     "Play a new note with random frequency and jitterized envelope."
#     freq = random.choice(midiToHz([36, 38, 41, 43, 45]))
#     sig.freq = [freq, freq*1.005]
#     env.attack = random.uniform(0.002, 0.01)
#     env.decay = random.uniform(0.1, 0.5)
#     env.sustain = random.uniform(0.3, 0.6)
#     env.release = random.uniform(0.8, 1.4)
#     # Start the envelope for the event.
#     env.play()
#
# # Periodically call a function.
# pat = Pattern(play_note, time=0.25).play()

# play_note()

s.gui(locals())
