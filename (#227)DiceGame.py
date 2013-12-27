import random
def rollDice():
    return random.randint(1,6)

def main(n):
    d1=1
    d2=n/2+1
    count=0
    while d1!=d2:
        r1=rollDice()
        r2=rollDice()
        if r1==6:
            if d1==n:
                d1=0
            else:
                d1+=1
        elif r1==6:
            if d1==0:
                d1=n
            else:
                d1-=1
        if r2==6:
            if d2==n:
                d2=0
            else:
                d2+=1
        elif r2==6:
            if d2==0:
                d2=n
            else:
                d2-=1
        count+=1
    return count
a=101
total=0
for x in range(a):
    total+=main(100)
print total*1.0/a
