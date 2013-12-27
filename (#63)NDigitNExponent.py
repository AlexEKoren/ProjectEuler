def makePowerArrays(y):
    ones=[]
    twos=[]
    threes=[]
    fours=[]
    fives=[]
    sixes=[]
    sevens=[]
    eights=[]
    nines=[]
    array=[ones, twos, threes, fours, fives, sixes, sevens, eights, nines]
    for x in array:
       n=1
       while n<y:
           x.append((array.index(x)+1)**n)
           n=n+1
    return array

def main():
    array=makePowerArrays(100)
    count=0
    for x in array:
        for y in x:
            if len(str(y))==x.index(y)+1:
                count=count+1
                print y, x.index(y)+1
    print count-98
                
main()
