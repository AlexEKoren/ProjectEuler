import AEKsys
import time
def convertToNum(s):
    total=0
    temp=[]
    for x in s:
        if x=="M":
            temp.append(1000)
        if x=="D":
            temp.append(500)
        if x=="C":
            temp.append(100)
        if x=="L":
            temp.append(50)
        if x=="X":
            temp.append(10)
        if x=="V":
            temp.append(5)
        if x=="I":
            temp.append(1)
    x=0
    while x<len(temp)-1:
        if temp[x]>=temp[x+1]:
            total+=temp[x]
        else:
            total-=temp[x]
        x+=1
    total+=temp[-1]
    #print total, s
    return total

def convertToRom(a):
    s=""
    while a>=1000:
        s+="M"
        a-=1000
    if a>=900:
        s+="CM"
        a-=900
    while a>=500:
        s+="D"
        a-=500
    if a>=400:
        s+="CD"
        a-=400
    while a>=100:
        s+="C"
        a-=100
    if a>=90:
        s+="XC"
        a-=90
    while a>=50:
        s+="L"
        a-=50
    if a>=40:
        s+="XL"
        a-=40
    while a>=10:
        s+="X"
        a-=10
    if a==9:
        s+="IX"
        a-=9
    while a>=5:
        s+="V"
        a-=5
    if a==4:
        s+="IV"
        a-=4
    while a>0:
        s+="I"
        a-=1
    #print s
    return s
def main():
    t=time.time()
    f=(open(AEKsys.MyPrograms+ "\\#89roman.txt","r")).readlines()
    #print f
    nums=[]
    romans=[]
    firstCount=0
    secondCount=0
    for l in f:
        nums.append(l.split('\n'))
    for l in nums:
        l[0]=l[0].split(" ")
    for l in nums:
        romans.append(l[0][0])
        firstCount+=len(romans[-1])
        secondCount+=len(convertToRom(convertToNum(romans[-1])))
    print firstCount-secondCount, time.time()-t
main()
