import time

def takeC(s):
    temp=""
    for y in s:
        if y=="0":
            temp+="1"
        else:
            temp+="0"
    return temp

def binToDec(s):
    x=list(s)
    x.reverse()
    total=0
    y=0
    while y<len(x):
        total+=2**y*int(x[y])
        y+=1
    return total

def A(n):
    t=time.time()
    s="0"
    for x in range(1,5+1):
        s+=takeC(s)
    print s
    x=0
    array=[]
    while x<len(s):
        for y in range(x+1,len(s)):
            temp=binToDec(s[x:y])
            array.append(temp)
        x+=1
    array=list(set(array))
    array.sort()
    print array
    #print array[n]
def inSet(s):
    if not "10101" in s and not "01010" in s and not "10110010" in s and not "11001100" in s and not "00110011" in s and not "101001101" in s:
        if not "1001101001" in s and not "1011010011" in s and not "1100101100" in s and not "10100101101" in s:
            y=0
            dub=0
            while y<len(s)-1:
                if s[y]==s[y+1]:
                    if s[y]==dub:
                        return False
                    else:
                        dub=s[y]
                y+=1
            return True
    return False
def A2(n):
    count=0
    num=0
    array=[]
    while count<n:
        if inSet(bin(num)[2:]):
            #print num, count
            array.append(num)
            count+=1
        num+=1
    #print array
    print num
#print binToDec("111")
#print inSet(str(bin(37))[2:])
A(100)
A2(1000)

