import AEKsys
from itertools import izip, cycle
 
def XOR(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))

def main():
    f=(open(AEKsys.MyPrograms+ "\\#59cipher.txt","r")).readlines()
    numList=f[0].split(',')
    charList=[]
    for x in numList:
        charList.append(chr(int(x)))
    f=""
    for y in charList[:200]:
        f+=y
    for a in range(97,123):
        cA=chr(a)
        for b in range(97,123):
            cB=chr(b)
            for c in reversed(range(97,123)):
                found=False
                d=True
                #print cA+cB+chr(c)
                z=XOR(f, str(cA+cB+chr(c)))
                #print z, cA, cB, chr(c), "\n"
                count=0
                for x in z:
                    if (ord(x)>97 and ord(x)<122) or ord(x)==32 or ord(x)==33 or ord(x)==46 or ord(x)==63:
                        count+=1
                    '''else:
                        d=False
                        break'''
                if count>170:
                    if z.__contains__("God"):
                        print z, cA, cB, chr(c), "\n"
                        key=cA+cB+chr(c)
                        found=True
                if found==True:
                    break
            if found==True:
                break
        if found==True:
            break
    total=0
    final=""
    if found==True:
        for y in charList:
            final+=y
        final=XOR(final,key)
        for y in final:
            total+=ord(y)
        print total
        
main()
