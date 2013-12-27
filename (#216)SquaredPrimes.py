def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for x in range(3,int(n**0.5)+1,2):
        if n%x==0:
            return False
    return True

def t(n):
    if isPrime(2*n**2-1):
        return True
    return False

def main(a):
    count=0
    for x in range(2,a):
        if t(x):
            #print x, 2*x**2-1
            count+=1
        else:
            print x
    print count

main(100)
    
