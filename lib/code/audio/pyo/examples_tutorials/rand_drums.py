import bplib as bp
import numpy as np

'''
rand drum pattern
'''
snds_path = './pyo_examples/snds/'
snds      = ['', snds_path+'bd_chicago.aif', snds_path+'Snaredrum.aif', snds_path+'hat_charter.aif', snds_path+'TR-808Tom04.aif'] #, snds_path+'e.aif', snds_path+'g#.aif', snds_path+'b.aif', snds_path+'a.aif']
seq       = np.random.randint(0, len(snds), 14) #size=np.random.randint(12, 17))
bp.sequencer(snds, seq, 140, 2)
