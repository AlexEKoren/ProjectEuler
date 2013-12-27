def main(x):
    final=0
    for i in range(2,1000000):
        j=0
        for a in str(i):
            j=j+int(a)**x
            if j==i:
                final+=j
    print final

main(5)
