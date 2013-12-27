def main(a):
    array=[9999]*(a+1)
    array[0]=0
    array[1]=0
    array[2]=1
    leaves=[[[2,[1,2]]]]
    count=2
    while array.count(9999)>0:
        nex=[]
        for z in leaves:
            leaf=[]
            for x in z:
                for y in x[1]:
                    if x[0]+y<=a:
                        if array[x[0]+y]>count:
                            array[x[0]+y]=count
                            if array.count(9999)==0:
                                print sum(array)
                                return
                        leaf.append([x[0]+y,[x[0]+y]+x[1]])
            nex.append(leaf)
        count+=1
        leaves=nex

main(200)
    
