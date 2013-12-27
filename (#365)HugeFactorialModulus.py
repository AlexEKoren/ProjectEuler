from operator import *
def factorial(x):
    return reduce(mul, (y for y in range(1,x+1)), 1)

def comb(n, k):
    return factorial(n)/(factorial(k)*factorial(k-n))

def main(n, k):
    c=comb(n,k)
    print c
    for x in range(2, c):
        if c%x==0:
            print x

main(10,4)
