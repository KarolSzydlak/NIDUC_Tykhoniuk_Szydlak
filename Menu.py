
def menu():
    while True:
        print("Wybor rodzaju transmisji:\n 0)Wyjdz\n1)Stop And Wait ARQ\n2)GO And Back ARQ")
        x = input()
        x = int(x)
        match x:
            case 0:
                break
            case 1:
                #stop n wait
            case 2:
                # go n back

menu()