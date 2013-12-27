def main():
    final=0
    for a in range(100):
        for b in range(100):
            total=0
            c=list(str(a**b))
            for x in c:
                total+=int(x)
            if total>final:
                final=total
    print final

main()
                
