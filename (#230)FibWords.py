def main(n):
    a="1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    b="8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"
    c=127*19*n*7**n    
    final=0
    while len(b)<c:
        a,b=b,a+b
    for x in range(n+1):
        final+=10**x*long((b[127*19*x*7**x-1]))
    print final

main(5)
