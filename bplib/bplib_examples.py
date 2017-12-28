import bplib as bp

example_number = int(input('Example to run: '))

if example_number == 1:
    '''
    1.) usage of bplib.sequencer
    '''
    snds_path = './samples/sebas/aif/'
    snds      = ['', snds_path+'e.aif', snds_path+'g#.aif', snds_path+'b.aif', snds_path+'a.aif']
    seq       = [1,2,1,2,1,2,3,1,2,1,2,1,2,3,4,2,4,2,4,2,3,4,2,4,2,4,2,3]
    bp.sequencer(snds, seq, 140, 2)

elif example_number == 2:
    '''
    2.) conversion of .wav file
    '''
    print('Converting to .aif...')
    bp.convert_to_aif('./samples/OpenPathMusic44V1/sleighbells.wav', './samples/output/', 'TEST')
    print('Done.')