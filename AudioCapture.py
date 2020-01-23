import time
from time import sleep

import numpy as np
import pyaudio
import wave


class AudioCapture:
    def __init__(self, stream_callback, chunk=1024, width=2, channels=1, rate=44100, pa_format=pyaudio.paFloat32):
        self.chunk = chunk
        self.width = width
        self.channels = channels
        self.rate = rate
        self.pa_format = pa_format
        self.frames = []
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=pa_format,
            channels=channels,
            rate=rate,
            input=True,
            output=True,
            stream_callback=stream_callback)

    def record(self, secs):
        print("* START recording {} secs".format(secs))
        self.__run_loop(secs)
        self.audio.terminate()
        print("* STOP recording")

    def __run_loop(self, secs):
        self.stream.start_stream()
        while self.stream.is_active():
            command = input("Write stop to stop: ")
            if command == "stop":
                self.stream.stop_stream()
        self.stream.close()

    def __get_stream_data(self):
        data = self.stream.read(self.chunk)
        return data, np.fromstring(data, dtype=np.float32)

    def save_audio(self, file_name="file.wav"):
        wave_file = wave.open(file_name, 'wb')
        wave_file.setnchannels(self.channels)
        wave_file.setsampwidth(self.audio.get_sample_size(self.pa_format))
        wave_file.setframerate(self.rate)
        wave_file.writeframes(b''.join(self.frames))
        wave_file.close()

    def clear(self):
        self.frames = []
