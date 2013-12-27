def main():
    final=1.0
    q=343.195459424
    counter=0
    while final!=0.02:
        final=1.0
        for x in range(1,51):
            final*=(1.0-x/q)
        print final, q, counter
        q+=.0000000001
        counter+=1
    print q

main()
        
