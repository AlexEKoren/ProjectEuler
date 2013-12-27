import random
def choose(a):
    return random.randint(1,a)

def Or(a,b):
    return a|b

def main(a):
    lim=2**32-1
    total=0
    for b in range(a):
        x=0
        count=0
        while x!=lim:
            y=choose(lim)
            x=Or(x,y)
            count+=1
        #print count
        total+=count
    print total*1.0/a

main(234379)
