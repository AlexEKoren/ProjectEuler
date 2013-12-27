import itertools
def main():
    tempPerms=list(itertools.permutations([9,8,7,6,5,4,3,2,1]))
    perms=[]
    #print tempPerms[0]
    for k in tempPerms:
        add=""
        i=0
        while i<len(k):
            add+=str(k[i])
            #print add
            i+=1
        perms.append(add)
    #print perms[0]
    total=0
    totalP=0
    array=[]
    for k in perms:
        m=1
        while m<=7:
            M=1
            while M<=9-m-1:
                if (int(k[0:m]))*(int(k[m:m+M]))==(int(k[m+M:])):
                    #print k
                    #print k[0:m], k[m:m+M]
                    if not array.__contains__((int(k[m+M:]))):
                        array.append((int(k[m+M:])))
                        total=total+(int(k[m+M:]))
                        totalP+=1
                        #print totalP
                M+=1
            m+=1
    print total
main()
        
            
