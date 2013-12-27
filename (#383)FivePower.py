import math
def fives(n):
    x=int(math.log(n,5))-1
    while n%(5**x)!=0:
        x-=1
    return x

def T(n):
    return fives(math.factorial(2*n-1))<2*fives(math.factorial(n))

def main(a):
    total=0
    for x in range(5,a+1,5):
        if T(x):
            print x
            total+=1
    print total

main(100)
            
        
    
