import bplib as bp
import numpy as np

example_number = int(input('Example to run: '))

#################################
if example_number == 1:
    '''
    1.) usage of bplib.sequencer
    '''
    # get sounds to play
    snds_path  = './samples/sebas/aif/'
    snds       = ['', snds_path+'e.aif', snds_path+'g#.aif', snds_path+'b.aif', snds_path+'a.aif', snds_path+'hat_charter.aif', snds_path+'bd_chicago.aif', snds_path+'Snaredrum.aif']

    # create sequence for guitar samples
    guitar     = bp.to_seq([1,2,1,2,1,2,3,1,2,1,2,1,2,3,4,2,4,2,4,2,3,4,2,4,2,4,2,3])

    # create a hat sequence
    hats       = bp.to_seq(np.tile([5,0], 14))

    # create rest of drum sequence
    kick_snare = bp.to_seq(np.tile([6,0,6,0,0,7,0], 4))

    # merge them
    seq = bp.merge_seq(guitar, hats)
    seq = bp.merge_seq(seq, kick_snare)

    # play
    bp.sequencer(snds, seq, 140, 2)


#################################
elif example_number == 2:
    '''
    2.) conversion of .wav file
    '''
    print('Converting to .aif...')
    bp.convert_to_aif('./samples/OpenPathMusic44V1/sleighbells.wav', './samples/output/', 'TEST')
    print('Done.')


#################################
elif example_number == 3:
    '''
    3.) reading a .wav file as a waveform with values in range [-1, 1] 
    '''
    # STEREO
    L, R, framerate = bp.read_wave('./samples/sebas/wav/once_we_were_fish.wav')
    reverse_L = np.flip(L,0).tolist() # logicals in bp.create_sample() will not evaluate correctly if passed np arrays
    reverse_R = np.flip(R,0).tolist() # thus, always use .tolist() after conducting transformations in numpy
    bp.create_sample('example3_stereo', './samples/output/', reverse_L, reverse_R)

    # MONO
    mono, empty, framerate = bp.read_wave('./samples/OpenPathMusic44V1/sleighbells.wav')
    reverse_mono = np.flip(mono, 0).tolist()
    bp.create_sample('example3_mono', './samples/output/', reverse_mono)

    # NOISE: WRITE WITHOUT READ
    noise_L = np.random.uniform(low=-1.0, high=1.0, size=44100*60).tolist()
    noise_R = np.random.uniform(low=-1.0, high=1.0, size=44100*60).tolist()
    bp.create_sample('example3_numpy_noise', './samples/output/', noise_L, noise_R)

    # RAMP: WRITE WITHOUT READ
    mono_ramp =  (((np.linspace(0.0, 1000.0, num=44100*30)**2)%2)-1).tolist()
    bp.create_sample('example3_numpy_ramp', './samples/output/', mono_ramp)