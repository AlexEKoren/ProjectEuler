#Finds the largest prime factor

import math
import time
def findFactors(n):
    x=[]
    #creates an array
    z=n
    x.append(z)
    x.append(1)
    #appends n and 1 to its factors
    y=z**.5+1
    #makes a variable that is one more than the square root of z
    p=2
    #starting value
    while p<y:
        #continues until p is equal or greater than y
        if z%p==0:
            #if y is a factor of z it adds it and its opposite to the array
            x.append(p)
            x.append(z/p)
        p=p+1
    x.sort()
    #sorts the array
    return x

def isPrime(n):
    if n<2:
        #checks if its less than 2
        return False
    if n==2:
        #2 is the first prime number
        return True    
    for x in range(3,int(n**0.5)+1,2):
        #checks if it has any factors beneath its square root plus 1
        if n%x==0:
            return False
    return True
    #returns true if all else is false.
    
def findLargestPrimeFactor(n):
    t1=time.time()
    array=findFactors(n)
    #sets an array of all the factors of number n
    i=len(array)-1
    #number to run through the array
    while i>0:
        if isPrime(array[i]):
             #if the number is prime in the end (no factors found)
             print array[i]
             print time.time()-t1
             return
        else:
            i=i-1
                
findLargestPrimeFactor(600851475143)
#findFactors(21)



    
        
