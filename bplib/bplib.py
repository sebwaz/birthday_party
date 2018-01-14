from pyo      import *
from warnings import *
from math     import floor
import soundfile as sf
import numpy     as np
import os
import wave
import struct

'''
helper function for sequencer()
'''
def make_trig_fn(sfplayer):
    def _function():
        sfplayer.out()
    return _function

'''
convert a 1-dimensional array to the seq format that sequencer expects
'''
def to_seq(vector):
    return np.array(vector).reshape(len(vector),1)

'''
if given uneven sequence lengths, assumes they start at the same time and sequence is as long as max
'''
def merge_seq(seq1, seq2):
    len_diff   = len(seq1)-len(seq2)
    add_to_seq = to_seq(np.zeros(abs(len_diff)))
    if len_diff > 0:
        seq2 = np.concatenate((seq2, add_to_seq))
    elif len_diff < 0:
        seq1 = np.concatenate((seq1, add_to_seq))
    return np.concatenate((seq1, seq2), axis=1)


'''
Takes a list SNDS of paths to sounds (0 should be empty str),
and a list PATTERN that is a sequence of integers.
Integers in PATTERN are interpreted as indices to SNDS,
and sequencer() plays SNDS according to PATTERN imposing uniform duration on each sound.

'''
# TODO: allow poly mode (current mode is mono only)
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

    b     = [] # a list of (lists containing each sounds trigger pattern)
    sfp   = [] # a list of sfplayers for each sound
    trigs = [] # a list of TrigFunc handles

    # loop to create each of the soundplayers
    for i in range(len(snds)):
        # if not 0 (0 interpreted as silence
        if i:
            # interpret sequence as individual trigger patterns
            seq = [int(i in x) for x in pattern]
            seq.insert(0, len(pattern))

            # setup individual trigger patterns
            b.append(Beat(time=beat_time, taps=16))
            b[i-1].setPresets([seq])
            b[i-1].recall(0)
            b[i-1].play()

            # setup sfplayers for each sound and run them
            sfp.append(SfPlayer(snds[i]))
            P = make_trig_fn(sfp[i-1])
            trigs.append(TrigFunc(b[i-1], P))

    s.gui(locals())
    return s

'''
Function to convert any audio file format to aiff, and use the '.aif' extension as used by PYO
The formats accepted by pysoundfile are listed here: http://www.mega-nerd.com/libsndfile/#Features
'''
def convert_to_aif(source_path, out_dir, fname=''):
    # get the file to be converted
    data, samplerate = sf.read(source_path)

    # use given filename, if specified
    if fname:
        sf.write(out_dir+fname+'.aiff', data, samplerate)

    # else, use original filename
    else:
        fname=os.path.basename(source_path)
        fname=os.path.splitext(fname)[0]
        sf.write(out_dir+fname+'.aiff', data, samplerate)

    # use the .aif extension that pyo recognizes
    base = os.path.splitext(out_dir+fname+'.aiff')[0]
    os.rename(out_dir+fname+'.aiff', base+'.aif')

'''
Read a .wav file as a stream(s) of values in the range [-1, 1]
'''
def read_wave(source_path, n_samples=None):
    # get file info
    wfile = wave.open(source_path, 'r')
    nchannels = wfile.getparams().nchannels # 1 for mono, 2 for stereo. MONO CASE NOT ADDRESSED
    sampwidth = wfile.getparams().sampwidth # number of bytes per sample
    framerate = wfile.getparams().framerate # number of samples per second
    nframes   = wfile.getparams().nframes   # number of samples in file (1 sample carries as many values as channels)

    # prep to parse file content
    if not n_samples or n_samples > nframes:
        n_samples = nframes
    typerange = 2 ** (8 * sampwidth)
    read_data = wfile.readframes(n_samples)

    # set byte format code (short by default)
    code='<H'
    if sampwidth==1:
        code='<B'
    elif sampwidth==4:
        code='<I'
    elif sampwidth==8:
        code='<Q'

    # if nchannels > 2, error
    if nchannels > 2:
        print('ERROR: input must be mono or stereo (n_channels = 1 or 2)')
        wfile.close()
        return

    elif nchannels == 2:
        # parse the read data
        y      = np.repeat(np.arange(n_samples), sampwidth) * (2 * sampwidth)
        l_i    = (y + np.tile(np.arange(sampwidth), n_samples)).reshape(n_samples, sampwidth)
        r_i    = (y + np.tile(np.arange(sampwidth, sampwidth * 2), n_samples)).reshape(n_samples, sampwidth)
        l_data = [struct.unpack(code, read_data[x[0]:x[-1] + 1])[0] for x in l_i]
        r_data = [struct.unpack(code, read_data[x[0]:x[-1] + 1])[0] for x in r_i]

        # convert to [-1, 1]
        l_norm = [x/((typerange/2)-1) if x<=((typerange/2)-1) else -((typerange-x)/(typerange/2)) for x in l_data]
        r_norm = [x/((typerange/2)-1) if x<=((typerange/2)-1) else -((typerange-x)/(typerange/2)) for x in r_data]
        wfile.close()
        return l_norm, r_norm, framerate

    else:
        # parse the read data
        data = [struct.unpack(code, read_data[sampwidth*x:sampwidth*x+sampwidth])[0] for x in range(n_samples)]

        # convert to [-1, 1]
        norm = [x/((typerange/2)-1) if x<=((typerange/2)-1) else -((typerange-x)/(typerange/2)) for x in data]
        wfile.close()
        return norm, None, framerate

'''
Take a list of values in the range [-1, 1] representing the normalized amplitude for a waveform and convert it into
a sound file with 16bit sample width. Automatically creates both .wav and .aif files
'''
def create_sample(fname, out_dir, channel1, channel2=None):
    # if 2 channels, make sure matched in length
    if channel2!=None and len(channel1)!=len(channel2):
        print('ERROR: the 2 audio channels must have the same length (unless channel2=None)')
        return

    # set up file info
    nchannels = 2 if channel2 else 1
    sampwidth = 2
    framerate = 44100
    nframes   = len(channel1)
    comptype  = 'NONE'
    compname  = 'not compressed'
    params    = (nchannels, sampwidth, framerate, nframes, comptype, compname)

    # convert from [-1, 1]
    typerange = 2 ** (8 * 2)
    l_short = [int(floor(((x / 2) + 1) * typerange)) if x < 0 else int(floor((x / 2) * (typerange - 1))) for x in channel1]
    r_short = [int(floor(((x / 2) + 1) * typerange)) if x < 0 else int(floor((x / 2) * (typerange - 1))) for x in channel2] if channel2 else []

    # put back into a single byte stream. if mono, r_short will be empty, so no problem
    merged = l_short + r_short
    if channel2:
        merged[::2]  = l_short
        merged[1::2] = r_short

    # convert the lest of sample values into bytes
    byte_stream = b''.join([struct.pack('<H', merged[i]) for i in range(len(merged))])

    # write the byte stream as a .wav file
    wav_path = out_dir+fname+'.wav'
    fwrite = wave.open(wav_path, 'w')
    fwrite.setparams(params)
    fwrite.writeframes(byte_stream)
    fwrite.close()

    # create corresponding .aif file
    convert_to_aif(wav_path, out_dir)

    return
