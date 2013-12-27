import itertools

def findChain(a,b,c,d):
    array=[]
    nums=list(itertools.permutations([a,b,c,d],4))
    ops=list(itertools.product(["+","-","*","/"],repeat=3))
    for x in nums:
        for y in ops:
            s1="((("+x[0]+y[0]+x[1]+")"+y[1]+x[2]+")"+y[2]+x[3]+")"
            if "/0" not in s1:
                array.append(eval(s1))
            #print s1
            '''s2="(("+x[0]+y[0]+"("+x[1]+y[1]+x[2]+"))"+y[2]+x[3]+")"
            if y[0]!="/" and eval(x[1]+y[1]+x[2])!=0:
                array.append(eval(s2))
            s3="("+x[0]+y[0]+"("+x[1]+y[1]+"("+x[2]+y[2]+x[3]+")))"
            if y[1]!="/" and eval(x[2]+y[2]+x[3])!=0:
                if y[0]!="/" and eval("("+x[1]+y[1]+"("+x[2]+y[2]+x[3]+"))")!=0:
                    array.append(eval(s3))
            s4="("+x[0]+y[0]+"(("+x[1]+y[1]+x[2]+")"+y[2]+x[3]+"))"
            if y[0]!="/" and eval("(("+x[1]+y[1]+x[2]+")"+y[2]+x[3]+")")!=0:
                array.append(eval(s4))'''
            s5="(("+x[0]+y[0]+x[1]+")"+y[1]+"("+x[2]+y[2]+x[3]+"))"
            if y[1]!="/" and eval(x[2]+y[2]+x[3])!=0:
                array.append(eval(s5))
    i=0
    array=list(set(array))
    array.sort()
    array2=[]
    for x in array:
        if x>0 and x==int(x):
            array2.append(x)
    array2.sort()
    #print array2
    while 1:
        if array2[i]!=i+1:
            return i
        i+=1
        if i==len(array2):
            return len(array2)
    return 0

def main():
    m=0
    final=[1,2,3,4]
    for a in range(1,10):
        for b in range(a+1,10):
            for c in range(b+1,10):
                for d in range(c+1,10):
                    temp=findChain(str(a*1.0),str(b*1.0),str(c*1.0),str(d*1.0))
                    print temp, a, b, c, d
                    if temp>m:
                        m=temp
                        final=[a,b,c,d]
                        print final, m
    print final, m
                        
#findChain("1","2","3","5")
main()          
