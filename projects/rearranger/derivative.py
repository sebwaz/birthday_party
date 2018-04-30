import bplib as bp
import numpy as np
from scipy import signal
from time import gmtime, strftime

wav_path = './samples/wav/'

L, R,   framerate = bp.read_wave(wav_path+'daviddockery.wav')
kL, kR, kframerate = bp.read_wave(wav_path+'kicklong.wav')
L = np.array(L)
R = np.array(R)
#sample_L = np.diff(L, 2)
#sample_R = np.diff(R, 2)
sample_L = signal.convolve(np.diff(R, 1), kR)
sample_R = signal.convolve(np.diff(L, 1), kL)

sample_L = (sample_L/max(abs(sample_L))).tolist()
sample_R = (sample_R/max(abs(sample_R))).tolist()


print(max(sample_L), max(sample_R), min(sample_L), min(sample_R))
timestamp = strftime("%Y-%m-%d %H%M%S", gmtime())
bp.create_sample(timestamp, './samples/output/', sample_L, sample_R)