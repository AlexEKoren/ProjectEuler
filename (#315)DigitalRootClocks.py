def digitalRoot(x):
    string=str(x)
    total=0
    for y in string:
        total+=int(y)
    return total

def Primes(x,y):
    primes=[]
    for z in range(x+1,y,2):
        prime=True
        for a in range(3,int(z**.5)+1,2):
            if z%a==0:
                prime=False
                break
        if prime==True:
            primes.append(z)
    return primes

def changeClock(x, clock):
    c=clock
    s=str(x)
    if s[0]==1:
        c[0][0]==1
        c[0][1]==1
    if s[0]==0:
        for x in c[0]:
            x=0
    for x in s[1:]:
        if x==1:
            clock[s.index(x)][1][1]==1
            clock[s.index(x)][1][3]==1
        if x==2:
            clock[s.index(x)]
def main(x):
    clock=[[0,0],[[0,0,0],[0,0,0,0]],[[0,0,0],[0,0,0,0]],[[0,0,0],[0,0,0,0]],[[0,0,0],[0,0,0,0]],[[0,0,0],[0,0,0,0]],[[0,0,0],[0,0,0,0]],[[0,0,0],[0,0,0,0]]]
    
