def check(a,b):
    d = (b**2-a*b-a**2)
    dd = b**2
    num1 = ((a * dd)/(d*b*1.0))
    num2 = 3*(a**2/(d*1.0))
    #print a,b,num1, num2
    return num1+num2



def main():
    f=[2,5,42,152,296,1050,2037,7205,13970,49392,95760,656357,338546]
    c=True
    b=267
    while len(f)<30:
        for a in range(int(.6180336*b),int(.618034*b)+1):
            n=check(a,b)
            if n==n//1 and n>0 and not n in f:
                f.append(long(n))
                print a, b, n, len(f), a*1./b
        b+=1
    print f

def fib():
    f=[]
    a=2
    b=3
    for x in range(60):
        f.append(b)
        a,b=b,a+b
        a,b=b,a+b
    return f

def main2():
    fibs = fib()
    f=[]
    n=2
    m=1
    i=0
    while len(f)<30:
        f.append(n)
        n+=m*fibs[i]
        if m==1:
            m=2
        else:
            m=1
        i+=1
    print sum(f), i
    

main2()
