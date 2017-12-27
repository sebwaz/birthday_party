# i want to apply two filters to the same signal
# one after the other
# and see whether the filters cascade, add, or replace each
# other

# trying a pitch shift? (not found in doc as filter)

# according to the doc they seem to cascade
# http://ajaxsoundstudio.com/pyodoc/examples/06-filters/02-bandpass-filters.html

#-----------------------------------------------------------#
# Imports
#-----------------------------------------------------------#

from pyo import *

#-----------------------------------------------------------#
# Code
#-----------------------------------------------------------#

s = Server().boot().start()
# s.amp = 0.1 # turn down 20dB



# check out this cool gui
s.gui(locals())

# s.stop()