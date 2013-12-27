from itertools import product
def main():
    perms=product('01',repeat=6)
    count=0
    for x in perms:
        t1=int(x[0]+x[1]+x[2]+x[3]+x[4]+x[5])
        t2=int(x[1]+x[2]+x[3]+x[4]+x[5]+str((int(x[0])^(int(x[1])&int(x[2])))))
        if t1&t2:
            count+=1
    print count

main()
