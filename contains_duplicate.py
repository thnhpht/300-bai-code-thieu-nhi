def containsDuplicate(nums):
    return len(nums) != len(set(nums))

nums = [1,2,3,4]
print(containsDuplicate(nums))