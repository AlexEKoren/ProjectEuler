from math import *
def findSlope(x1, y1, x2, y2):
    if x1-x2==0:
        return -123454
    return (y1-y2)/(x1-x2)

def main(a):
    total=0
    tris=[]
    for x1 in range(a+1):
        for y1 in range(a+1):
            if x1==y1 and x1==0:
                continue
            for x2 in range(a+1):
                for y2 in range(a+1):
                    if x2==y2 and x2==0:
                        continue
                    if x1==x2 and y1==y2:
                        continue
                    if x1==y1 and x2==y2:
                        continue
                    #print x1, y1, x2, y2
                    l1=sqrt(x1**2+y1**2)
                    l2=sqrt(x2**2+y2**2)
                    l3=sqrt((x1-x2)**2+(y1-y2)**2)
                    lS=[l1,l2,l3]
                    #print lS, x1, y1, x2, y2
                    lS.sort()
                    #print lS
                    if abs(lS[0]**2+lS[1]**2-lS[2]**2)<10**-10:
                        if lS not in tris:
                            total+=3
                            #print x1, y1, x2, y2
                            tris.append(lS)
    print total+a-a%2
main(50)
