import itertools
def sortAll(a):
    x=0
    while x<len(a):
        a[x].sort()
        x+=1
    return a

def removeCopies(a):
    x=[]
    for y in a:
        if not y in x:
            x.append(y)
    return x        

def main():
    sq=["01","04","09","16","25","36","49","64","81"]
    di=[]
    for x in itertools.combinations(range(10),6):
        d=list(x)
        d.sort()
        di.append(d)
    dice=[]
    for x in di:
        temp=x
        temp.sort()
        dice.append(temp)
    total=0
    used=[]
    for x in range(len(dice)):
        d1=dice[x]
        for y in range(x,len(dice)):
            d2=dice[y]
            count=0
            for s in sq:
                b=False
                if s=="09":
                    if (0 in d1 and 6 in d2) or  (6 in d1 and 0 in d2):
                        b=True
                        count+=1
                elif s=="64":
                    if (4 in d1 and 9 in d2) or  (9 in d1 and 4 in d2):
                        b=True
                        count+=1
                elif s=="36":
                    if (3 in d1 and 9 in d2) or  (9 in d1 and 3 in d2):
                        b=True
                        count+=1
                elif s=="16":
                    if (1 in d1 and 9 in d2) or (9 in d1 and 1 in d2):
                        b=True
                        count+=1
                elif s=="49":
                    if (4 in d1 and 6 in d2) or (6 in d1 and 4 in d2):
                        b=True
                        count+=1
                if b==False:
                    if (int(s[0]) in d1 and int(s[1]) in d2) or (int(s[1]) in d1 and int(s[0]) in d2):
                        count+=1
            if count==9:
                total+=1
    print total
main()

