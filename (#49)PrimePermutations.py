import itertools
import math
def Primes(y):
    primes=[]
    primes.append(2)
    i=3
    while i<y:
        isprime=True
        for x in range(2, int(i**.5 + 1)):
            if i%x==0: 
                isprime=False
                break
        if isprime:
            primes.append(i)
        i=i+1
    return primes

def Primes2(y):
    primes=[]
    i=1000
    while i<y:
        isprime=True
        for x in range(2, int(i**.5 + 1)):
            if i%x==0: 
                isprime=False
                break
        if isprime:
            primes.append(i)
        i=i+1
    return primes

def findPermutations(y):
    return list(itertools.permutations([int(str(y)[0]), int(str(y)[1]), int(str(y)[2]), int(str(y)[3])]))
    
def main():
    fullprimes=Primes(10000)
    primes=Primes2(10000)
    for x in primes:
        counter=0
        temp=[x]
        perms=findPermutations(x)
        for p in perms:
            if len(str(p))>4:
                perms.append(int(str(p)[1])*1000+int(str(p)[4])*100+int(str(p)[7])*10+int(str(p)[10]))
                perms.remove(p)
        for y in perms:
            if primes.__contains__(y) and not temp.__contains__(y):
                counter=counter+1
                temp.append(y)
        if counter>=2 and abs(temp[1]-temp[2])==abs(temp[0]-temp[1]):
            print temp
            print x
#findPermutations(1234)
print len(Primes(2000000))
#main()
