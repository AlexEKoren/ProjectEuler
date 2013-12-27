import time
def main(y,z):
    t=time.time()
    total=0
    for x in range(10,10**z):
            if int(str(x)[-1]+str(x)[0:-1])%x==0:
                print x
                total+=x
                total%100000
    '''for x in xrange(10**(z+2),10**(z+3)):
        #if int(str(x)[0])<=x%10:
            if int(str(x)[-1]+str(x)[0:-1])%x==0:
                print x
                total+=x
                total%100000'''
    for x in range(z,101):
        total+=499995
        total%=100000
    print time.time()-t
    print total
main(10**100,6)
