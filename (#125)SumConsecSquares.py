def findSquares(x):
    s=[]
    y=1
    while y**2<x+1:
        s.append(y**2)
        y+=1
    return s

def main(x):
    sq=findSquares(x)
    #print sq
    total=-1
    for y in range(1,len(sq)):
        z=y
        temp=sq[z]+sq[z-1]
        while temp<x and z<len(sq)-1:
            if str(temp)==str(temp)[::-1]:
                print temp, sq[z]
                total+=temp
            z+=1
            temp+=sq[z]
    print total
main(10**8)
