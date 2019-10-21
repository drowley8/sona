import math        # do I even need this here?
import pyaudio     # sound wave maker (sort of) and player
import wave        # sound wave saver

p = pyaudio.PyAudio()   #initialize pyaudio

def play(WAVEDATA, BITRATE):
    stream = p.open(format = p.get_format_from_width(1),
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
    waveFile.setsampwidth(p.get_sample_size(p.get_format_from_width(1))) # Heck
    waveFile.setframerate(BITRATE)
    waveFile.writeframes(WAVEDATA.encode())
    waveFile.close()
