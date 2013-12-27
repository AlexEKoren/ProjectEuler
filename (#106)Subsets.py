import itertools
def main():
    perms=list(itertools.combinations_with_replacement("0123456789, 6))
    print len(perms)
    subset=[13,14,15,16,17,18,19,20,21,22,23,24]
    total=0
    for x in perms:
        for y in x:
            if y==12:
                list(x).remove(y)
                #print "removed"
    print "done"
    print perms[-1]
    for x in perms:
        for y in perms:
            B=0
            C=0
            if not x==y:
                for z in x:
                    B+=subset[int(z)]
                for z in y:
                    C+=subset[int(z)]
            if B==C:
                total+=1
    print total
            
main()
