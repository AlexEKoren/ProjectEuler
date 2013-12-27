import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def isPower(x, y, z):
    if z%(x*y)==0:
        g=(x*y)
    elif z%x==0:
        g=x
    elif z%y==0:
        g=y
    else:
        return False
    t=z
    while z%g==0:
        z/=g
        if z==1:
            return True
    while z%x==0:
        z/=x
        if z==1:
            return True
    while z%y==0:
        z/=y
        if z==1:
            return True
    return False
    

def main(a):
    t=time.time()
    primes=Primes(a)
    #print primes
    x=1
    array=[]
    while x<a:
        while x<a and not primes[x]:
            x+=1
        y=x+1
        while y<a:
            while y<a and not primes[y]:
                y+=1
            if x*y>a:
                break
            g=a/(x*y)
            while isPower(x,y,g)==False and g>1:
                g-=1
            #print x, y, g,g*x*y
            array.append(g*x*y)
            y+=1
        x+=1
        
    print sum(list(set(array))), time.time()-t, max(array)
    #print array

main(10000000)
