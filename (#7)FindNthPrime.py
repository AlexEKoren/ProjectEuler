#Finds the nth prime

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

def main(n):
    x=0
    #which number prime we're at
    i=2
    #which number is being checked for primeness
    while x<n:
        #while we haven't gotten to the nth prime we want
        if isPrime(i):
            #if it is prime add one to which prime we are at
            x=x+1
            if x==n:
                i=i-1
                #negates the i having one added at the end
        i=i+1
        #moves i up one more number
    print i
print isPrime(6791)
main(10001)


