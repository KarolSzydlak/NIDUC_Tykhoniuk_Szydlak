import random
from enum import Enum

class Channel_state(Enum):
    G = "good"
    B = "bad"
class Channel:
    state = Channel_state
    number = 0
    def __init__(self, state, number):
        self.state = state
        self.number = number
    def change_state(self):
        if(self.number<2):
            self.number = random.randint(0,10)
            if (self.number < 8):
                if (self.state == Channel_state.G.value):
                    self.state = Channel_state.B.value
                    return
                else:
                    self.state = Channel_state.G.value
                    return
        self.number = random.randint(0,10)
        if(self.number<2):
            if(self.state==Channel_state.G.value):
                self.state=Channel_state.B.value
            else:
                self.state=Channel_state.G.value