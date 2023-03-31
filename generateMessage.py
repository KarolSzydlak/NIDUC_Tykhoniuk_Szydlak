import random

def generateMessage(i):
    message = ''
    while(i>0):
        x = random.randint(0, 1)
        x = str(x)
        message = message + x
        i-=1
    return message

generateMessage()