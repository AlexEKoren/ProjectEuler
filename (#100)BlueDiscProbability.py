from math import*
from decimal import Decimal
def quad(a,b,c):
    """solves quadratic equations of the form
        aX^2+bX+c, inputs a,b,c,
        works for all roots(real or complex)"""
    root=b**2-4*a*c
    if root <0:
        return .5,1.5
    else:
        x1=(-b+sqrt(root))/2*a
        x2=(-b-sqrt(root))/2*a
        return x1,x2
    
def main(a):
    x=803761
    tempx=137904
    while x<a:
        #print x
        for y in range(int(.705*x), int(.71*x)):
            if (y*(y-1)*1.0)/(x*(x-1))==.5:
                tempx2=x
                x=int(x*x/tempx)
                tempx=x
                print y,"/",tempx2, tempx
        x+=1
#main(1000000000)

def main2(a):
    x=85
    while x<a:
        for y in range(int(x),10**4):
            if abs(x*1.0/y*((x-1)*1.0/(y-1))-.5)<=10**-10:
                print x, y
                x=int(x*5.6)
                break
        x+=1
        #print x

#main2(10**7)

def main3(a):
    x=2
    while x<a*10:
        x1,x2=quad(1,-1,(-1*(2*x**2-x*2)))
        #print x1, x2
        y=max(x1,x2)
        if int(y)==y:
            tempX=Decimal(x)
            y=Decimal(y)
            if (tempX*(tempX-1))/(y*(y-1))==Decimal(.5):
                print y, log10(y), tempX
                #print x, long(y-x), long(y)
                if y>a:
                        print (tempX*(tempX-1))/(y*(y-1))
                        print y, tempX
                        return
                x=int(x*5.828402)
        x+=1
        #print x

main3(10**12)
