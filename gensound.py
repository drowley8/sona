import waveforms


#See https://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 384000 # on a scale of 8000-384000
AMP = 63 # on a scale of 0-64
FREQUENCY = 440 # human hearing is between 20-20000hz

WAVEDATA = ''
waveforms.noise(2, BITRATE)
waveforms.sine(262, 1, BITRATE, 63)
waveforms.sine(294, 1, BITRATE, 63)
waveforms.sine(330, 1, BITRATE, 63)
waveforms.sine(349, 1, BITRATE, 63)
waveforms.sine(392, 2, BITRATE, 63)

#for x in range(NUMBEROFFRAMES):
#    WAVEDATA += chr(random.randint(32,96))
