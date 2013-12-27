def isPrime(n):
    if n<2:
        #checks if its less than 2
        return False
    if n==2 or n==3:
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

def findFactors(n):
    x=[]
    #creates an array
    z=n
    #x.append(1)
    y=z**.5
    p=2
    #makes a variable that is one more than the square root of z
    while p<y:
        #continues until y is 1
        if z%p==0:
            #if y is a factor of z it adds it and its opposite to the array
            if isPrime(p):
                x.append(p)
            if z/p!=p and isPrime(z/p):
                x.append(z/p)
        p+=1
    #print x
    return x

def main():
    print isPrime(8)
    print findFactors(25)
    #array=[]
    #for i in range(5000000):
        #array.append(findFactors(i))
    #print "done"
    i=600
    while 1==1:
        sub1=0
        sub2=0
        sub3=0
        sub4=0
        if len(findFactors(i))==4:
            if len(findFactors(i+1))==4:
                if len(findFactors(i+2))==4:
                    if len(findFactors(i+3))==4:
                        print i
                        return
        i+=1
            
                        
main()
