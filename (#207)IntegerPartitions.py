def drange(start, stop, step):
     r = start
     while r < stop:
             yield r
             r += step

def main(m):
    num=0
    denom=0
    for k in range(2,m+1):
        #print k
        t=0
        while 4**t<2**t+k:
            #print t
            t+=1
        if 4**t==2**t+k:
            print "yes:",k
            num+=1
            denom+=1
        else:
            print k
            for t1 in drange(1.001,4,.001):
                    b=False
                    #print k, abs(4-2-(k**(1.0/(t+1)))), k**(1.0/(t+1)), t
                    if abs(2-(k**(1.0/(t1+1))))<.00001 and t1!=int(t1):
                        print t1
                        print "non perfect", k, t1, k**(1.0/(t1+1))
                        break
                        '''for t2 in drange(t, t+.001, .00001):
                            if abs(2-(k**(1.0/(t2+1))))<.000001:
                                print "non perfect", k, t2, k**(1.0/(t+1))
                                denom+=1
                                b=True
                                break'''
                    if b==True:
                        break
    print num, denom, num/denom

main(20)
