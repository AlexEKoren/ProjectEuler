import time
def main(x):
    t=time.time()
    unforced=[]
    forced=[0,1]
    count=0
    for y in range(2, x):
        #print y
        b=True
        for p in range(y/2+2):
            if not forced.__contains__(p) and forced.__contains__(y-p-2):
                b=False
                break
        if b==True:
            unforced.append(y)
            count+=1
            print y, p
        else:
            forced.append(y)
    print x-count, time.time()-t, forced, unforced
main(50)
