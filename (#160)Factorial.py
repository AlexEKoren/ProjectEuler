def fact(x):
    f=1
    for y in range(2,x+1):
        f*=y
        while f%10==0:
            f/=10
        f=f%(10**5)
    return f

print fact(10000000)
