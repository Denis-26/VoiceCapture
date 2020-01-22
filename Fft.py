from scipy.fftpack import fft, fftfreq
import scipy.io.wavfile as wav


class Fft:
    def __init__(self, file_name="file.wav"):
        self.file_name = file_name

    def extract(self):
        (rate, sig) = wav.read(self.file_name)
        samples = sig.shape[0]

        data_fft = fft(sig)
        return abs(data_fft), fftfreq(samples, 1 / rate), sig
