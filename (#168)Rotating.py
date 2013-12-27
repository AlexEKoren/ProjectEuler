def main(a):
    total=0
    count=0
    for x in range(1,10):
        s=str(x)+str(x)
        while len(s)<a:
            total+=int(s)
            s+=s[0]
            count+=1
    #total=total%10**5
    print count
    count=0
    for x in range(1,10**6):
        s=str(x)
        if int(s[-1]+s[:-1])%x==0 and int(s[-1]+s[:-1])!=x:
            while len(s)<a:
                #print s
                if int(s[-1]+s[:-1])%int(s)==0:
                    total+=int(s)
                    count+=1
                s+=str(x)
    print total#%10**5, count

main(100)
