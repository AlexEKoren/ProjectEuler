import itertools
def findMuls():
    l=list(itertools.product(range(0,4),repeat=3))
    final=[]
    for x in l:
        for y in reversed(x):
            if y==0:
                continue
            elif y==2:
                final.append(x)
                break
            else:
                break
    return final

def findScores():
    return list(itertools.product(range(1,21),repeat=3))

def main():
    muls=findMuls()
    scores=findScores()
    count=0
    for x in scores:
        for y in muls:
            temp=x[0]*y[0]+x[1]*y[1]+x[2]*y[2]
