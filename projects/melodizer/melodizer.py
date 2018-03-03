import bplib as bp
import numpy as np
import os
from   math import floor

# convert guitar sounds
wav_path = './samples/wav/guitar/'
aif_path = './samples/aif/'
if not os.path.isfile('./samples/aif/0.aif'):
    for k in range(25):
        bp.convert_to_aif(wav_path+str(k)+'.wav', aif_path)

# convert drum sounds
if not os.path.isfile('./samples/aif/kick.aif'):
    bp.convert_to_aif('./samples/wav/kick.wav', aif_path)
if not os.path.isfile('./samples/aif/snare.aif'):
    bp.convert_to_aif('./samples/wav/snare.wav', aif_path)

# set tempo and create list of sounds
tempo       = 140
num_samples = 24
with_drums  = True
samp_align  = True
snds        = ['']

# put the sounds in the rack
for i in range(num_samples+1):
    snds.append(aif_path + str(i) + '.aif')

# add the drums to the sample list
snds.append(aif_path + 'kick.aif')
snds.append(aif_path + 'snare.aif')
s = len(snds)-1
k = len(snds)-2


#### CREATE SEQ ####
# pattern the drums
snares           = bp.to_seq(np.tile([0,0,0,0,s,0,0,0], 4))
kicks            = np.tile(np.random.randint(2, size=16)*(k), 2)
kicks[0]         = k
kicks[16]        = k
kicks            = bp.to_seq(kicks)
kicks[snares==s] = 0

# merge drums
drums = bp.merge_seq(kicks, snares)

# create sample seq
samps           = np.random.randint(num_samples+1, size=32)
zeros           = np.random.randint(2,             size=32)
samps           = bp.to_seq(np.multiply(samps, zeros)) # TODOD: make this an option
if samp_align:
    samps[kicks==k] = 1
samps[16:24]    = samps[0:8] # first quarter to sound like third quarter

# merge drums and samples
seq = bp.merge_seq(drums, samps)

# play sequence
bp.sequencer(snds, seq if with_drums else samps, tempo, 2)




