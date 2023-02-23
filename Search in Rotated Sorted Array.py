def search(nums, target):
    return nums.index(target) if target in nums else -1

    # for i, n in enumerate(nums):
    #         if n == target:
    #             return i  
    # return -1
    
nums = [4,5,6,7,0,1,2]
target = 0

print(search(nums, target))