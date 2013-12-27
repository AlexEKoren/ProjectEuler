from fractions import gcd
def factorial(x):
    return 1 if x<=1 else factorial(x-1)*x

def S(n):
    t=0
    for d in range(1,int(n**.5)+1):
        if n%d==0:
            if gcd(d,n/d)==1:
                print d, n/d
                t+=d**2
                t+=(n/d)**2
    return t

def main(a):
    for x in range(2,a):
        print x, S(x)
S(factorial(15))
