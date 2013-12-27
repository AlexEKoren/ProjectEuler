import itertools
import time
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


def main():
    t=time.time()
    pandigitalList=[]
    pandigitalList=itertools.permutations([1,2,3,4,5,6,7])
    pandigitals=[]
    for l in pandigitalList:
        pandigitals.append(int(str(l)[1]+str(l)[4]+str(l)[7]+str(l)[10]+str(l)[13]+str(l)[16]+str(l)[19]))
    pandigitals.reverse()
    for x in pandigitals:
        if isPrime(x):
            t2=time.time()
            print t2-t
            print x
            return
    
isPrime(7654312)  
main()
