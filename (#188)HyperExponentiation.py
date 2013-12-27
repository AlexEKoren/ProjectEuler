def hyperexp(base, exp):
    if exp==1:
        return base
    else:
        return pow(base,hyperexp(base,exp-1),10**8)

def main(b, e):
    count=0
    temp=1
    if e>50:
        x=hyperexp(b,50)
        while count+50<e:
            temp*=x
            count+=50
    temp*=hyperexp(b,e%50)
    print temp
main(1777,7)
#print hyperexp(1777,40)
#print pow(3,81,10**8)
