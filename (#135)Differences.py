def main(a):
    array=[0]*(a+1)
    x=1
    i=int(x/2.5)
    while x<a:
        print (x)
        while i>=x/5:
            b=x**2-(x-i)**2-(x-2*i)**2
            c=x**2-(x-(x-i))**2-(x-2*(x-i))**2
            #print (x, i, b, c)
            if b<=a:
                if b>0:
                    array[b]+=1
                else:
                    break
            if c<=a:
                if c>0:
                    array[c]+=1
                else:
                    break
            i+=1
        x+=1
        i=int(x/2.5)
    total=0
    for x in range(len(array)):
        if array[x]==10:
            print (x)
            total+=1
    print (total)
main(10000)
