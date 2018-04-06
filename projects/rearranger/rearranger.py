import bplib as bp

L_pos_chunks, L_neg_chunks, R_pos_chunks, R_neg_chunks = bp.chunkify('./samples/wav/pigeon.wav')

# sort the chunks by length
L_pos_chunks.sort(key=sum, reverse=True)
L_neg_chunks.sort(key=sum)#, reverse=True)
R_pos_chunks.sort(key=sum, reverse=True)
R_neg_chunks.sort(key=sum)#, reverse=True)

bp.flatten_chunks('0', './samples/output/', L_pos_chunks, L_neg_chunks, R_pos_chunks, R_neg_chunks)

