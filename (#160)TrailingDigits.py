import time
def main(y):
    for b in range(1,y):
        tim=time.time()
        t=10*9*8*7*6*5*4*3*2
        a=10**6
        for x in range(11,10**b+1):
            t*=x
            while t%10==0:
                t/=10
            '''if t%10==0:
                t/=10'''
            t%=a
        while t%10==0:
                t/=10
        print t%a, time.time()-tim 
        
def main2(x):
    f=1
    for y in range(1,x):
        if y%10==0:
            while f%100==0:
                f/=100
            print f%10, y
            continue
        f*=y

def main3(y):
        t=10*9*8*7*6*5*4*3*2
        for x in range(11, 10**y+1):
                t*=x
                while t%10==0:
                        t/=10
                t%=10**6
        print t%10**6
        for x in range(10**y+1, 2*10**y+1):
                t*=x
                while t%10==0:
                        t/=10
                t%=10**6
        print t%10**6

def main4(y):
    t=1
    for x in range(1,10000):
        t*=x
    array=[]
    while t%10==0:
        t/=10
    t=t%10**5
    print "second"
    for x in range(10000,100000):
        array.append(x)
    for x in array:
        if x%1000==0:
            print x
        if x%10!=0:
            #print x, 1, t
            temp=pow(x, 597872, 10**5)
            #print temp
            t*=temp
            t%=10**15
        elif x%10000==0:
            temp=pow(x/10000,597872, 10**5)
            #print temp
            t*=temp
            t%=10**15
        elif x%1000==0:
            #print x, 3, t
            t*=pow(x/1000,597872,10**5)
            t%=10**15
        elif x%100==0:
            #print x, 4, t
            t*=pow(x/100,597872,10**5)
            t%=10**15
        else:
            #print x, 5, t
            t*=pow(x/10,597872,10**5)
            t%=10**15
        while t%10==0:
            t/=10
    print t%10**5
#main2(500)
main4(10)
#main(8)
