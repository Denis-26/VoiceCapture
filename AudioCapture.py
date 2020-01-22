import pyaudio
import wave


class AudioCapture:
    def __init__(self, chunk=1024, width=2, channels=1, rate=44100, pa_format=pyaudio.paInt16):
        self.chunk = chunk
        self.width = width
        self.channels = channels
        self.rate = rate
        self.pa_format = pa_format
        self.frames = []
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=self.audio.get_format_from_width(width),
            channels=channels,
            rate=rate,
            input=True,
            output=True,
            frames_per_buffer=chunk)

    def record(self, secs):
        print("* START recording {} secs".format(secs))
        for i in range(0, int(self.rate / self.chunk * secs)):
            data = self.stream.read(self.chunk)
            self.frames.append(data)
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        print("* STOP recording")

    def save_audio(self, file_name="file.wav"):
        wave_file = wave.open(file_name, 'wb')
        wave_file.setnchannels(self.channels)
        wave_file.setsampwidth(self.audio.get_sample_size(self.pa_format))
        wave_file.setframerate(self.rate)
        wave_file.writeframes(b''.join(self.frames))
        wave_file.close()

    def clear(self):
        self.frames = []
