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
    i=4
    final=0
    primes=Primes(10000000)
    m=0
    print "done."
    while i<len(primes):
        p=0
        k=0
        j=str(primes[i])
        while p<len(j):
            if int(j[p])%2==0:
                i=i+1
                j=str(primes[i])
                break
            p=p+1
        l=len(j)
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
