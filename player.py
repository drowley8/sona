import math        # do I even need this here?
import pyaudio     # sound wave maker (sort of) and player
import wave        # sound wave saver

p = pyaudio.PyAudio()   #initialize pyaudio
FORMAT = p.get_format_from_width(1, unsigned=True)
#p.get_sample_size(p.get_format_from_width(1))

def play(WAVEDATA, BITRATE):
    stream = p.open(format = FORMAT,
                    channels = 1,
                    rate = BITRATE,
                    output = True)
    stream.write(WAVEDATA)
    stream.stop_stream()
    stream.close()
    p.terminate()

def save(WAVEDATA, BITRATE, CHANNELS):
    waveFile = wave.open("file.wav", 'wb')
    waveFile.setnchannels(CHANNELS) # Yes, but actually no.
    waveFile.setsampwidth(p.get_sample_size(FORMAT))
    waveFile.setframerate(BITRATE)
    waveFile.writeframes(WAVEDATA.encode())
    waveFile.close()
