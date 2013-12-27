def factorize(x):
    n=2
    t=1
    while x>1:
        count=0
        while x%n==0:
            count+=1
            x/=n
        t*=(2*count+1)
        n+=1
    return t

def main(a):
    m=0
    num=2*3*5*7*11*13*17*19*23*29*31*37
    x=num
    while 1:
        if factorize(x)>2*a:
            print x, factorize(x)
            return
        #print x, factorize(x)
        x+=num
    

main(4000000)
