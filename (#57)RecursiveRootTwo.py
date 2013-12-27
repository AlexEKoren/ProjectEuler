from fractions import Fraction
def recursion(x):
    if x==1:
        return 2
    else:
        return 2+1.0/recursion(x-1)

def main():
    total=0
    for x in range(2):
        print recursion(x)
        if len(str(Fraction(recursion(x)-1))[0])>len(str(Fraction(recursion(x)-1))[2]):
            total+=1
    print total
print str(Fraction(Fraction(recursion(5)-1)))
print len(str(Fraction(recursion(7)-1))[0])>len(str(Fraction(recursion(7)-1))[2])
#main()
