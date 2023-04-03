
def decoderCRC8(x,y):
    i = 0
    xlen = len(x)
    ylen = len(y)
    while (i < xlen - 9):
        d = y
        a = 0
        while (a < i):
            d = '0' + d
            a += 1
        while (a < xlen - 9):
            d = d + '0'
            a += 1
        b = 0
        lst_d = list(d)
        lst_x = list(x)
        n = ''
        m = ''
        for elem in lst_x:
            n += elem
        for elem in lst_d:
            m += elem
        print("x: " + n)
        print("y: " + m)
        while (b != xlen):
            if (lst_x[i] == 0):
                print("POMIJAM")
                break
            if ((lst_x[b] == '0' and lst_d[b] == '1') or (lst_x[b] == '1' and lst_d == '0')):
                lst_x[b] = '1'
            else:
                lst_x[b] = '0'
            b += 1
        i += 1
    c = ''
    for elem in lst_x:
        c += elem
    #c = int(c)
    c = str(c)
    print(c)
    print(len(c))
    return c
i = '000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100011111001000'
crc = 356
crc = format(crc,'b')
crc = str(crc)
decoderCRC8(i,crc)