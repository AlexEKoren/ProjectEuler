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

def nextPrime(n):
    x=n+1
    while isPrime(x)!=True:
        x+=1
    return x

def fibs(x):
    a=0
    b=1
    fib=[]
    y=0
    while y<100000000000031:
        if y<x:
            fib.append(a)
        temp=b
        b=a+b
        a=temp
        y+=1
    fib.append(b)
    return fib


def main(x):
    fib=fibs(nextPrime(x))
    print "fibs done"
    total=fib[-1]
    for y in range(2,x):
        total+=fib[nextPrime(y)]
    print total
main(100000)
