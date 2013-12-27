from itertools import permutations

def factorial(x):
    if x==1:
        return 1
    return long(x*factorial(x-1))

def main(a):
    perms=permutations('10A'+'x'*(a-3),a)
    final=[]
    count=0
    f=factorial(a-3)
    print f
    x=0
    c=0
    for x in perms:
        #if c<f-1:
            #c+=1
            #continue
        #c=0
        final.append(x)
    for x in final:
        print x
    print len(final)

def main2(l):
    total=0
    for a in range(4,l+1):
        f=long(factorial(a))
        total+=long(f*(2./a)/long(factorial(a-3))*long((16**(a-3))))
        total+=long(f*(1./a)/long(factorial(a-3))*long((16**(a-4)))*(15))
    print long(total)
    print hex(long(total))
main2(16)
