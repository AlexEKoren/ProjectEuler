def main():
    x=256
    count=0
    while len(hex(x))<7:
        h=hex(x)[2:]
        if "a" in h:
            if "0" in h:
                if "1" in h:
                    count+=1
                    print h, x
        x+=1
    print count
#main()

def main2():
    total=0
    for x in range(0,13):
        total+=
    print total
main2()
