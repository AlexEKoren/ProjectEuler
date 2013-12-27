#finds the number of distinct terms when a^b and 2<a<101 and 2<b<101
def main():
    array=[4]
    for a in range(2, 101, 1):
        for b in range(2,101, 1):
            for i in range(len(array)):
                if a**b==array[i]:
                    break
                elif i==len(array)-1 and a**b!=array[i]:
                    array.append(a**b)
                else:
                    i=i+1
    print len(array)

main()

            
