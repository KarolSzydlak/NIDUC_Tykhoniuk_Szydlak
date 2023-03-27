import socket

import channel_state
from channel_state import *
class Sender:
    channel = Channel(state=Channel_state.G.value, number=3)
    print(channel.state)
    channel.change_state()
    print(channel.state)
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 9090

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((HOST,PORT))

    socket.send("hi".encode('ascii'))

