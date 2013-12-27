def A(m, n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return A2(m-1,1)
    elif m>0 and n>0:
        return A2(m-1, A2(m,n-1))

def A2(m, n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return A3(m-1,1)
    elif m>0 and n>0:
        return A3(m-1, A3(m,n-1))

def A3(m, n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return A4(m-1,1)
    elif m>0 and n>0:
        return A4(m-1, A4(m,n-1))

def A4(m, n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return A5(m-1,1)
    elif m>0 and n>0:
        return A5(m-1, A5(m,n-1))

def A5(m, n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return A6(m-1,1)
    elif m>0 and n>0:
        return A6(m-1, A6(m,n-1))

def A6(m, n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return A(m-1,1)
    elif m>0 and n>0:
        return A(m-1, A(m,n-1))

def main(a):
    total=0
    for x in range(a):
        total+=A(x,x)
    print total

main(3)
