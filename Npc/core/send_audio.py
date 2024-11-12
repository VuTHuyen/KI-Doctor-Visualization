
from pythonosc import udp_client

from ..utils.audio2face_streaming.test_client import push_audio_track
from ._config import audio_server

client = udp_client.SimpleUDPClient('127.0.0.1', 5008)

# This function is used to send a audio array to your audio2face instance through audio_player_streaming of Audio2Face
def send_audio(wavarr, sample_rate):
    client.send_message("/FaceIdle", float(1))
    push_audio_track(audio_server,wavarr,sample_rate, '/World/audio2face/audio_player_streaming')
    client.send_message("/FaceIdle",float(0))
