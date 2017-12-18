import bplib as bp

snds_path = './pyo_examples/snds/'
snds      = ['', snds_path+'e.aif', snds_path+'g#.aif', snds_path+'b.aif', snds_path+'a.aif']
seq       = [1,2,1,2,1,2,3,1,2,1,2,1,2,3,4,2,4,2,4,2,3,4,2,4,2,4,2,3]

bp.sequencer(snds, seq, 140, 2)

