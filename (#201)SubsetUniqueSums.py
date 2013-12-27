import itertools
def main():
    array=[]
    for x in range(1,101):
        array.append(x**2)
    combs=list(itertools.combinations(array,50))
    print len(combs)
main()
