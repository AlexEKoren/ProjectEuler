def check(x):
    for d in range(1,int(x**.5)+2):
        q=x//d
        '''s=d**2
        q=x//(s)
        r=x%(s)
        print q, s, r
        if q*r==s**2:
            print x, q, s, r
            return True'''
        if x==d*(q+float(d)/q):
            print x, q, d, x**.5
            return True
        
    return False

def main(a):
    s=0
    for x in range(2,int(a**.5)+1):
        if check(x**2):
            s+=x**2
    print s

main(10**7)

'''n=dq+r
n=dq+(d*d/q)
n=dq+d**2/q
n=d(q+d/q)'''
