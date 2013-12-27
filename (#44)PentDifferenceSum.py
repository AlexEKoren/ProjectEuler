def findPents(x):
    array=[]
    i=1
    while i<x:
        array.append(i*(3*i-1)/2)
        i=i+1
    return array

def main(x):
    pents=findPents(x)
    check=pents[len(pents)-1]
    for i in pents:
        #print i
        else:
            j=0
        for j in pents:
            if j>i:
                break
            if pents.__contains__(j+i) and pents.__contains__(i-j):
                if abs(i-j)<check:
                    check=abs(i-j)
                    difference=check
                    print check
                    return
main(10000)
