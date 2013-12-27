f=[1]
def fact(x):
    t=1
    for y in range(1,x+1):
        t*=y
        f.append(t)


def choose(i,j,k):
    return f[-1]/(f[i]*f[j]*f[k])

def main(a):
    #fact(a)
    count=0
    for i in range(a+1):
        for j in range(a-i+1):
            #print i,j,a-j-i, choose(i,j,a-i-j)
            #if choose(i,j,a-j-i)%10**12==0:
                count+=1
    print count

main(200000)
    
