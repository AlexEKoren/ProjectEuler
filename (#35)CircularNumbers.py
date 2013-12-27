#Finds all circular primes under x
import copy
def forwardsArray(n):
    #creates an array of the number by inserting each digit
    f=[]
    a=n
    while(a!=0):
        f.insert(0,a%10)
        a=a/10
    return f

def arrayToNumber(n):
    k=0
    number=0
    while k<len(n):
        number=number+(n[k]*10**(len(n)-k-1))
        k=k+1
    return number

def isPrime(n):
    if n < 2:
        #checks if its less than 2
        return False
    if n == 2:
        #2 is the first prime number
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def rotate(n):
    a=n
    a.insert(0,a[len(a)-1])
    a.pop()
    return a

def main(x):
    final=0
    i=2
    while i<x:
        while i<12:
            if isPrime(i):
                final=final+1
                #print i
            i=i+1
        origArray=forwardsArray(i)
        if isPrime(arrayToNumber(origArray)):
            array=copy.copy(origArray)
            rotate(array)
            while(array!=origArray):
                if isPrime(arrayToNumber(array)):
                    #print origArray
                    rotate(array)
                    if array==origArray:
                        final=final+1
                else:
                    break
        i=i+1
    print final

main(1000000)
