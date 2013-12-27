from itertools import product
def binToInt(s):
    e=0
    total=0
    for x in reversed(s):
        print int(x)*2**e
        total+=int(x)*2**e
        e+=1
    return total

def genBins(a):
    return product('10',repeat=a)

def main(a):
    bins=list(genBins)
    

main(5)
