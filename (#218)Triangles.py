from fractions import gcd
def genPrims(m,n):
    if gcd(m,n)==1:
        return m**2-n**2, 2*m*n, m**2+n**2

def isSquare(x):
    return (x**.5).is_integer()

def main(l):
    total=0
    for m in range(1,l):
        for n in range(1,m):
            g=genPrims(m,n)
            if g!=None:
                a,b,c=g[0],g[1],g[2]
                #print a, b, c
                if isSquare(c):
                    #print c
                    if a*b/2%28!=0 and a*b/2%28!=0:
                        total+=1
                        print a,b,c
    print total
main(10000)
        
