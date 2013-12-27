import time

def Primes(start, y):
    primes=[]
    i=start
    while i<y:
        isprime=True
        for x in range(start, int(i**.5 + 1)):
            if i%x==0: 
                isprime=False
                break
        if isprime:
            primes.append(i)
        i=i+1
    return primes

def main(z):
    t=time.time()
    array=[0,1]
    primes=[1,2]
    x=100000
    while x<z:
        primes=(Primes(428570*x/1000000,428572*x/1000000))
        y=0
        while y<len(primes):
            #print y
            n=primes[y]
            #print str(float(n)/x)+":"+str(n)+"/"+str(x)
            if (str(float(n)/x)+":"+str(n)+"/"+str(x))<(str(float(3)/7)+":"+str(3)+"/"+str(7)):
                array.append(str(float(n)/x)+":"+str(n)+"/"+str(x))
                array.sort()
                array.remove(array[0])
            y=y+1
        x=x+1
    array.append(str(float(3)/7)+":"+str(3)+"/"+str(7))
    array.sort()
    p=1
    a=array.index(str(float(3)/7)+":"+str(3)+"/"+str(7))
    '''while str(array[a-p])[0:15]==str(array[a])[0:15]:
        p+=1'''
    t2=time.time()
    print len(array)
    print t2-t
    print array[a]
    print array[a-1]
            
main(1000000)
