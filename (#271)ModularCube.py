import time
def isCube(x):
    n=int(x**(1./3))+1
    return n**3==x

def main(n):
    t=time.time()
    s=n+1
    total=0
    while s<n**3:
        if isCube(s):
            print s, s**(1./3), (s-1)/n
            total+=s**(1./3)
        s+=n
    print total
    
main(91)
13082761331670030
