from itertools import *

def main(a):
    for x in range(2,a):
        total=0
        perms=permutations('abcdefghijklmnopqrstuvwxyz',x)
        for y in perms:
            count=0
            #print y
            for p in range(0,x-1):
                m=ord(y[p])
                n=ord(y[p+1])
                if m<n:
                    count+=1
                if count>1:
                    break
            if count==1:
                total+=1
        print x, total#str(total)+"/"+str(len(perms)), total*1.0/len(perms)

main(7)
