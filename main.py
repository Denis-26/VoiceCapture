import pyaudio
import wave
from python_speech_features import mfcc
from python_speech_features import logfbank
from python_speech_features import fbank
import scipy.io.wavfile as wav

CHUNK = 1024
WIDTH = 2
CHANNELS = 1
RATE = 44100
FORMAT = pyaudio.paInt16
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("* recording")
# start Recording
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    print(data)
    frames.append(data)

print("finished recording")

# stop Recording
stream.stop_stream()
stream.close()
p.terminate()

waveFile = wave.open("file.wav", 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(p.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

(rate, sig) = wav.read("file.wav")
mfcc_feat = mfcc(sig, rate)
fbank_feat = fbank(sig, rate)

print(fbank_feat[0][:10])

