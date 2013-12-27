import time
def Primes(x):
    primes=[2]
    for y in range(3, int(x**.5)+1, 2):
        isPrime=True
        for z in range(3, int(y**.5)+1, 2):
            if y%z==0:
                isPrime=False
                break
        if isPrime==True:
            primes.append(y)
    return primes

def scq(primes,a):
    s=[]
    c=[]
    q=[]
    for y in primes:
        temp=y**2
        s.append(temp)
        temp*=y
        if temp<a:
            c.append(temp)
            temp*=y
            if temp<a:
                q.append(temp)
    print len(s), len(c), len(q)
    return s, c, q

def main(a):
    t=time.time()
    b=scq(Primes(a),a)
    print "primes done"
    s=b[0]
    c=b[1]
    q=b[2]
    print q[-1]
    print c[-1]
    array=[]
    for x in s:
        for y in c:
            for z in q:
                if x+y+z<a:
                    array.append(x+y+z)
                    #print x, y, z, x+y+z
    print time.time()-t
    return len(list(set(array)))

print main(50000000)
