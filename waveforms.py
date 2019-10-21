import math
import random
from player import play

# TODO: add a wave mixer to mix two waves together. e.g. A chord.
# TODO: add a triangle wave. Sines sound too ringtone-y

def sine(FREQUENCY, LENGTH, BITRATE, AMP):
    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    WAVEDATA = ''
    for x in range(NUMBEROFFRAMES):
        WAVEDATA += chr(int(math.sin(2*x*FREQUENCY*math.pi/BITRATE)*AMP+128))
        # Complex math stuff goes on here
    print(WAVEDATA) # see the cyclic action
    #play(WAVEDATA, BITRATE)
    return WAVEDATA

def noise(LENGTH, BITRATE):
    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    WAVEDATA = ''
    for x in range(NUMBEROFFRAMES):
        WAVEDATA += chr(random.randint(64,192))
    print(WAVEDATA) # see chaos
    #play(WAVEDATA, BITRATE)
    return WAVEDATA

def rest(LENGTH, BITRATE):
    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    WAVEDATA = ''
    for x in range(NUMBEROFFRAMES):
        WAVEDATA += chr(128) # constant data for a constant silence
    print(WAVEDATA) # see uniformity
    #play(WAVEDATA, BITRATE)
    return WAVEDATA
