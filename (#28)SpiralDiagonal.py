#Finds the sum of the diagonal in a spiral with x*x dimensions
import time
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

def main():
    increment=8
    total=13
    primes=8
    x=49
    while primes*10>=total:
        m=0
        while m<4:
            x+=increment
            if isPrime(x):
                primes+=1
            m+=1
            total+=1
        increment+=2
        #print primes,total, increment-1
    print increment-1
    
main()
