import math        #import needed modules
import pyaudio     #sudo apt-get install python-pyaudio
import random

PyAudio = pyaudio.PyAudio     #initialize pyaudio

#See https://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 8000
FREQUENCY1 = 440
FREQUENCY2 = 880
LENGTH = 4
AMP = 63 # on a scale of 0-64

NUMBEROFFRAMES = int(BITRATE * LENGTH)

WAVEDATA = ''

for x in range(NUMBEROFFRAMES):
    WAVEDATA += chr(int(math.sin(2*x*FREQUENCY1*math.pi/BITRATE)*AMP+64))
    #WAVEDATA += chr(int(math.sin(2*x*FREQUENCY2*math.pi/BITRATE)*AMP+64))

#for x in range(NUMBEROFFRAMES):
#    WAVEDATA += chr(random.randint(0,127))
#for x in range(NUMBEROFFRAMES):
#    WAVEDATA += chr(random.randint(32,96))

print(WAVEDATA)

p = PyAudio()
stream = p.open(format = p.get_format_from_width(1),
                channels = 1,
                rate = BITRATE,
                output = True)

stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()
