import pyaudio
import waveforms
from player import play, save

#See https://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 44100 # on a scale of 8000-384000
                # "Normal" would be 44100
AMP = 63 # on a scale of 0-64. Currently does nothing. Do not exceed 63
FREQUENCY = 440 # human hearing is between 20-20000hz, so...

# We're running at 60 BPM!

WAVEDATA = '' # initialize the WAVEDATA!
              # I hoped that would have sounded cooler, but it didn't
WAVEDATA += waveforms.noise(.5, BITRATE)
WAVEDATA += waveforms.rest(.25, BITRATE)
WAVEDATA += waveforms.sine(698, .25, BITRATE, 63)
WAVEDATA += waveforms.sine(880, .25, BITRATE, 63)
WAVEDATA += waveforms.sine(988, .5, BITRATE, 63)
WAVEDATA += waveforms.sine(698, .25, BITRATE, 63)
WAVEDATA += waveforms.sine(880, .25, BITRATE, 63)
WAVEDATA += waveforms.sine(988, .5, BITRATE, 63)
WAVEDATA += waveforms.sine(698, .25, BITRATE, 63)
WAVEDATA += waveforms.sine(880, .25, BITRATE, 63)
WAVEDATA += waveforms.sine(988, .25, BITRATE, 63)
WAVEDATA += waveforms.sine(1318.5, .25, BITRATE, 63)
WAVEDATA += waveforms.sine(1175, .5, BITRATE, 63)
WAVEDATA += waveforms.sine(988, .25, BITRATE, 63)
WAVEDATA += waveforms.sine(1046.5, .25, BITRATE, 63)
WAVEDATA += waveforms.sine(988, .25, BITRATE, 63)
WAVEDATA += waveforms.sine(784, .25, BITRATE, 63)
WAVEDATA += waveforms.sine(659, 1, BITRATE, 63)
WAVEDATA += waveforms.rest(.25, BITRATE)
WAVEDATA += waveforms.noise(.5, BITRATE)
play(WAVEDATA, BITRATE) # Drop needle here
save(WAVEDATA, BITRATE, 1) # Extra channels = extra speed. For now.

#for x in range(NUMBEROFFRAMES):
#    WAVEDATA += chr(random.randint(32,96))
# experimental white AMP stuff
