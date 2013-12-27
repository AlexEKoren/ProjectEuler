def fibonacci(n):
    a,b=1,1
    x=0
    fibs=[1]
    while x<n:
        fibs.append(b)
        a,b=b,a+b
        x+=1
    return fibs
def blues(n):
    total=0
    if n<=4:
        return n/4
    else:
        total+=n-3
        return total+blues(n-1)
    
def main(y):
    fibs=fibonacci(60)
    red=7
    green=3
    blue=2
    x=4
    while x<y-1:
        red+=fibs[x]
        x+=1
    x=2
    while x<y-3:
        green+=fibs[x]
        x+=1
    x=0
    while x<y-5:
        blue+=fibs[x]
        x+=1
    print red
    print green
    print blue
    print red+green+blue
#main(50)
print blues(9)
