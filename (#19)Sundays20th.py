def main():
    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    x=1
    year=1901
    total=0
    while year<2000:
        months[1]=28
        if year%4==0:
            months[1]=29
        for i in months:
            x+=i
            if x%7==0:
                total+=1
        year+=1
    print total
main()
