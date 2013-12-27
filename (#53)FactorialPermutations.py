import math
def main():
    n=23
    r=1
    final=0
    while n<=100:
        while r<=n:
            if math.factorial(n)/(math.factorial(r)*(math.factorial(n-r)))>1000000:
                final=final+1
            r=r+1
        r=0
        n=n+1
    print final
main()
