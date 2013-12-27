import time
def rad2(x):
    temp=x
    array=[]
    if temp%2==0:
        array.append(2)
        while temp%2==0:
            temp/=2
    for y in range(3,int(temp**.5)+1,2):
        if temp%y==0:
            array.append(y)
            while temp%y==0:
                temp/=y
    if not array.__contains__(temp):
        array.append(temp)
    final=1
    if len(array)==0:
        array.append(x)
    for y in array:
        final*=y
    return final
        

def rad(a, primes):
    total=1
    y=a
    for x in primes:
        if x>y:
            break
        temp=x
        if y%x==0:
            total*=x
    return total

def main(y):
    t=time.time()
    array=[]
    for x in range(1,y+1):
        array.append([rad2(x), x])
    print "yay!"
    array.sort()
    #print array
    print time.time()-t
    print array[9999]
main(100000)
    
