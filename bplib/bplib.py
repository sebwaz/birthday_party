from pyo import *
from warnings import *

'''
helper function for sequencer()
'''
def make_trig_fn(sfplayer):
    def _function():
        sfplayer.out()
    return _function

'''
Takes a list SNDS of paths to sounds (0 should be empty str),
and a list PATTERN that is a sequence of integers.
Integers in PATTERN are interpreted as indices to SNDS,
and sequencer() plays SNDS according to PATTERN imposing uniform duration on each sound.

'''
def sequencer(snds, pattern, bpm=140, tpb=4):
    # check whether user entered a sound at 0 index. 0 reserved for silence
    if snds[0]:
        warn("0 index reserved for rest (silence). Sounds assigned to 0 will not be expressed.")

    # pyo inits
    s = Server(duplex=0).boot()
    s.start()

    # timing params
    beat_time = 1.0/(tpb*(bpm/60.0))
    window    = CosTable([(0,0), (0,1)])

    b       = [] # a list of (lists containing each sounds trigger pattern)
    players = [] # a list of sfplayers for each sound
    trigs   = [] # a list of TrigFunc handles
    for i in range(len(snds)):
        if i:
            # interpret sequence as individual trigger patterns
            seq = [int(x==i) for x in pattern]
            seq.insert(0, len(pattern))

            # setup individual trigger patterns
            b.append(Beat(time=beat_time, taps=16))
            b[i-1].setPresets([seq])
            b[i-1].recall(0)
            b[i-1].play()

            # setup sfplayers for each sound and run them
            players.append(SfPlayer(snds[i]))
            P = make_trig_fn(players[i-1])
            trigs.append(TrigFunc(b[i-1], P))

    s.gui(locals())
    return s
