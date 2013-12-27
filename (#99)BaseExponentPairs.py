import AEKsys
import math
import time
def main():
    t=time.time()
    q=(open(AEKsys.MyPrograms+"\\#99base_exp.txt","r")).readlines()
    temp=[]
    pairs=[]
    pair=[]
    count=0
    for x in q:
        temp.append(x)
    for x in temp:
        #print x
        pairs.append([x[0:x.index(',')],x[x.index(',')+1:]])
    for x in pairs:
        temp=[]
        for y in x:
            if not y.__contains__('\n'):
                temp.append(int(y))
            else:
                temp.append(int(y[0:y.index('\n')]))
        pair.append(temp)
    m=0
    mc=0
    c=1
    for x in pair:
        digits=int(1+x[1]*math.log10(x[0]))
        if digits>=m:
            m=digits
            mc=c
        c+=1
    print mc, time.time()-t
        

main()
