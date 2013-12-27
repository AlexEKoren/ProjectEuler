import math
count=0
def rec(begin):
    global count
    for x in begin:
        if begin.count(x)>2:
            return
    count+=1
    #print begin
    done=[]
    for x in begin:
        if x!=1 and not x in done:
            temp=begin[:]
            temp.remove(x)
            done.append(x)
            rec(temp+[x/2]*2)
def main(a):
    begin=[]
    while a>0:
        l=int(math.log(a,2))
        begin.append(2**l)
        a-=2**l
    rec(begin)
    print count

main(10000000)
    
