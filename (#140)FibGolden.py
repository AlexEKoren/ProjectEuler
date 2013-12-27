def G(a):
    array=[1,4]
    for x in range(a):
        array.append(array[-1]+array[-2])
    return array

g=G(1000)

def Ag(x):
    y=0
    total=0
    while y<len(g):
        total+=x**(y+1)*g[y]
        #print x, g[y], y, x**(y+1)*g[y], total
        y+=1
    return total

def main(a):
    array=[]
    for d in range(2,a):
        print d
        for n in range(1,d):
            ag=Ag(n*1./d)
            if ag<10**10:
                if abs(int(ag)+1-ag)<10**-5 or int(ag)==ag:
                    #print n, d, ag
                    if not ag in array:
                        array.append(ag)
                        print n,d,ag
main(1000)
