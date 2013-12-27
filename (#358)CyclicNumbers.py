def main():
    l=[0,0,0,0,0,0,0,0,1,3,5,6,7,7,8,9]
    regx=0000000013756789
    x=00000000137156789
    middle=1
    while 1:
        print x
        temp=x
        temp*=2
        b=False
        while 1:
            templist=list(str(temp))
            templist.sort()
            for y in range(len(templist)):
                if templist[y]!=l[y]:
                    b=True
                    break
            if b==True:
                break
            temp+=x
            if temp==x*len(str(temp)):
                return x
        middle+=1
        x=int(str(regx)[0:12]+str(middle)+str(regx)[12:])
main()
