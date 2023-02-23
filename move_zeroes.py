def moveZeroes(nums):
    count_zero = nums.count(0)
    for i in range(count_zero):
        nums.remove(0)
        nums.append(0)
    return(nums)
    
nums = [0,1,0,3,12]
print(moveZeroes(nums))