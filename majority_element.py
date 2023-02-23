def majorityElement(nums):
    for x in set(nums):
        if nums.count(x) > (len(nums)/2.0):
            return(x)

nums = [-1,100,2,100,100,4,100]
print(majorityElement(nums))


