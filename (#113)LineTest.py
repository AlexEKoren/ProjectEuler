def function(n):
    return 1-n*(1-n*(1-n*(1-n*(1-n*(1-n*(1-n*(1-n*(1-n*(1-n)))))))));


def rref(M):
    if not M: return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        M[r] = [ mrx / lv for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
        lead += 1

def main():
    array=[]
    total=0
    for n in range(1,12):
        array.append(function(n))
    array=[9,99,474,1674,4953,12951]
    #print array
    for x in range(1,6):
        m=[]
        for n in range(1,x+1):
            temp=[]
            for p in range(0,x):
                temp.append(n**p)
            temp.append(array[n-1])
            m.append(temp)
        #print m
        rref(m)
        print m
        f=[]
        for y in reversed(m):
            f.append(y[-1])
        #print x,f
        n=1
        while 1:
            check=0
            for l in range(len(f)):
                check+=f[l]*n**(x-l-1)
            if n==12:
                break
            if check==array[n-1]:
                #print check
                n+=1
            else:
                break
        #print "added:",check
        total+=check
    print "total:", total

main()

    
