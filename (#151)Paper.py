import random
def cr(l):
    return random.choice(l)

def main(a):
    total=0
    for x in range(a):
        l=[1]
        count=0
        for y in range(16):
            if len(l)==1 and l[0]!=1 and l[0]!=5:
                count+=1
            if 5 not in l:
                c=cr(l)
            while not 5 in l:
                l.append(c+1)
                l.append(c+1)
                l.remove(c)
                c+=1
            l.remove(5)
        total+=count
    print total*1.0/a
main(12347)
