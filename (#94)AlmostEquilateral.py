import time
def main(x):
    t=time.time()
    total=16
    count=0
    z=False
    a=7
    while a<10**x/3:
        #print a
        if count%2==0:
            b=a-1
            c=(a**2-(b/2)**2)**.5
            if int(c)==c:
                if c*b/2==int(c*b/2):
                    total+=2*a+b
                    print a, b, c, "option 1", total
                    z=True
        else:
            if (a-1)**.5==int((a-1)**.5):
                b=a+1
                c=(a**2-(b/2)**2)**.5
                if int(c)==c:
                    if c*b/2==int(c*b/2):
                        total+=2*a+b
                        print a, b, c, "option 2", total
                        z=True
        if z==True:
            count+=1
            a=int(a*3.5)
            z=False
        else:
            a+=2
    print total, time.time()-t

main(9)
                
