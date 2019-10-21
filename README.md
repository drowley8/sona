# sona
Python-powered sound maker
## Prerequisites
To install the required Python packages, run
`pip install -r requirements.txt`
PyAudio requires the package portaudio19-dev in order to build. Install it with
`sudo apt install portaudio19-dev`

## Usage
`python3 gensound.py`

## gensoud.py
This is the main part of the program. Its contents can be safely changed to get desired output.

## player.py
This file uses PyAudio to play the audio output through the computer's default output device.
The file uses wave to save audio output to a wav file. By default, the output is saved to "file.wav"
### Usage
`player.play(WAVEDATA, BITRATE)`
Plays the byte data in WAVEDATA at rate BITRATE

`player.save(WAVEDATA, BITRATE, CHANNELS)`
Saves the byte data in WAVEDATA as a wav file. The file is saved at the rate BITRATE with CHANNELS.
CHANNELS is currently not working and should always be set to 1.

## waveforms.py
This file uses math to generate sound waves in the form of byte data.
### Usage
`waveforms.sine(FREQUENCY, LENGTH, BITRATE, AMP)`
Generates a sine wave at FREQUENCY hertz, LENGTH seconds, and AMP volume. BITRATE should match the BITRATE given to player.play() and player.save().
The range for FREQUENCY is 20-20000.
LENGTH is not limited by a range.
The range for AMP is 0-63. At this time, AMP should not exceed 64.

`waveforms.noise(LENGTH, BITRATE)`
Generates white noise for a length of LENGTH seconds. BITRATE should match the BITRATE given to player.play() and player.save().
LENGTH is not limited by a range.

`waveforms.rest(LENGTH, BITRATE)`
Generates a constant wave for a length of LENGTH seconds. BITRATE should match the BITRATE given to player.play() and player.save().
LENGTH is not limited by a range.

# Support
Like what you see? Download [Brave](https://brave.com/dro635) and click on the little orange triangle.
