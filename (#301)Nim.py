def nim(heaps, misere=True):
        """Computes next move for Nim in a normal or misère (default) game, returns tuple (chosen_heap, nb_remove)"""
        X = reduce(lambda x,y: x^y, heaps)
        if X == 0: # Will lose unless all non-empty heaps have size one
                if max(heaps) > 1:
                        return 1
                for i, heap in enumerate(heaps):
                        if heap > 0: # Empty any (non-empty) heap
                                chosen_heap, nb_remove = i, heap
                                break
        else:
                sums = [t^X < t for t in heaps]
                chosen_heap = sums.index(True)
                nb_remove = heaps[chosen_heap] - (heaps[chosen_heap]^X)
                heaps_twomore = 0
                for i, heap in enumerate(heaps):
                        n = heap-nb_remove if chosen_heap == i else heap
                        if n>1: heaps_twomore += 1
                # If move leaves no heap of size 2 or larger, leave an odd (misère) or even (normal) number of heaps of size 1
                if heaps_twomore == 0: 
                        chosen_heap = heaps.index(max(heaps))
                        heaps_one = sum(t==1 for t in heaps)
                        # misère (resp. normal) strategy: if it is even (resp. odd) make it odd (resp. even), else do not change
                        nb_remove = heaps[chosen_heap]-1 if heaps_one%2!=misere else heaps[chosen_heap]
        return chosen_heap, nb_remove

def main2():
        print nim([1,2,3])
fibs=[1,2,3,5,8,13,21]
for x in range(6,50):
        fibs.append(fibs[x]+fibs[x-1])
#print fibs[30]

def main(a):
    count=0
    for x in xrange(1,a+1):
        if nim([x,2*x,3*x])==1:
            count+=1
        else:
            #print x, 2*x, 3*x
            count+=0
    return count
temp=1
for x in range(9):
       # print main(2**x)
        temp=temp*2+fibs[x]
main2()
#print main(2**15)
#print temp
