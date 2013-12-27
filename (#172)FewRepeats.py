def check(x):
    s=str(x)
    for y in range(10):
        if s.count(str(y))>=3:
            #print x
            return False
    return True

def main(a):
    total=0
    for x in range(10**(a-1),10**(a)):
        if check(x):
            total+=1
    print total

main(5)
            
