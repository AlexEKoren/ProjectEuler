import itertools
import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def isPrime(n):
    if n<2:
        #checks if its less than 2
        return False
    if n==2:
        #2 is the first prime number
        return True
    if n%2==0:
        return False
    for x in range(3,int(n**0.5)+1,2):
        #checks if it has any factors beneath its square root plus 1
        if n%x==0:
            return False
    return True
    #returns true if all else is false.

def tS(x):
    s=""
    for y in x:
        s+=y
    return s

def removeNums(x, l):
    for y in list(str(x)):
        if y not in l:
            return [],False
        else:
            l.remove(y)
    return l, True

def main():
    primes=Primes(10**7)
    print "primes done"
    for x in primes:
        cont=False
        nums=range(10)
        temp=removeNums(x,nums)
        if temp[1]==True:
            nums=temp[0]
        for y in primes:
            if 
main()
