import itertools
import AEKsys

def main():
    f=(open(AEKsys.MyPrograms+"\\#105sets.txt","r")).readlines()
    perms=[]
    sets=[]
    for x in f:
        #print x
        temp=[]
        s=""
        for y in x:
            if y!=",":
                s+=y
            else:
                #print s
                temp.append(int(s))
                s=""
        temp.append(int(s))
        sets.append(temp)
    #print sets[0]
    perms=[]
    for x in range(1,13):
        temp=(itertools.combinations(range(12), x))
        for y in temp:
            #print y
            perms.append(list(y))
    '''for h in perms:
        print h'''
    total=0
    count=0
    for x in sets:
        #print x
        x.sort()
        n=2
        yes=True
        '''while len(x)-n>=n:
            #print "yep",x[0:n], x[-n+1:], x
            if sum(x[0:n])<sum(x[-n+1:]):
                yes=False
                break
            n+=1'''
        if yes==True:
            print x
            k=0
            SS=[[0]]
            cL=0
            temp=[0]
            while k<len(perms):
                h=perms[k]
                #print h, k, len(x)
                while h[-1]>=len(x) and k<len(perms)-1:
                    k+=1
                    h=perms[k]
                if len(h)>len(x):
                    break
                #print h
                temp1=[]
                for a in h:
                    temp1.append(x[a])
                if sum(temp1) in SS or sum(temp1)<max(SS[-1]) or sum(temp1) in temp:
                    cL=len(temp1)
                    yes=False
                    break
                if len(temp1)!=cL:
                    cL=len(temp1)
                    SS.append(temp)
                    temp=[]
                else:
                    temp.append(sum(temp1))
                #print temp1
        if yes==True:
            count+=1
            total+=sum(x)
            print x
            '''
            j=0
            while j<len(perms):
                z=perms[j]
                while z[-1]>=len(x) and j<len(perms)-1 or j==k:
                    #print j
                    j+=1
                    if j>=len(perms)-1:
                        break
                    z=perms[j]
                if j>=len(perms)-1:
                    break
                if len(z)>len(x)/2+1:
                    break
                if z[-1]>=len(x):
                    break
                #print z
                temp2=[]
                for a in z:
                    temp2.append(x[a])
                #print temp1, temp2
                if sum(temp1)==sum(temp2):
                    yes=False
                    print "YES"
                    break
                if len(temp1)>len(temp2):
                    if sum(temp1)<sum(temp2):
                        yes=False
                        print "YES"
                        break
                if len(temp2)>len(temp1):
                    if sum(temp2)<sum(temp1):
                        yes=False
                        print "YES"
                        break
                j+=1
            if yes==False:
                print "BREAKING"
                break
            k+=1
        if yes==True:
            total+=sum(x)
            #print x
            count+=1'''
    print total, count
            
                    


main()
