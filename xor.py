from shlex import join


def xor8(x,y):
    j = x
    x = x + '00000000'
    i = 0
    xlen = len(x)
    ylen = len(y)
    while(i<xlen-9):
        d = y
        a = 0
        while(a<i):
            d = '0'+d
            a += 1
        while(a<xlen-9):
            d = d + '0'
            a += 1
        b = 0
        lst_d = list(d)
        lst_x = list(x)
        n = ''
        m = ''
        # for elem in lst_x:
        #     n += elem
        # for elem in lst_d:
        #     m += elem
        # print("x: " + n)
        # print("y: " + m)
        while(b!=xlen):
            if(lst_x[i]==0):
                print("POMIJAM")
                break
            if((lst_x[b]=='0' and lst_d[b]=='1') or (lst_x[b]=='1' and lst_d=='0')):
                lst_x[b] = '1'
            else:
                lst_x[b] = '0'
            b += 1
        i +=1
    c = ''
    for elem in lst_x:
        c += elem
    c = int(c)
    c = str(c)
    c = j + c
    print(c)
    print(len(c))
    return c
x = 71
message = format(x,'b')
i = str(message)
while(i.__len__()<100):
    i = '0'+i
    #i = i+'00000000'
#print(len(i))
#print(i)
crc = 356
crc = format(crc,'b')
crc = str(crc)
c=xor8(i,crc)

