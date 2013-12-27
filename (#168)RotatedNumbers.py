import time
def rotate(x):
    return int(str(x)[-1]+str(x)[0:-1])

def main():
    t=time.time()
    count=0
    for x in range(10, 100000000):
        r=rotate(x)
        if x<r:
            if r%x==0:
                print x
                count+=1
        elif x==r:
            print x
            count+=1
    print "count:", count
    print time.time()-t

def main2():
    count=52
    for x in range(7, 100):
        count+=9
    print count
main2()
