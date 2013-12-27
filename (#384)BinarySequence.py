nums=[]
fibs=[]
def binary(x):
    return str(bin(x))[2:]

def a(y):
    x=0
    count=0
    n=binary(y)
    while x<len(n)-1:
        if n[x]=="1" and n[x]==n[x+1]:
            count+=1
        x+=1
    return count

def b(n):
    return (-1)**(a(n))

def s(n):
    global nums
    array=[]
    total=0
    count=0
    for x in range(n):
        total+=b(x)
        count+=1
        if total>len(array):
            array.append([[total,count]])
        else:
            array[total-1].append([total,count])
    nums=array

def find(a,n):
    return nums[a-1][n-1][1]

def fibo(n):
    global fibs
    fibs.append(1)
    fibs.append(1)
    for x in range(n-2):
        fibs.append(fibs[-1]+fibs[-2])
def main(a,n):
    s(a)
    x=1
    fibo(n)
    total=0
    while x<len(fibs):
        print fibs[x], fibs[x-1],x
        print find(fibs[x],fibs[x-1])
        total+=find(fibs[x],fibs[x-1])
        x+=1
    print total

main(30000,15)
    

