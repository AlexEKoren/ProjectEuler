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

def factor(x):
    f=[[x]]
    for y in range(2, int(x**.5)+1):
        if x%y==0:
            f.append([y, x/y])
    print f
    '''for y in f:
        for z in y:
            if not isPrime(z):
                z=factor(z)'''
    return f

print factor(24)
