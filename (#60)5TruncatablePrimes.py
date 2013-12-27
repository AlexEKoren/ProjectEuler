import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(a, l):
    t=time.time()
    ptemp=Primes(a)
    print "sieve done", time.time()-t
    primes=[]
    for x in range(3,len(ptemp)):
        if x>l:
            break
        if ptemp[x]:
            primes.append(x)
    print "primes done", time.time()-t
    for x in primes:
        print x
        for y in primes:
            if y<x:
                continue
            if ptemp[int(str(x)+str(y))]:
                if ptemp[int(str(y)+str(x))]:
                    for z in primes:
                        if z<y or z<x:
                            continue
                        if ptemp[int(str(x)+str(z))]:
                            if ptemp[int(str(z)+str(x))]:
                                if ptemp[int(str(y)+str(z))]:
                                    if ptemp[int(str(z)+str(y))]:
                                        for u in primes:
                                            if u<z or u<y or u<x:
                                                continue
                                            if ptemp[int(str(x)+str(u))]:
                                                if ptemp[int(str(u)+str(x))]:
                                                    if ptemp[int(str(y)+str(u))]:
                                                        if ptemp[int(str(u)+str(y))]:
                                                            if ptemp[int(str(z)+str(u))]:
                                                                if ptemp[int(str(u)+str(z))]:
                                                                    for v in primes:
                                                                        if v<u or v<x or v<y or v<z:
                                                                            continue
                                                                        if ptemp[int(str(x)+str(v))]:
                                                                            if ptemp[int(str(v)+str(x))]:
                                                                                if ptemp[int(str(y)+str(v))]:
                                                                                    if ptemp[int(str(v)+str(y))]:
                                                                                       if ptemp[int(str(z)+str(v))]:
                                                                                           if ptemp[int(str(v)+str(z))]:
                                                                                               if ptemp[int(str(u)+str(v))]:
                                                                                                   if ptemp[int(str(v)+str(u))]:
                                                                                                       print x, y, z, u, v, x+y+z+u+v, time.time()-t
                                                                                                       return
print Primes(100000000)[-20:]                                                                           
main(100000000, 10000)
                                
                        
