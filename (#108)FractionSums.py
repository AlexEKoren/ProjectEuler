import time
from fractions import *
def main(a):
    x=4
    i=1
    m=0
    first=0
    second=0
    while 1:
        count=0
        #array=[]
        for y in range(2*x,x**2+2*x,x):
            num=y/x
            num-=1
            if y%num==0:
                count+=1
                #array.append(y)
        if count>=m:
            first=second
            second=x
            m=count
            i=second-first
        if count>a:
            print x
            return
        print x,count, i#, array
        x+=i
main(1000)
