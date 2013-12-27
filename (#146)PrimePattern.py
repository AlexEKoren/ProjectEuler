import random
import time
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
    for repeat in range(1):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True

def factors(x):
    f=[]
    for y in range(1,int(x**.5)+1):
        if x%y==0:
            f.append(y)
            if y!=x/y:
                f.append(x/y)
    f.sort()
    return f

def main(a):
    t=time.time()
    total=0
    for n in range(0,a,10):
            if n%3!=0 and (n%7==3 or n%7==4) and n%13!=0:
                x=n**2
                if isPrime(x+1):
                    if isPrime(x+3):
                        if not isPrime(x+5):
                            if isPrime(x+7):
                                if isPrime(x+9):
                                    if not isPrime(x+11):
                                        if isPrime(x+13):
                                            if not isPrime(x+15):
                                                if not isPrime(x+17):
                                                    if not isPrime(x+19):
                                                        if not isPrime(x+21):
                                                            if not isPrime(x+23):
                                                                if not isPrime(x+25):
                                                                    if isPrime(x+27):#, factors(n)
                                                                        total+=n
                                                                        print n, total, time.time()-t
    print total, time.time()-t

main(150000000)
                
