import itertools
def factors(n):
    return set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

def mul(f):
    t=1
    for x in f:
        t*=x
    return t

def main(a):
    array=[0]*(a+1)
    for x in range(2,int(a*2.5)):
        f=factors(x)
        for n in range(2,int(x/2)+1):
            for y in itertools.combinations_with_replacement(f,n):
                s=sum(y)
                if s==mul(y):
                    if len(y)<=a:
                        if (s<array[len(y)] or array[len(y)]==0):
                            print x, s, y
                            array[len(y)]=s
    print sum(set(array))
    print array

def main2(a):
    array=[0]*((a)+1)
    for n in range(2,a):
        for y in itertools.combinations_with_replacement(range(1,20),n):
            s=sum(y)
            if s==mul(y):
                if len(y)<=a:
                    if (s<array[len(y)] or array[len(y)]==0):
                        print y, s
                        array[len(y)]=s
    print array
main2(20)
