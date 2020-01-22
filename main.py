import numpy as np
from AudioCapture import AudioCapture
from Fft import Fft
from OSCClient import OSCClient


def main():
    audio_capture = AudioCapture()
    fft = Fft()
    audio_capture.record(1)
    audio_capture.save_audio()
    audio_capture.clear()

    (fft_abs, freq_s) = fft.extract()
    # fft_abs = list(set(np.round(fft_abs, 0)))
    # freq_s = list(set(np.round(freq_s, 0)))

    client = OSCClient("localhost", 6448)
    for (k, v) in zip(fft_abs, freq_s):
        client.send_message(data=(k, v))


if __name__ == '__main__':
    main()
