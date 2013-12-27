def rec(length, used, i):
    used[i]+=1
    if length == 5:
        print "yes"
        return 1
    counts = 0
    print used
    if used[i] < 4:
        for x in range(10):
            
            counts+=rec(length + 1, used, x)
    return counts

def main():
    total = 0
    for x in range(10):
        #total+=rec(1,[0]*10,x)
        rec(1,[0]*10,x)

    print total
main()
