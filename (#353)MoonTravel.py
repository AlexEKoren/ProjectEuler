from math import *
def drange(start, stop, step):
     r = start
     while r < stop:
             yield r
             r += step

def main(x):
    total=0
    for r in range(1,16):
        m=1
        f=0
        for d in drange(.1, r, .1):
            #print d
            if int(r/d)==r/d:
                #print "yes"
                if r/d*((d)**2)<m:
                    print r/d*((d)**2)
                    m=d*((d*pi*r/pi*r)**2)
                    f=d
        print r, m
main(5)
