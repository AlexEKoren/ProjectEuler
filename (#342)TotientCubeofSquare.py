import time
def findPrimeFactors(n):
    array=[]
    i=2
    while i<=n:
        if n%i==0:
            array.append(i)
            n/=i
        else:
            i+=1
    array=list(set(array))
    return array

def totient(n):
    array=findPrimeFactors(n)
    #print array
    r=n
    for x in array:
        r*=x-1
        r/=x
    return r

def main(n):
    t1=time.time()
    total=0
    for x in range(2,n):
        y=int(totient(x**2)**(1.0/3))
        while y**3<totient(x**2):
            y+=1
        if y**3==totient(x**2):
            total+=x
            #print y
            print x, x**2, total
    print time.time()-t1
#main(10**5)
#print findPrimeFactors(24)
print totient(10)
