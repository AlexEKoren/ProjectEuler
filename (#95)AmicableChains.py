import time
def factors(x):
    f=[1]
    if x%2==0:
        for y in range(2,int(x**.5)+1):
            if x%y==0:
                f.append(y)
                f.append(x/y)
    else:
        for y in range(3,int(x**.5)+1,2):
            if x%y==0:
                f.append(y)
                f.append(x/y)
    return sum(list(set(f)))

def getPrime(x):
    if x==0:
        return 2
    count=0
    y=3
    while 1:
        isPrime=True
        for z in range(3, int(y**.5)+1, 2):
            if y%z==0:
                isPrime=False
                break
        if isPrime==True:
            count+=1
        if count==x and isPrime==True:
            return y
        y+=2

def factors2(x):
    #print "yes"
    s=1
    lastsum=0
    ip=0
    p=0
    n=x
    while 1:
          p=getPrime(ip)
          #print p
          if p*p>n:
              break
          lastsum=s
          while n%p==0:
              n/=p
              s=s*p+lastsum
          ip+=1
    if n>1:
        s*=n+1
    return s-x;

def main(a):
    t=time.time()
    nums=[]
    for x in range(10000,1000000):
        nums.append(x)
    m=1
    mx=1
    for x in range(100000,a):
        b=False
        l=0
        #print x
        temp=x
        temp=factors(temp)
        array=[]
        if temp!=1:
            while 1:
                temp=factors(temp)
                if array.__contains__(temp):
                    #print array
                    #print x,c
                    #array.append(temp)
                    i=array.index(temp)
                    l=len(array)-1-i
                    for y in array:
                        if nums.__contains__(y):
                            nums.remove(y)
                    break
                array.append(temp)
                if temp==1 or temp>a:
                    #print x, "break"
                    b=True
                    break
                #print temp, x
            if l>m and b==False:
                m=l
                mx=min(array)
                print m, mx
                print time.time()-t
                return
#print getPrime(5)
#print factors2(28)
main(1000000)          
        
