def check3(x):
    s=str(x)
    y=0
    while y<len(s)-2:
        if s[y]==s[y+1] and s[y]==s[y+2]:
            return False
        y+=1
    return True

def check(x):
    while x>0:
        if x%10==(x/10)%10 and x%10==(x/100)%10:
            return False
        x/=10
    return True

def main():
    x=1000999999
    total=20.6923829109
    count=0
    while 1:
        if check(x):
            total+=1.0/x
        if x>10011100100:
            print x,total
        x+=1

def main2():
    total=0
    for x in range(1000000):
        if check(x):
            total+=1
    print total

#print check(100023)
#main2()
main()
