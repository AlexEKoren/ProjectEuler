import time
def main():
    t=time.time()
    penny=.01
    dPenny=.02
    nickel=.05
    dime=.10
    dDime=.20
    dQuarter=.50
    single=1.00
    double=2.00
    counter=0
    j=0
    k=0
    l=0
    m=0
    n=0
    o=0
    p=0
    q=0
    while double*j<=2.00:
        while single*k<=2.00:
            while single*k+dQuarter*l<=2.00:
                while single*k+dQuarter*l+dDime*m<=2.00:
                    while single*k+dQuarter*l+dDime*m+dime*n<=2.00:
                        while single*k+dQuarter*l+dDime*m+dime*n+nickel*o<=2.00:
                            while single*k+dQuarter*l+dDime*m+dime*n+nickel*o+dPenny*p<=2.00:
                                #while penny*q<=2.00:
                                if dPenny*p+nickel*o+dime*n+dDime*m+dQuarter*l+single*k+double*j<=2.00:
                                    counter+=1
                                    #if p%10==0:
                                    #print p*dPenny,o*nickel,n*dime,m*dDime,l*dQuarter,k*single,j*double, counter
                                    #q+=1
                                #q=0
                                p+=1
                            p=0
                            o+=1
                        o=0
                        n+=1
                    n=0
                    m+=1
                m=0
                l+=1
            l=0
            k+=1
        k=0
        j+=1
    t2=time.time()
    print t2-t
    print counter
main()
                    
    
