import bplib.bplib as bp
from time import gmtime, strftime

L_pos_chunks, L_neg_chunks, R_pos_chunks, R_neg_chunks = bp.chunkify('./samples/wav/AMP_BUZZ_SAW.wav')

# sort the chunks by length
# L_pos_chunks.sort(key=len)#, reverse=True)
# L_neg_chunks.sort(key=len)#, reverse=True)
# R_pos_chunks.sort(key=len)#, reverse=True)
# R_neg_chunks.sort(key=len)#, reverse=True)
L_pos_chunks.sort(key=sum, reverse=True)
L_neg_chunks.sort(key=sum)#, reverse=True)
R_pos_chunks.sort(key=sum, reverse=True)
R_neg_chunks.sort(key=sum)#, reverse=True)

# offset = 2
# Lp = []
# Ln = []
# Rp = []
# Rn = []
# for k in range(1, 1+offset):
#     if k % 2 == 0:
#         Lp.extend(L_pos_chunks[k::offset])
#         Ln.extend(L_neg_chunks[k::offset])
#         Rp.extend(R_pos_chunks[k::offset])
#         Rn.extend(R_neg_chunks[k::offset])
#     else:
#         Lp.extend(reversed(L_pos_chunks[k::offset]))
#         Ln.extend(reversed(L_neg_chunks[k::offset]))
#         Rp.extend(reversed(R_pos_chunks[k::offset]))
#         Rn.extend(reversed(R_neg_chunks[k::offset]))



timestamp = strftime("%Y-%m-%d %H%M%S", gmtime())
bp.flatten_chunks(timestamp, './samples/output/', L_pos_chunks, L_neg_chunks, R_pos_chunks, R_neg_chunks)
# bp.flatten_chunks(timestamp, './samples/output/', Lp, Ln, Rp, Rn)
