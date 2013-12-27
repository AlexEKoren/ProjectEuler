import time
from fractions import *
def isPrime(x):
    if x==1:
        return False
    if x==2:
        return True
    if x%2==0:
        return False
    for y in range(3,int(x**.5)+1,2):
        if x%y==0:
            return False
    return True

def A(k):
    s=1
    while s%k!=0:
        s*=10
        s+=1
    #print len(str(s))
    return len(str(s))

def main():
    t=time.time()
    count=0
    total=0
    x=91
    while count<25:
        if x%5!=0 and x%3!=0:
            #print A(x), x
            if not isPrime(x):
                if (x-1)%A(x)==0:
                    total+=x
                    print x
                    count+=1
        x+=2
    print time.time()-t
    print total

main()
