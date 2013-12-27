import time
def isPrime(x):
    if x==1:
        return False
    if x==2:
        return True
    if x%2==0:
        return False
    for y in range(3,int(x**.5)+1,2):
        if x%y==0:
            return False
    return True

def main(a):
    t=time.time()
    tri=[]
    num=1
    count=0
    countMax=1
    for x in range(a):
        temp=[]
        while count<countMax:
            temp.append([num, isPrime(num)])
            num+=1
            count+=1
        tri.append(temp)
        count=0
        countMax+=1
    print time.time()-t
    #print tri
main(1000)

