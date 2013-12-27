import itertools
def main(a):
    array=["A","B","C","D","E","F"]
    for x in range(10):
        array.append(str(x))
    total=0
    for x in itertools.product(array, repeat=a):
        if x[0]=="0":
            continue
        if "A" in x:
            if "0" in x:
                if "1" in x:
                    #print x
                    total+=1
    print total

main(6)
