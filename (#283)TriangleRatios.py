from math import sqrt
def area(a,b,c):
    s=(a+b+c)*1./2
    return sqrt(s*(s-a)*(s-b)*(s-c))

def perimeter(a,b,c):
    return a+b+c

def main(lim, p):
    total=0
    for c in range(1,lim**p):
        for b in range(1,c+1):
            for a in range(1,b+1):
                if a+b>c:
                    if area(a,b,c)%perimeter(a,b,c)==0:
                        total+=perimeter(a,b,c)
                        #print a, b, c, area(a,b,c)/perimeter(a,b,c)
    print total

main(5,4)
                
