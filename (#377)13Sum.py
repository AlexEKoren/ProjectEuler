def check(x,n):
    return sum(int(y) for y in str(x))==n

def check0(x):
    while x/10!=0:
        if x%10==0:
            return False
        x/=10
    return True

def main(n):
    count=0
    total=0
    for x in range(111112):
        if check0(x):
            if check(x,n):
                print x
                count+=1
                total+=x
    print count,total
    
def main2(n,i):
    total=0
    for x in range(1,i+1):
        print x
        total+=pow(2,(n**x-1),10**30)
    print total%10**9
main(6)
#main2(13,17)
