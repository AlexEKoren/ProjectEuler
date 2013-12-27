import math
def findE():
    total=0
    x=1
    while x<100:
        total+=1.0/math.factorial(x)
        x+=1
    return total
def A(x):
    total=0
    y=1
    for p in range(100):
        if x-p<0:
            total+=1.0/math.factorial(y)
        else:
            total+=A(x-1)*1.0/math.factorial(y)
    return total
def recursiveA(x,y):
        if x<0:
            return 1
        else:
            print recursiveA(x-y,y+1)*1.0/math.factorial(y)
            return recursiveA(x-y,y+1)*1.0/math.factorial(y)
def f(array):
    y=1
    total=0
    for p in reversed(array):
        #print p*1.0/math.factorial(y)
        total+=p*1.0/math.factorial(y)
        #print total
        y+=1
    while y<100:
        total+=1.0/math.factorial(y)
        y+=1
    #print total
    return total

def main(x):
    e=findE()+1
    array=[e-1,2*e-3,7/2*e-6]
    y=3
    while y<=x:
        l=f(array)
        #print l
        array.append((l/e)-l%e)
        print (l/e)-l%e
    b=recursiveA(0,0)
    print b


main(10)

