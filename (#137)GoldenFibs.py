def check(a,b):
    d = (b**2-a*b-a**2) * b * 1.0
    dd = b**2
    num = long((a * dd)/d)
    return num

def fibs():
    f=[]
    a=1
    b=1
    while b < 10000000:
        f.append(b)
        a,b=b,a+b
    return f


def main():
    f = set([])
    fib = fibs()
    for a in fib:
        for b in fib:
            if b>a:
                n=check(a,b)
                if n==int(n) and n>0:
                    if not n in f:
                        f.add(n)
                        print a, b, n
    print f
    f=list(f)
    f.sort()
    print f[14]

main()
    
