from fractions import *
import time
def main(a):
    t=time.time()
    total=a**2*3
    for x in range(1,a+1):
        for y in range(1,x+1):
            if x==y:
                total+=min(x,(a-x))*2
            else:
                g=gcd(x,y)
                my=y/g
                mx=x/g
                total+=min(y/mx,(a-x)/my)*2
                total+=min(x/my,(a-y)/mx)*2
    print total, time.time()-t
main(1000)
