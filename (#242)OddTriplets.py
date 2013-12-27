import itertools

def f(n, k):
    count=0
    perms=itertools.combinations(range(1,n+1), k)
    for x in perms:
        if sum(x)%2==1:
            count+=1
    return count


def main(x):
    count=0
    for n in range(1,x,2):
        for k in range(1,n+1,2):
            if f(n,k)%2==1:
                count+=1
                print n, k, f(n,k)
    print count

main(25)
