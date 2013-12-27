import time
def factorial(x):
    total=x
    temp=x-1
    while temp>1:
        total*=temp
        temp-=1
    return total

def f(n):
    total=0
    for x in str(n):
        total+=factorial(int(x))
    return total

def sumDigits(n):
    total=0
    for x in str(n):
        total+=int(x)
    return total

def sumDigits2(n):
    total=0
    temp=n
    while temp>0:
        total+=temp%10
        temp/=10
    return total

def g(i):
    x=1
    while 1:
        if sumDigits2(f(x))==i:
            return x
        else:
            x+=1

def main(x):
    t=time.time()
    total=0
    array=[]
    for i in range(1,x+1):
        '''if i>5:
            if i%3==1:
                temp=int("1"+str(array[i-2]))
                print temp
                if sumDigits2(f(temp))==i:
                    y=sumDigits2(temp)
            elif i%3==2:
                temp=int("2"+str(array[i-3]))
                print temp
                if sumDigits2(f(temp))==i:
                    y=sumDigits2(temp)
            else:
                z=g(i)
                y=sumDigits2(z)
        else:'''
        z=g(i)
        y=sumDigits2(z)
        total+=y
        print i, z, y
        array.append(z)
    print time.time()-t
    return total
  
print main(50)
