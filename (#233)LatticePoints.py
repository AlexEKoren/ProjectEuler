from math import sqrt
def isSqr(x):
    return sqrt(x).is_integer()

def main(n,l):
    m=0
    total=0
    for c in range(1105,l,1105):
        count=1
        for b in range(1,c):
            if isSqr(c**2-b**2):
                count+=1
        if count>m:
            m=count
            print c, count
            total+=1

main(420,200000)
