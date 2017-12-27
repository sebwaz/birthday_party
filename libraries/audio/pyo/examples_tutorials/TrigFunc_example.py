from pyo import *
s = Server().boot()
s.start()
f = Fader(fadein=.005, fadeout=.1, dur=.12, mul=.2)
a = SineLoop(midiToHz([60,60]), feedback=0.05, mul=f).out()
c = 0.0
def count():
    global c
    freq = midiToHz(round(c) + 60)
    a.freq = [freq, freq*0.995]
    c += 1.77
    if c > 13: c = 0
    f.play()
m = Metro(.125).play()
tf = TrigFunc(m, count)
