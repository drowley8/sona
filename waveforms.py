import math
import random
from player import play

def sine(FREQUENCY, LENGTH, BITRATE, AMP):
    NUMBEROFFRAMES = int(BITRATE * LENGTH)

    WAVEDATA = ''

    for x in range(NUMBEROFFRAMES):
        WAVEDATA += chr(int(math.sin(2*x*FREQUENCY*math.pi/BITRATE)*AMP+64))

    play(WAVEDATA, BITRATE)

def noise(LENGTH, BITRATE):
    NUMBEROFFRAMES = int(BITRATE * LENGTH)

    WAVEDATA = ''
    for x in range(NUMBEROFFRAMES):
        WAVEDATA += chr(random.randint(0,127))

    play(WAVEDATA, BITRATE)
