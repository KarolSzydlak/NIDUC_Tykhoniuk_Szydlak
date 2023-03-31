import xor
def goBackStart():
    x = 71
    message = format(x,'b')
    i = str(message)
    while(i.__len__()<100):
        i = '0'+i
    #i = i+'00000000'
    crc = 358
    crc = format(crc,'b')
    a = b =0
    i = int(i)
    c = xor.xor8(i,crc)
    print(c)
goBackStart()