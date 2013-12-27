def lightNeeded(x):
    if x==0:
        return 6
    if x==1:
        return 2
    if x==2:
        return 5
    if x==3:
        return 5
    if x==4:
        return 4
    if x==5:
        return 5
    if x==6:
        return 6
    if x==7:
        return 4
    if x==8:
        return 7
    if x==9:
        return 6
'''

def changeConsumed(x,y):
    if y=="*":
        return lightNeeded(x)
    if x==y:
        return 0
    if (x==0 or y==0):
        if (x==0 and y==1) or (x==1 and y==0):
            return 4
        if (x==0 and y==2) or (x==2 and y==0):
            return 3
        if (x==0 and y==3) or (x==3 and y==0):
            return 3
        if (x==0 and y==4) or (x==4 and y==0):
            return 4
        if (x==0 and y==5) or (x==5 and y==0):
            return 3
        if (x==0 and y==6) or (x==6 and y==0):
            return 2
        if (x==0 and y==7) or (x==7 and y==0):
            return 2
        if (x==0 and y==8) or (x==8 and y==0):
            return 1
        if (x==0 and y==9) or (x==9 and y==0):
            return 2
    if (x==1 or y==1):
        if (x==1 and y==2) or (x==2 and y==1):
            return 5
        if (x==1 and y==3) or (x==3 and y==1):
            return 3
        if (x==1 and y==4) or (x==4 and y==1):
            return 2
        if (x==1 and y==5) or (x==5 and y==1):
            return 5
        if (x==1 and y==6) or (x==6 and y==1):
            return 6
        if (x==1 and y==7) or (x==7 and y==1):
            return 2
        if (x==1 and y==8) or (x==8 and y==1):
            return 5
        if (x==1 and y==9) or (x==9 and y==1):
            return 4
    if (x==2 or y==2):
        if (x==2 and y==3) or (x==3 and y==2):
            return 2
        if (x==2 and y==4) or (x==4 and y==2):
            return 5
        if (x==2 and y==5) or (x==5 and y==2):
            return 4
        if (x==2 and y==6) or (x==6 and y==2):
            return 3
        if (x==2 and y==7) or (x==7 and y==2):
            return 5
        if (x==2 and y==8) or (x==8 and y==2):
            return 2
        if (x==2 and y==9) or (x==9 and y==2):
            return 3
    if (x==3 or y==3):
        if (x==3 and y==4) or (x==4 and y==3):
            return 3
        if (x==3 and y==5) or (x==5 and y==3):
            return 2
        if (x==3 and y==6) or (x==6 and y==3):
            return 3
        if (x==3 and y==7) or (x==7 and y==3):
            return 3
        if (x==3 and y==8) or (x==8 and y==3):
            return 2
        if (x==3 and y==9) or (x==9 and y==3):
            return 1
    if (x==4 or y==4):
        if (x==4 and y==5) or (x==5 and y==4):
            return 3
        if (x==4 and y==6) or (x==6 and y==4):
            return 4
        if (x==4 and y==7) or (x==7 and y==4):
            return 2
        if (x==4 and y==8) or (x==8 and y==4):
            return 3
        if (x==4 and y==9) or (x==9 and y==4):
            return 2
    if (x==5 or y==5):
        if (x==5 and y==6) or (x==6 and y==5):
            return 1
        if (x==5 and y==7) or (x==7 and y==5):
            return 3
        if (x==5 and y==8) or (x==8 and y==5):
            return 2
        if (x==5 and y==9) or (x==9 and y==5):
            return 1
    if (x==6 or y==6):
        if (x==6 and y==7) or (x==7 and y==6):
            return 4
        if (x==6 and y==8) or (x==8 and y==6):
            return 1
        if (x==6 and y==9) or (x==9 and y==6):
            return 2
    if (x==7 or y==7):
        if (x==7 and y==8) or (x==8 and y==7):
            return 3
        if (x==7 and y==9) or (x==9 and y==7):
            return 2
    if (x==8 or y==8):
        if (x==8 and y==9) or (x==9 and y==8):
            return 1'''

def dig(x):
    total=0
    while x>0:
        total+=x%10
        x/=10
    return total

def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def countClock(x):
    s=str(x)
    total=0
    for y in s:
        total+=lights(y).count("1")
    return total

def changeClock(x,y):
    s1=str(x)
    s2=str(y)
    while len(s2)<len(s1):
        s2="*"+s2
    total=0
    for z in range(len(s1)):
        if s2[z]=="*":
            total+=changeConsumed(int(s1[z]),s2[z])
        else:
            total+=changeConsumed(int(s1[z]),int(s2[z]))
    return total

def lights(x):
    if x=="*":
        return '0000000'
    x=int(x)
    if x==0:
        return '1111110'
    if x==1:
        return '0110000'
    if x==2:
        return '1101101'
    if x==3:
        return '1111001'
    if x==4:
        return '0110011'
    if x==5:
        return '1011011'
    if x==6:
        return '1011111'
    if x==7:
        return '1110010'
    if x==8:
        return '1111111'
    if x==9:
        return '1111011'

def changeClock2(x,y):
    s1=str(x)
    s2=str(y)
    total=0
    while len(s2)<len(s1):
        s2="*"+s2
    for z in range(len(s1)):
        a=int(lights(s1[z]),2)
        b=int(lights(s2[z]),2)
        #print x,y, a, b, bin(a^b), lights(s1[z]), lights(s2[z])
        total+=bin(a^b).count("1")
    return total   
        
def main(a,b):
    p=Primes(b)
    primes=[]
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    x=0
    while primes[x]<a:
        x+=1
    count1=0
    count2=0
    print primes[-1]
    #primes=[137]
    #x=0
    for y in range(x, len(primes)):
        p=primes[y]
        #print p
        count1+=countClock(p)*2
        count2+=countClock(p)
        #print count1, count2
        prev=p
        nex=dig(p)
        while prev>=10:
            count1+=countClock(nex)*2
            #print nex, countClock(nex)*2
            count2+=changeClock2(prev,nex)
            #print prev, nex, changeClock2(prev,nex)
            prev=nex
            nex=dig(nex)
            #print prev, nex
        #print nex
        count2+=lightNeeded(nex)
    print count1, count2, count1-count2
        
main(10000000,20000000)
        
