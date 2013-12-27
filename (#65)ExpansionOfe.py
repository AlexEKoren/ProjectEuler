def main(x):
    denoms=[0,1]
    nums=[1,2]
    k=2
    count=0
    for y in range(1,x):
        if count%3==0 or count%3==2:
            denoms.append(denoms[y]+denoms[y-1])
            nums.append(nums[y]+nums[y-1])
        else:
            denoms.append(k*denoms[y]+denoms[y-1])
            nums.append(k*nums[y]+nums[y-1])
            k+=2
        count+=1
    s=str(nums[-1])
    total=0
    for a in s:
        total+=int(a)
    print total
main(100)
