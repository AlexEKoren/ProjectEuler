import itertools
import math
def main(n):
    pows=[]
    for x in range(int(math.log(n,2))+1):
        pows.append(2**x)
    pows=pows*2
    perms=[]
    total=0
    for x in range(int(math.log(n,2))+5):
        perms.append(itertools.combinations(pows,x))
    finalPerms=[]
    for x in perms:
        for p in x:
            if sum(p)==n:
                total+=1
                '''temp=list(p)
                temp.sort()
                if temp not in finalPerms:
                    finalPerms.append(temp)
    for x in finalPerms:
        if sum(x)==n:
            print x
            total+=1'''
    print total
main(100)
