from math import sqrt
import itertools
import time
def sumDigits(x):
    t=0
    while x>0:
        t+=(x%10)**2
        x/=10
    return t

def isSqr(x):
    return sqrt(x).is_integer()

def main(a):
    t=time.time()
    total=0
    for x in range(1, a):
        if isSqr(sumDigits(x)):
            total+=x
    print total, time.time()-t
main(1000000)
f = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]
def main2(a):
    t=time.time()
    nums=[1,2,3,4,5,6,7,8,9,0]
    squareSets=[]
    for z in range(1,a):
        for x in itertools.combinations_with_replacement(nums,z):
            if isSqr(sum(y**2 for y in x)):
                squareSets.append(x)
    print time.time()-t, len(squareSets)
    total=0
    working=[]
    for x in squareSets:
        for y in itertools.permutations(x):
            temp=0
            if y[0]!=0:
                for z in y:
                    temp*=10
                    temp+=z
            working.append(temp)
    working=set(working)
    total=sum(working)
    print total, time.time()-t
    

main2(7)
