# FUNCTION TO GET LSL STREAM

# CODE AUTHORED BY: SHAWHIN TALEBI
# THE UNIVERSITY OF TEXAS AT DALLAS
# MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

# import pylsl modules
from pylsl import StreamInlet, resolve_stream

# define function
# inputs: none
# outputs: pylsl data inlet
def getStream(streamNumber):
    # first resolve an EEG stream on the lab network
    print("looking for an EEG stream...")
    streams = resolve_stream()

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[streamNumber])

    return inlet
