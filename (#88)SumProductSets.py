import math
import time
def main(a):
    m=a*2
    nf=int(math.log(m,2))
    values=[x*2 for x in range(a+1)]
    factors=[0 for x in range(nf)]
    factors[0]=1
    cm=1
    x=0
    while True:
        if x==0:
            if cm==nf:
                break
            if factors[0]<factors[1]:
                factors[0]+=1
            else:
                cm+=1
                factors[cm-1]=a**2
                factors[0]=2
            x+=1
            factors[1]=factors[0]-1
        elif x==cm-1:
            factors[x]+=1
            total=0
            prod=1
            for y in range(cm):
                prod*=factors[y]
                total+=factors[y]
            if prod>m:
                x-=1
            else:
                p=prod-total+cm
                #print p
                if p<=a and prod<values[p]:
                    values[p]=prod
        elif factors[x]<factors[x+1]:
            factors[x]+=1
            factors[x+1]=factors[x]-1
            x+=1
        elif factors[x]>=factors[x+1]:
            x-=1
    #print values
    print sum(set(values))-2
t=time.time()
main(1000)
print time.time()-t
        
