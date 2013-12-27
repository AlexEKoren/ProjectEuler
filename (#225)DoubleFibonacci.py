def dubFib(e):
    d=[1,1,1]
    for x in range(e):
        d.append(d[x]+d[x+1]+d[x+2])
    return d

def main(x):
    dF=dubFib(x)
    count=0
    y=27
    while y<dF[-1]:
        div=False
        for z in dF:
            if z%y==0 and y!=z:
                div=True
                break
        if div==False:
            count+=1
            print y
        if count==124:
            print y
            return
        y+=2
    
main(30000)
