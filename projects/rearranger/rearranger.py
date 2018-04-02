import bplib as bp
import numpy as np

# STEREO
L, R, framerate = bp.read_wave('./samples/wav/stays.wav')

# lists to hold the chunks from each channel
L_pos_chunks = []
L_neg_chunks = []
R_pos_chunks = []
R_neg_chunks = []

# for each channel
for k in range(2):
    channel = np.asarray(L) if k==0 else np.asarray(R)
    pos = channel.copy()
    neg = channel.copy()
    pos[pos < 0] = 0
    neg[neg > 0] = 0
    pos_chunks = np.empty(shape=(0, 0))
    neg_chunks = np.empty(shape=(0, 0))

    # for both positive- and negative-passed copies
    for h in range(2):
        chunks  = []
        buf     = []
        write   = False
        samples = pos if h==0 else neg

        # create the chunk list
        for t in samples:
            if write:
                if t==0:
                    write = False
                    buf.append(0)
                    chunks.append(buf)
                    buf = []
                else:
                    buf.append(t)
            elif t!=0 and write==False:
                write = True
                buf.append(t)

        # save out copies of the chunk list
        if h==0:
            pos_chunks = np.asarray(chunks.copy())
            #allpos = [smp for chnk in pos_chunks for smp in chnk]
        elif h==1:
            neg_chunks = np.asarray(chunks.copy())
            #allneg = [smp for chnk in neg_chunks for smp in chnk]

    # save out the master copies of the chunk lists
    if k==0:
        L_pos_chunks = pos_chunks.copy()
        L_neg_chunks = neg_chunks.copy()
    elif k==1:
        R_pos_chunks = pos_chunks.copy()
        R_neg_chunks = neg_chunks.copy()

# crop the chunk lists so that they are all the same size
chunk_counts = [L_pos_chunks.size, L_neg_chunks.size, R_pos_chunks.size, R_neg_chunks.size]
crop = min(chunk_counts)
L_pos_chunks = L_pos_chunks[0:crop]
L_neg_chunks = L_neg_chunks[0:crop]
R_pos_chunks = R_pos_chunks[0:crop]
R_neg_chunks = R_neg_chunks[0:crop]

# convert to standard py lists so that we can use py in-built sort function
L_pos_chunks = L_pos_chunks.tolist()
L_neg_chunks = L_neg_chunks.tolist()
R_pos_chunks = R_pos_chunks.tolist()
R_neg_chunks = R_neg_chunks.tolist()

# sort the chunks by length
#L_pos_chunks.sort(key=sum, reverse=True)
#L_neg_chunks.sort(key=sum)#, reverse=True)
#R_pos_chunks.sort(key=sum, reverse=True)
#R_neg_chunks.sort(key=sum)#, reverse=True)

# create the rearranged sequences
L_c = [None]*(len(L_pos_chunks) + len(L_neg_chunks))
R_c = [None]*(len(R_pos_chunks) + len(R_neg_chunks))

# TODO: create two functions; one that outputs L/R_neg/pos_chunks, and one that takes L_c, R_c (below as arguments)

# in this case, do not rearrange the chunks, just put them back together in alternating pos-neg order
L_c[0::2] = L_pos_chunks
L_c[1::2] = L_neg_chunks
R_c[0::2] = R_pos_chunks
R_c[1::2] = R_neg_chunks
#L_c = L_c.tolist()
#R_c = R_c.tolist()

# flatten L_c and R_c
reL = [item for sublist in L_c for item in sublist]
reR = [item for sublist in R_c for item in sublist]

# crop reL and reR so that they are the same length
re_lens = [len(reL), len(reR)]
crop = min(re_lens)
reL = reL[0:crop]
reR = reR[0:crop]

bp.create_sample('0', './samples/output/', reL, reR)

