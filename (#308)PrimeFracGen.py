import math
def makesInt(x, n, d):
    temp=x*1.0*n/d
    #print temp
    if temp==int(temp):
        return True
    return False

def main(a):
    fracs=[[17,91],[78,85],[19,51],[23,38],[29,33],[77,29],[95,23],[77,19],[1,17],[11,13],[13,11],[15,2],[1,7],[55,1]]
    num=2
    count=0
    total=0
    while 1:
        l=math.log(num, 2)
        if l==int(l):
            count+=1
            print num, total
        if count==a:
            print total, num
            return
        for x in fracs:
            if makesInt(num, x[0], x[1]):
                num=num*x[0]/x[1]
                print num, x
                break
        total+=1
        #print num, 

main(6)
