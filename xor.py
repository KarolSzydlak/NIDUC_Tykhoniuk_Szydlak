
def xor8(x,y):
    i=0
    c = x
    print(y)
    while(i<len(x)-9):
        a=0
        d =y
        print(c)
        while(a<i):
            d = '0'+d
            a+=1
        print(len(d))
        while(a<len(x)-9):
            d = d+'0'
            a+=1
        b = 0
        print("x:")
        print(x)
        print("y:")
        print(d)
        print("to d")
        while(b!=len(x)):
            if(c[b]==d[b]):
                c[b].replace(c[b],'0')
            else:
                c[b].replace(c[b], '1')
            b+=1
        i+=1
    print("hej")
    print(c)
    return c

x = 71
message = format(x,'b')
i = str(message)
while(i.__len__()<100):
        i = '0'+i
        #i = i+'00000000'
print(len(i))
print(i)
crc = 356
crc = format(crc,'b')
crc = str(crc)
i = i+'0000000'
xor8(i,crc)