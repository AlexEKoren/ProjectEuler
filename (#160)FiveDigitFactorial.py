import time
def main(x):
    t=time.time()
    f=1
    for y in range(1,10):
        f*=y
    y=11
    while y<x+1:
        f*=y
        temp=str(f)
        for z in reversed(temp):
            if z=="0":
                temp=temp[:-1]
            if z!="0":
                break
        f=int(temp[-6:])
        y+=1
    print time.time()-t
    print str(f)[-5:]
main(10000000)
