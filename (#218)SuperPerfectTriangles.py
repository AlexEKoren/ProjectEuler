import fractions
import time
def squares(x):
    sq=[]
    for y in range(1,int(x**.5)):
        sq.append(y**2)
    return sq
def main(x):
    sq=squares(x)
    t=time.time()
    c=1
    total=0
    for c in sq:
        #print c
        for b in range(1,c):
            a=(c**2-b**2)**.5
            if int(a)==a:
                #print a, b, c
                if a*b%28!=0 and a*b%6!=0:
                    if fractions.gcd(a, b)==1 and fractions.gcd(b, c)==1:
                        total+=1
    print time.time()-t
    print total
main(10**4)
                
