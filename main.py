import io
import time

import numpy as np
import pyaudio

from AudioCapture import AudioCapture
from OSCClient import OSCClient


class SendToWekinator:
    def __init__(self):
        self.client = OSCClient("localhost", 6448)
        self.audio_capture = AudioCapture(self.stream_callback)
        self.data = []

    def run(self):
        self.audio_capture.record(5)

    def stream_callback(self, in_data, frame_count, time_info, flag):
        audio_data = np.frombuffer(in_data, dtype=np.float32)
        float_data = list(map(lambda x: float(x), audio_data))
        float_data = float_data[:500]
        float_data = float_data[400:]
        # print(len(float_data))
        self.client.send_message(data=float_data)
        return audio_data, pyaudio.paContinue


def main():
    send_to_wekinator = SendToWekinator()
    send_to_wekinator.run()


if __name__ == '__main__':
    main()
