from pyo import *

snds_path = './pyo_examples/snds/'
snds = {'kick':'bd_chicago.aif', 'snare':'Snaredrum.aif', 'hat':'hat_charter.aif', 'tom':'TR-808Tom04.aif' }

s = Server(duplex=0).boot()
s.start()

bpm       = 140
note      = 4
beat_time = 1.0/( note*(bpm/60.0))
window    = CosTable([(0,0), (0,1)])

K_preset = [16, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0 ,0, 0, 0]
S_preset = [16, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
H_preset = [16, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1]

K_beat = Beat(time=beat_time, taps=16)
S_beat = Beat(time=beat_time, taps=16)
H_beat = Beat(time=beat_time, taps=16)

K_beat.setPresets([K_preset])
S_beat.setPresets([S_preset])
H_beat.setPresets([H_preset])

K_beat.recall(0)
S_beat.recall(0)
H_beat.recall(0)

K_beat.play()
S_beat.play()
H_beat.play()

K_sf = SfPlayer(snds_path+snds['kick'])
S_sf = SfPlayer(snds_path+snds['snare'])
H_sf = SfPlayer(snds_path+snds['hat'])

def K(): K_sf.out()
def S(): S_sf.out()
def H(): H_sf.out()

K_tr = TrigFunc(K_beat, K)
S_tr = TrigFunc(S_beat, S)
H_tr = TrigFunc(H_beat, H)

s.gui(locals())
