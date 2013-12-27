def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(a):
    print Primes(a)
    primes = [x for x in range(len(Primes(a))) if Primes(a)[x]]
    #print primes
    nums = [True] * (a+1)
    for p in primes:
        for x in range(p**2, a, p**2):
            nums[x] = False
    print nums.count(True)-1, len(primes), primes

def main2(a):
    pr = Primes(a)
    primes = [x for x in range(len(pr)) if pr[x]]
    sq = int(a**.5)+2
    nums = [True] * (sq)
    total = 0
    for x in primes:
        s = x**2
        for y in range(s,sq,s):
            nums[y] = False
        for y in range(1,sq):
            if y
        

main2(2**4)
