def main():
    seq=[]
    total=1
    for n in range(1,12):
        seq.append(1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10)
    print seq
    array=[0,0,0,0,0,0,0,0,0,0]
    total+seq[1]+seq[1]-seq[0]
    t1=[-1, -1, -1, -1]
    t2=[683**2, 683**2, 683, 1]
    t3=[44287**2, 44287**2, 44287, 1]
    temp=[]
    temp2=[]
    temp3=[]
    for x in range(4):
        temp.append((t1[x]+t2[x])*-1*44286)
        temp2.append((t1[x]+t3[x])*682)
    for x in range(4):
        temp3.append((temp[x]+temp2[x]))
    print temp2
    print temp3
    
main()
    
    
