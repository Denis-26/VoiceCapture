from pythonosc import udp_client
import argparse


class OSCClient:
    def __init__(self, host, port):
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default=host, help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=port, help="The port the OSC server is listening on")
        args = parser.parse_args()
        self.client = udp_client.SimpleUDPClient(args.ip, args.port)

    def send_message(self, address="/wek/inputs", data=("test")):
        print(data)
        self.client.send_message(address, data)
