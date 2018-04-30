import bplib as bp
import numpy as np
import os
from   math import floor


def trip_seq():
    i   = np.random.choice(2, 3, p=[0.5, 0.5])
    ii  = np.random.choice(2, 3, p=[0.5, 0.5])
    seq = np.zeros(12)
    seq[0::4] = i
    seq[2::4] = ii
    return seq

def dup_seq():
    i   = np.random.choice(2, 2, p=[0.5, 0.5])
    ii  = np.random.choice(2, 2, p=[0.5, 0.5])
    seq = np.zeros(12)
    seq[0::6] = i
    seq[3::6] = ii
    return seq

# convert drums sounds
wav_path = './samples/wav/'
aif_path = './samples/aif/'
if not os.path.isfile('./samples/aif/kick.aif'):
    bp.convert_to_aif(wav_path+'kick.wav',  aif_path)
if not os.path.isfile('./samples/aif/snare.aif'):
    bp.convert_to_aif(wav_path+'snare.wav', aif_path)

# set tempo and create list of sounds
tempo       = 140
with_drums  = False
samp_align  = True
snds        = ['']
trips_1     = False
trips_2     = False
trips_3     = False
trips_4     = False

# pattern chords/samples
bar1  = dup_seq()*1
bar2  = dup_seq()*2
bar3  = bar1*3
bar4  = trip_seq()*4
samps = bp.to_seq(np.concatenate((bar1, bar2, bar3, bar4)))

# Create 4 random samples from source wav
L, R, framerate = bp.read_wave(wav_path+'sebtoss.wav')
sample_len      = int(floor(60*44100/(tempo*1.5)))
for i in range(1,5):
    # get random index for the new sample
    index = int(np.random.randint(0, len(L)-sample_len))

    # create the sample
    sample_L = np.array(L[index:index+sample_len]).tolist()  # logicals in bp.create_sample() will not evaluate correctly if passed np arrays
    sample_R = np.array(R[index:index+sample_len]).tolist()  # thus, always use .tolist() after conducting transformations in numpy
    bp.create_sample(str(i), aif_path, sample_L, sample_R)

    # add sample to the sound list
    snds.append(aif_path + str(i) + '.aif')

# add the drums to the sample list
snds.append(aif_path + 'kick.aif')
snds.append(aif_path + 'snare.aif')
k = len(snds)-2
s = len(snds)-1

# pattern the drums
snare    = np.zeros(12)
kick     = np.zeros(12)
snare[0] = s
kick[0]  = k
drums = bp.to_seq(np.concatenate((kick, snare, kick, snare)))

# merge drums
play = bp.merge_seq(drums, samps) if with_drums else samps

# play sequence
bp.sequencer(snds, play, tempo*3, 2)




