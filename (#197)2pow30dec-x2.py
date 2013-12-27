def main(z):
    x=-1
    for y in range(z):
        x=(int(2**(30.403243784-(x**2)))+1)*1.0
        x*=(10**(-9))
        if y==z-2:
            t=x
    print x+t
main(10**5)
