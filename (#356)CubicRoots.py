from math import *
import time
def cubicRoot(a, b, c, d):
    f=((3*c/a)-(b**2/a**2))/3.0
    #print "f=", f
    g=((2*b**3/a**3)-(9*b*c/a**2)+27*d/a)/27.0
    #print "g=", g
    h=g**2/4.0+f**3/27.0
    #print "h=", h
    if h>0:
        #print "h>0"
        R=g/2.0*-1+(h**.5)
        S=R**(1.0/3)
        T=g/2.0*-1-(h**.5)
        if T<0:
            U=((-1*T)**(1.0/3))*-1
        else:
            U=T**(1.0/3)
        X1=(S+U)-(b/(3.0*a))
        return X1
    elif h==0:
        #print "h==0"
        return (d/a)**(1.0/3)*-1
    else:
        #print "h<0"
        i=((g**2/4.0)-h)**.5
        #print "i=", i
        j=i**(1.0/3)
        #print "j=", j
        K=acos(g/(2*i)*-1)
        #print "K=", K
        L=j*-1
        #print "L=", L
        M=cos(K/3.0)
        #print "M=", M
        N=3**.5*sin(K/3.0)
        #print "N=", N
        P=(b/(3.0*a))*-1
        #print "P=", P
        X1=2*j*cos(K/3.0)-(b/(3.0*a))
        X2=L*(M+N)+P
        X3=L*(M-N)+P
        return X1,X2,X3
def PowerMod(a, b, m):
    tempo=0
    if (b ==0):
        tempo=1
    elif b==1:
        tempo=a
    else:
        temp=PowerMod(a,b/2.0,m)
        if b%2==0:
            tempo=(temp*temp)%m
        else:
            tempo=((temp*temp)%m)*a%m
    return tempo;

def PowerMod2(a, b, m):
    c=1
    for x in xrange(b):
        c=a*c%m
        #print c
    return c

def main(i):
    t=time.time()
    total=0
    for n in range(1, i+1):
        m=cubicRoot(1,-PowerMod2((2**n),654321,10**8), 0, PowerMod2((2**n),654321,10**8))
        #print m
        if type(m)==float:
            p=int(PowerMod2(m, 4321,10**8))
            print m, p
        else:
            p=int(PowerMod2(max(m),4321,10**8))
            print max(m),p
        total+=p
        #print time.time()-t
        #print m,p
    print total%10**8
#print (pow(3, 2345, 7))
#print PowerMod2(3.423,98721,7)
main(30)

def tester(n,x):
    c=1
    for y in xrange(2*10**x):
        c*=n
        if c%10**x==64:
            print c,y
        c%=10**(x+1)
#tester(2,2)
#print pow(2, 490823, 10**5)
    
