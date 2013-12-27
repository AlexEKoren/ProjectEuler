def factor(x):
    a=[]
    for n in range(1,int(x**.5)+1):
        if x%n==0:
            a.append(n)
            a.append(x/n)
    return a

print len(factor(71328803586048))
