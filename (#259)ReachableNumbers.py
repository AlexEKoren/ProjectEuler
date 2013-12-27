import time
def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)

def is_number(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
    
def main():
    t=time.time()
    array=[]
    total=0
    '''parPlacement=list(set(list(combinations_with_replacement('0123456789',16))))
    for x in parPlacement:
        list(x).sort()
    parPlacement=list(set(parPlacement))
    print "Done with parPlacement", time.time()-t'''
    for x in list(combinations_with_replacement('+-*/ ',8)):
        string="1"+x[0]+"2"+x[1]+"3"+x[2]+"4"+x[3]+"5"+x[4]+"6"+x[5]+"7"+x[6]+"8"+x[7]+"9"
        string2=string.replace(' ','')
        '''for x in parPlacement:
            temp=string2
            numI=-1
            for y in temp:
                if is_number(y)==True:
                    numI+=1
        '''         
        y=eval(string2)
        if y>0:
            print y
            array.append(y)
    array=list(set(array))
    print array
    for x in array:
        total+=x
    print total
    #return total
main()

