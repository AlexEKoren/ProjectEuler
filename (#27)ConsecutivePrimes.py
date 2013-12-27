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
    a=-999
    b=-999
    final=0
    finalA=a
    finalB=b
    while a<1000:
        while b<1000:
            n=0
            while isPrime(n**2+n*a+b):
                n+=1
            if n>final:
                final=n
                print final
                finalA=a
                finalB=b
            b+=2
        b=-999
        a+=1
    print time.time()-t
    print finalA, finalB
    print finalA*finalB
t=time.time()
print isPrime(99999989)
print time.time()-t
#main()
