import io
import time

import numpy as np
import pyaudio

from AudioCapture import AudioCapture
from Fft import Fft
from OSCClient import OSCClient
import librosa
import soundfile as sf
import matplotlib.pyplot as plt


class SendToWekinator:
    def __init__(self):
        self.client = OSCClient("localhost", 6448)
        self.audio_capture = AudioCapture(self.stream_callback)
        self.data = []

    def run(self):
        self.audio_capture.record(5)

    def stream_callback(self, in_data, frame_count, time_info, flag):
        audio_data = np.frombuffer(in_data, dtype=np.float32)
        self.client.send_message(data=(float(max(audio_data)), float(min(audio_data))))
        return audio_data, pyaudio.paContinue


def main():
    send_to_wekinator = SendToWekinator()
    send_to_wekinator.run()


if __name__ == '__main__':
    main()
