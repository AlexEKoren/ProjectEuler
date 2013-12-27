def u(k,r):
    return (900-3*k)*r**(k-1)

def s(n):
    r=1.0
    total=0
    end=0
    add=.1
    while total!=-600000000000:
        total=0
        for k in range(1, n+1):
            total+=u(k,r,)
        if total<-600000000000:
            print r, end
            r-=add
            add/=10
            if len(str(r))==13:
                print r, end-1
                return
            else:
                end=0
        r+=add
        print total, r, end
        end+=1
        if end%10==0:
            end=0
s(5000)
        
