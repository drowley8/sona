import pyaudio
import waveforms
from player import play, save

#See https://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 44100 # on a scale of 8000-384000
                # "Normal" would be 44100
AMP = 63 # on a scale of 0-64
FREQUENCY = 440 # human hearing is between 20-20000hz

# We're running at 60 BPM!

WAVEDATA = ''
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
play(WAVEDATA, BITRATE)
save(WAVEDATA, BITRATE, 1)

#for x in range(NUMBEROFFRAMES):
#    WAVEDATA += chr(random.randint(32,96))
