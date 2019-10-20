import math
import random
from player import play

def sine(FREQUENCY, LENGTH, BITRATE, AMP):
    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    WAVEDATA = ''
    for x in range(NUMBEROFFRAMES):
        WAVEDATA += chr(int(math.sin(2*x*FREQUENCY*math.pi/BITRATE)*AMP+64))
    print(WAVEDATA) # see the cyclic action
    #play(WAVEDATA, BITRATE)
    return WAVEDATA

def noise(LENGTH, BITRATE):
    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    WAVEDATA = ''
    for x in range(NUMBEROFFRAMES):
        WAVEDATA += chr(random.randint(0,127))
    print(WAVEDATA) # see chaos
    #play(WAVEDATA, BITRATE)
    return WAVEDATA

def rest(LENGTH, BITRATE):
    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    WAVEDATA = ''
    for x in range(NUMBEROFFRAMES):
        WAVEDATA += chr(64) # constant data for a constant silence
    print(WAVEDATA) # see uniformity
    #play(WAVEDATA, BITRATE)
    return WAVEDATA
