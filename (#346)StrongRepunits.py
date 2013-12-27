def main(a):
    repunits=[1]
    for x in range(2,int(a**.5)+1):
        temp=x**2
        tempTotal=x**2+x+1
        while tempTotal<a:
            repunits.append(tempTotal)
            tempTotal+=temp*x
            temp*=x
    repunits=list(set(repunits))
    total=0
    for x in repunits:
        total+=x
    print total
main(10**12)
