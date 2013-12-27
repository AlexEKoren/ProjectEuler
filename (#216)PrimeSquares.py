def isPrime(x):
    if x%2==0:
        return False
    if (x-1)%6==0 or (x+1)%6==0:
        for y in range(3,int(x**.5)+1,2):
            if x%y==0:
                return False
    return True

def main(a):
    count=0
    for x in range(2,a+1):
        if isPrime(2*x**2-1):
            count+=1
        #else:
            #print x
    print count

main(10000)
