import math

def powmod(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if (exponent and 1) == 1:
           result = (result * base) % modulus
        exponent = exponent - 1
        base = (base * base) % modulus
    return result

def main(a):
    total=0
    for x in range(1,10**a):
        temp=0
        while x%10==0:
            temp+=1
            x/=10
        total+=temp
    total=111111111099
    e1=10**12
    e2=pow(math.e,1.0/e1/2)
    print long(e1*e2*math.sqrt(2*math.pi*10**12))
    
#main(1)

def main2(a):
    total=1
    for x in xrange(1,10**a+1):
        total*=x
        total%=10**249999999997
    print total%10**5
main2(3)
