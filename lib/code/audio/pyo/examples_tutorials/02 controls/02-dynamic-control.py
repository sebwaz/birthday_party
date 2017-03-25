# dynamic parameter tweaking with controller window

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

s = Server().boot()
s.start()
s.amp = 0.1 # turn down 20dB

# make 2 fm signals
a = FM().out()
b = FM().out( chnl=1 )

# open controller windows
a.ctrl(title="freq mod left channel")


# check out this cool gui
s.gui(locals())

# s.stop()