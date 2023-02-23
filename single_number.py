def singleNumber(nums):
    for x in set(nums):
         if nums.count(x) == 1:
            return x 

nums = [2,2,1]
print(singleNumber(nums))