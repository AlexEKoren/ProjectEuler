from math import sqrt
from itertools import combinations, product
from time import time
def isPrime(x):
    if x<2:
        return False
    if x%2==0:
        return False
    for y in range(3,int(sqrt(x))+1,2):
        if x%y==0:
            return False
    return True



def S(n,d):
    found=False
    f=[]
    for M in range(n):
        for x in combinations(range(n),M):
            for y in product(range(10),repeat=M):
                s=""
                i=0
                for z in range(n):
                    if not z in x:
                        s+=str(d)
                    else:
                        s+=str(y[i])
                        i+=1
                if s[0]!="0":
                    if isPrime(int(s)):
                        found=True
                        f.append(int(s))
        if found==True:
            break
    return sum(f)

def main(d):
    t=time()
    total=0
    for x in range(10):
        total+=S(d,x)
    print total, time()-t
main(10)
