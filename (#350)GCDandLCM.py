import itertools
def gcd(a, b):
    while b:      
        a,b=b,a%b
    return a

def gcdm(*args):
    return reduce(gcd, args)[0]

def lcm(a, b):
    return a*b//gcd(a,b)

def lcmm(*args):  
    return reduce(lcm, args)[0]

def main(g, l, n):
    nums=list(itertools.combinations_with_replacement(range(0,l+1),n))
    print len(nums)
    count=0
    for x in nums:
        #print gcd(x[0],x[1]), x
        if gcd(x[0],x[1])>=g:
            #print lcm(x[0],x[1]),x
            if lcm(x[0],x[1])<=l:
                print gcd(x[0],x[1]), lcm(x[0],x[1]), x
                count+=1
    print count
print lcm(2, 4)
#main(10,100,2)
