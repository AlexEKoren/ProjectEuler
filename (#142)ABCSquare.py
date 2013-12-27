from math import sqrt
import time
def isSqr(x):
    return sqrt(x).is_integer()

used=list([x] for x in range(10**6))
#used=[]
#cs=[]
def main():
    t=time.time()
    x=2
    while 1:
        for a in range(x**2/2+1,x**2/4*3):
            b=x**2-a
            if isSqr(a-b):
                used[a].append(b)
                if len(used[b])>1:
                    for c in used[b][1:]:
                        if isSqr(a-c):
                            if isSqr(a+c):
                                print a, b, c, a+b+c, time.time()-t
                                return
        x+=1
main()
