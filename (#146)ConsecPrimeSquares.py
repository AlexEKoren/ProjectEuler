import random
def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in xrange(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1

def isPrime(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in xrange(3):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True

def main(a):
    total=0
    for x in range(10,a,2):
        n=x**2
        if isPrime(n+1):
            print x
            if isPrime(n+3):
                if isPrime(n+7):
                    if isPrime(n+9):
                        if isPrime(n+13):
                            if isPrime(n+27):
                                total+=x
                                print x
    print total

main(1000000)
                                
