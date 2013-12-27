from fractions import *
def M(a):
    m=0
    mn=0
    md=0
    N=a
    for x in range(2,N):
        n=N**x
        d=x**x
        if n*1.0/d>m:
            m=n*1.0/d
            mn=n
            md=d
    g=gcd(mn, md)
    print mn/g, md/g
    return mn/g, md/g

def D(N, D):
    n=N
    d=D
    while d%2==0:
        d/=2
    while d%5==0:
        d/=5
    if d>1:
        return -1.0*N/D
    return N*1.0/D

def main(a):
    total=0
    for x in range(5,a+1):
        m=M(x)
        #print x,m, D(m[0], m[1])
        total+=D(m[0],m[1])
    print total
main(100)
