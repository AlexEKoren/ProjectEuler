import time
from math import *
def main(x):
    f=time.time()
    i=.0000000000001
    count=0
    total=0
    array=[[17,16,15],[305,272,273],[5473, 4896, 4895],[98209,87840,87841]]
    for x in array:
        print x[0], x[1], x[2]
        total+=x[0]
    h=int(array[-1][2]*17.9442717760439)-10
    if h%2==0:
        h+=1
    Q=array[-1][0]+array[-1][1]
    while h<x:
            #print h
        #print int(tan((h+1)/2.0/h)*1000000)==546302
        #if abs(546302-int(tan((h+1)/2.0/h)*1000000))<.01:
            #if count%2==1:
                B=h-1
                #print tan(B/2/h)
                L=(B+Q)
                #print B*((4*L**2-B**2)**.5), h*B*2
                #if B*(4*L**2-B**2)==h*B*2:
                if B*(B*1.25+2)==L**2-1:
                        array.append([L, B, h])
                        print L, B, h, tan(B/2.0/h), time.time()-f, 1
                        total+=L
                        count+=1
                        h=int(h*(17.9442719099064+i))-100
                        if h%2==0:
                            h+=1
                        Q=array[-1][0]+array[-1][1]
            #else:
                B=h+1
                L=(B+Q)
                #print B*((4*L**2-B**2)**.5), h*B*2
                #if B*(4*L**2-B**2)==h*B*2:
                if B*(B*1.25-2)==L**2-1:
                        array.append([L, B, h])
                        print L, B, h, tan(B/2.0/h), time.time()-f, 2
                        total+=L
                        count+=1
                        h=int(h*(17.9442719099064+i))-100
                        if h%2==0:
                            h+=1
                        #if L==1762289.0:
                            #break
                        Q=array[-1][0]+array[-1][1]
                h+=2
    print time.time()-f
    '''temp=1762289
    for x in range(5,13):
        total+=int(temp*17.9442719099064)+1
        temp*=int(17.9442719099064)+1
    print long(total)'''

#main(10000000000)

def main2(a):
    i=16
    x=16
    array=[]
    total=0L
    while x<a:
        #print x
        temp1=5.0/4*x**2+2*x+1
        temp2=temp1-4*x
        #print temp1
        s1=sqrt(temp1)
        s2=sqrt(temp2)
        #print temp
        if s1==int(s1):
            total+=long(sqrt((x/2)**2+(x+1)**2))
            print x, 1, long(sqrt((x/2)**2+(x+1)**2))
            array.append(x)
            x=sum(array)*16
        elif s2==int(s2):
            total+=long(sqrt(long((x/2))**2+long((x-1))**2))
            print x, 2, long(sqrt(long((x/2))**2+long((x-1))**2))
            array.append(x)
            x=sum(array)*16
        x+=i
    print long(total)

def isSqr(x):
    return sqrt(x).is_integer()

def main3(a):
    t=time.time()
    total=0
    count=0
    which=0
    h=3L
    i=2
    while count<a:
        if which%2==1:
            num=5*h**2-2*h+1
            if num%2==0:
                if isSqr(num):
                    if sqrt(num)%2==0:
                        print sqrt(num)/2
                        count+=1
                        total+=long(h)
                        which+=1
                        #h*=5
            '''if 4*(h+i-1)**2==num:
                count+=1
                total+=h+i
                print h+i
                i=h+h+i-1
                #print 1, h, h+i, h-1, i
                which+=1'''
        else:
            num2=5*h**2+h*2+1
            if num2%2==0:
                if isSqr(num2):
                    if sqrt(num2)%2==0:
                        print sqrt(num2)/2
                        count+=1
                        total+=long(h)
                        which+=1
                        #h*=5
            '''if 4*(h+i)**2==num2:
                count+=1
                total+=h+i
                print h+i
                i=h+1+h+i
                #print 2, h, h+i, h+1, i
                which+=1'''
        h+=1
        #print h
    print total, time.time()-t
main3(12)
