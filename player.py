import math        #import needed modules
import pyaudio     #sudo apt-get install python-pyaudio
import wave

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
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(p.get_sample_size(p.get_format_from_width(1)))
    waveFile.setframerate(BITRATE)
    waveFile.writeframes(WAVEDATA.encode())
    waveFile.close()
