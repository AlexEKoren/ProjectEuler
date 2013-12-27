import math
def findRadius(a,b,c):
    k=.5*(a+b+c)
    temp=k*(k-a)*(k-b)*(k-c)
    if temp>0:
        temp2=math.sqrt(temp)
        if temp2==int(temp2):
            temp3=a*b*c/(4*temp2)
            if temp3==int(temp3):
                print temp3
                return temp3
    return 0
    '''if temp>0:
        temp2=math.sqrt(temp)/k
        if temp2==int(temp2):
            print temp2
            return temp2
    return 0'''

def main(l):
    total=0
    for a in range(1,int(4*l)):
        for b in range(a,int(4*l)):
            for c in range(b,int(4*l)):
                r=findRadius(a,b,c)
                if r<l:
                    #print r
                    total+=r
                else:
                    break
    print total

main(100)

