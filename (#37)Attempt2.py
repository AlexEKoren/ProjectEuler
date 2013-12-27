def Primes(y):
    primes=[]
    i=3
    while i<y:
        isprime=True
        for x in range(2, int(i**.5 + 1)):
            if i%x==0: 
                isprime=False
                break
        if isprime:
            primes.append(i)
        i=i+1
    return primes

def main():
    i=200000
    final=0
    primes=Primes(50000000)
    m=0
    print "done."
    while i<len(primes):
        p=0
        k=0
        q=0
        while q<len(primes):
            if str(primes(q)).startswith(str(2)) or str(primes(q)).startswith(str(4)) or str(primes(q)).startswith(str(6)) or str(primes(q)).startswith(str(8)) or str(primes(q)).startswith(str(0)):
                primes.remove(primes(q))
        while k<len(j):
            if not primes.__contains__(int(j[0:len(j)-k])):
                break
            else:
                k=k+1
        if k==len(j):
            while l>0:
                if not primes.__contains__(int(j[len(j)-l:len(j)])):
                    break
                else:
                    l=l-1
            if l==0:
                print j
                final=final+int(j)
                m=m+1
        if m==11:
            break
        i=i+1
    print final

main()
