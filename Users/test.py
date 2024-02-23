def mostcase(nums):
    nums = list(set(nums))
    output = []
    for i in range(len(nums)):
        if(len(nums)<3):
            return output
        lptr =i+1
        rptr =len(nums)-1
        if(lptr>=len(nums)):
            return output
        while lptr!=rptr:
            if(nums[i]+nums[lptr]+nums[rptr]) ==0:
                output.append([nums[i],nums[lptr],nums[rptr]])
            rptr -=1
    return output
x = mostcase([-1,0,1,2,-1,-4])   
print(x)