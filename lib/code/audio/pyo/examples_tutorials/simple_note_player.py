# simple note player using beat and trigger func

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

# my note dictionary function
from note_dictionary import *

#-----------------------------------------------------------#
# Main
#-----------------------------------------------------------#

# add paths to sounds
snds_path = './pyo_examples/snds/'
snds = {'kick':'bd_chicago.aif', 'snare':'Snaredrum.aif', 'hat':'hat_charter.aif', 'tom':'TR-808Tom04.aif' }

# start pyo
s = Server(duplex=0).boot()
s.start()

# set BPM
bpm       = 120
note      = 2
beat_time = 1.0/( note*(bpm/60.0))

# note dictionary
nd      = note_dictionary( n_octs = 9 )
notes   = [ nd['C3'], nd['C4'], nd['B3'], nd['F3'], nd['F3'], nd['F3'], nd['F3'], nd['G3'] ]

# start sequencer
# env = CosTable([(0,0),(900,1),(1000,.3),(8191,0)])
env = CosTable([(0,0), (500,1), (1000, 0.3), (1500, 1), (2000, 0.3), (8191,0)])
seq = Seq(time=beat_time, seq=[5,2,2,2,2,1,1,1], poly=1).play()
cnt = Counter( seq, min = 0, max = len(notes) )

# note streams
sels    = [Select(cnt, ii) for ii in range( 0, len(notes) )]
amps    = [TrigEnv(sels[ii], table=env, dur=1, mul=.25) for ii in range( 0, len(notes) )]
sines   = [SineLoop(notes[ii], feedback=0.07, mul=amps[ii]).out() for ii in range( 0, len(notes) )]

s.gui(locals())
