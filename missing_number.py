def missingNumber(nums):
    nums = sorted(nums)
    count = nums[0]
    for x in nums:
        if x == count:
            count += 1
        else: 
            return count
    if 0 in nums:
        return count
    return 0

nums = [0,1]
print(missingNumber(nums))