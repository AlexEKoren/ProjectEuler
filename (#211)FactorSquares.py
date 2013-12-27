import math
def factorSieve(a):
    sieve=[[1,x**2] for x in range(a+1)]
    sqrt=int(a**.5)+1
    for x in range(2,int(a/2)+1):
        for y in range(2*x, a+1, x):
            sieve[y].append(x**2)
    return sieve

def sq(a):
    return sum(a)

def isSq(x):
    return math.sqrt(x).is_integer()

def main(a):
    l=factorSieve(a)
    print "done"
    total=0
    for x in l:
        if isSq(sq(x)):
            total+=max(x)
    print total

main(1000000)
