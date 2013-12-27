def main():
    total=0
    n=3
    d=2
    for x in range(1000):
        temp=d
        d=n+d
        n=d+temp
        if len(str(n))>len(str(d)):
            total+=1
    print total
main()
