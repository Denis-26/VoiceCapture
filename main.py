import numpy as np
from AudioCapture import AudioCapture
from Fft import Fft
from OSCClient import OSCClient
import matplotlib.pyplot as plt
from time import sleep


def main():
    audio_capture = AudioCapture()
    fft = Fft()
    audio_capture.record(2)
    audio_capture.save_audio()
    audio_capture.clear()

    (fft_abs, freq_s, sig) = fft.extract()

    cut_sig = list(filter(lambda x: x > 1000 or x < -1000, sig[20000:]))

    plt.plot(cut_sig)
    plt.show()

    client = OSCClient("localhost", 6448)
    for (k, v) in enumerate(cut_sig):
        client.send_message(data=(k, float(v)))


if __name__ == '__main__':
    main()
