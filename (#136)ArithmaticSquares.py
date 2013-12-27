import time
def main(l):
    a=[0]*(l+1)
    for i in range(l/2-1):
        for x in range(l**2):
            if x-2*i>0:
                temp=x**2-(x-i)**2-(x-2*i)**2
                if temp<l-1 and temp>0:
                    #print temp
                    a[temp]+=1
    count=0
    for x in range(len(a)):
        if a[x]==1:
            print x
            count+=1
    print count

main(200)
