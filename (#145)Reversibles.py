def main(a,b):
    count=0
    for x in range(b,a):
        if x%10==0:
            continue
        temp=str(x+int(str(x)[::-1]))
        b=True
        for x in temp:
            if int(x)%2==0:
                b=False
                break
        if b==True:
            count+=1
    print count

main(10**2, 10)
