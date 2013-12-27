import random
import itertools
def main():
    pSum=0
    cSum=0
    pCount=0
    tCount=0
    for z in range(10000000):
        for x in range(9):
            temp=random.randrange(1,5)
            pSum+=temp
        for x in range(6):
            temp=random.randrange(1,7)
            cSum+=temp
        if pSum>cSum:
            pCount+=1
        tCount+=1
        pSum=0
        cSum=0
    print str(pCount)+"/"+str(tCount), pCount*1.0/tCount

def main2():
    pyr=list(itertools.product('1234', repeat=9))
    cub=list(itertools.product('123456',repeat=6))
    print "perms done"
    pyrs=[]
    cube=[]
    for x in pyr:
        temp=0
        for y in x:
            temp+=int(y)
        pyrs.append(temp)
    for x in cub:
        temp=0
        for y in x:
            temp+=int(y)
        cube.append(temp)
    print len(pyrs), len(cube)
    pyrs.sort()
    cube.sort()
    pCount=0
    tCount=0
    cubes=[]
    pyramids=[]
    x=0
    while x<len(cube)-1:
        #print x
        count=1
        while cube[x]==cube[x+1]:
            count+=1
            x+=1
        print cube[x],count
        cubes.append([cube[x],count])
        x+=1
    x=0
    cubes.append([36,1])
    print "cubes done"
    #print cubes
    while x<len(pyrs)-1:
        #print x
        count=1
        while pyrs[x]==pyrs[x+1]:
            count+=1
            x+=1
        print pyrs[x],count
        pyramids.append([pyrs[x],count])
        x+=1
    pyramids.append([36,1])
    #print cubes, pyramids
    for y in pyramids:
        for x in cubes:
            if y[0]>x[0]:
                pCount+=y[1]*x[1]
                #print y[0],x[0], pCount
            tCount+=y[1]*x[1]   
    
        
    print str(pCount)+"/"+str(tCount), pCount*1.0/tCount
main2()
