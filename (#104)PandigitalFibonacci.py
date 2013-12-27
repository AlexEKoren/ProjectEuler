import itertools
def checkPan2(b,num):
            for x in range(1,10):
                if b.count(str(x),0,9)!=1:
                    return num
            print "First Pandigital", b[:9],num
            for x in range(1,10):
                if b.count(str(x),-9)!=1:
                    return num
            print "Last Pandigital", b[-9:], num
            
            return True
def checkPan(b, num):
            for x in range(1,10):
                if b.count(str(x),-9)!=1:
                    return num
            print "Last Pandigital", b[-9:], num
            temp=fib(num)
            temp=temp/(10**10)
            temp=str(temp)
            for x in range(1,10):
                if temp.count(str(x),0,9)!=1:
                    return num
            return True
                
def powLF(n):
    if n == 1:     return (1, 1)
    L, F = powLF(n//2)
    L, F = (L**2 + 5*F**2) >> 1, L*F
    if n & 1:
        return ((L + 5*F)>>1, (L + F) >>1)
    else:
        return (L, F)

def fib(n):
    if n & 1:
        return powLF(n)[1]
    else:
        L, F = powLF(n // 2)
        return L * F

def partialFib():
    a=0
    b=1
    count=1
    while 1:
        a,b=b%10**10,(a+b)%10**10
        l=checkPan(str(b), count+1)
        if l==True:
            print count+1
            return
        count+=1
def main():
    x=100
    while 1:
        numTemp=fib(x)%10**10
        #print numTemp
        temp=str(numTemp)
        #print temp
        #print x
        temp2=checkPan(temp,x)
        if not temp2==x:
            print x
            return
        x+=1
#main()
partialFib()
