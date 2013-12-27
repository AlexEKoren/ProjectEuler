import math
def main():
    i=3
    total=0
    while i<2500000:
        subtotal=0
        for m in str(i):
            subtotal=subtotal+math.factorial(int(m))
        if subtotal==i:
            print i
            total=total+i
        i=i+1
    print total
main()
