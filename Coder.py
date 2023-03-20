
def coder(message):
    divider = 2
    while(message%divider!=0):
        divider+=1
    message = format(message,'b')
    divider = format(divider,'b')
    print(message)
    message = message +" "
    message = message+divider
    print(message)
coder(8)