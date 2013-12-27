import itertools

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
    primes=Primes(1000)
    perms=list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
    print perms[0]
    total=0
    for x in perms:
        i=2
        y=0
        while i<len(x)-1:
            temp=int(str(x)[i])*100+int(str(x)[i+1])*10+int(str(x)[i+2])
            divisible=False
            for y in primes:
                if temp%y==0:
                    i=i+1
                    divisible=True
                    break
            if divisible==False:
                break
        if divisible==True:
            total=total+x
main()
            
            
