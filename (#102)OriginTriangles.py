import AEKsys
from math import *
def formatTri():
    f=(open(AEKsys.MyPrograms+"\\#102triangles.txt", "r")).readlines()
    triangles=[]
    for x in f:
        temp=""
        count=0
        finalA=[]
        tempA=[]
        for y in x:
            if y!=",":
                temp+=y
            elif count%2==0:
                tempA.append(int(temp))
                count+=1
                temp=""
            else:
                tempA.append(int(temp))
                count+=1
                temp=""
                finalA.append(tempA)
                tempA=[]
        tempA.append(int(temp))
        finalA.append(tempA)
        triangles.append(finalA)
    count=0
    return triangles
def main():
    triangles=formatTri()
    for x in triangles:
        m1=(x[0][1])*1.0/(x[0][0])
        m2=(x[1][1])*1.0/(x[1][0])
        m3=(x[2][1])*1.0/(x[2][0])
        #print m1, m2, m3
        t1=atan((m1-m2)/(1+m1*m2))
        if t1<0:
            t1=2*pi+t1
        t2=atan((m2-m3)/(1+m2*m3))
        if t2<0:
            t2=2*pi+t2
        t3=atan((m3-m1)/(1+m1*m3))
        if t2<0:
            t3=2*pi+t3
        #print t1,t2, t3, x
        if abs(2*pi-t1-t2-t3)<.000000000000001:
            count+=1
    print count

def main2():
    tri=formatTri()
    count=0
    for x in tri:
        x1=x[0][0]
        x2=x[1][0]
        x3=x[2][0]
        y1=x[0][1]
        y2=x[1][1]
        y3=x[2][1]
        m12=((x1-x2)**2+(y1-y2)**2)**.5
        m13=((x1-x3)**2+(y1-y3)**2)**.5
        m23=((x2-x3)**2+(y2-y3)**2)**.5
        m10=(x1**2+y1**2)**.5
        m20=(x2**2+y2**2)**.5
        m30=(x3**2+y3**2)**.5
        s=(m12+m13+m23)/2
        s120=(m12+m10+m20)/2
        s130=(m13+m10+m30)/2
        s230=(m23+m20+m30)/2
        A=(s*(s-m12)*(s-m13)*(s-m23))**.5
        Ap1=(s120*(s120-m12)*(s120-m10)*(s120-m20))**.5
        Ap2=(s130*(s130-m13)*(s130-m10)*(s130-m30))**.5
        Ap3=(s230*(s230-m23)*(s230-m20)*(s230-m30))**.5
        if abs(A-(Ap1+Ap2+Ap3))<.01:
            count+=1
    print count
main2()
        
        
