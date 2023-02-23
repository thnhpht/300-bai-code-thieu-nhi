nums = [2,5,5,11]
target = 10

# Brute Force
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Two-pass Hash Table
# def two_sum(nums, target):
#     hashmap = {}
#     for i in range(len(nums)):
#         hashmap[nums[i]] = i
#     for i in range(len(nums)):
#         complement = target - nums[i]
#         if complement in hashmap and hashmap[complement] != i:
#             return [i, hashmap[complement]] 

# One-pass Hash Table
# def two_sum(nums, target):
#     hashmap = {}
#     for i in range(len(nums)):
#         complement = target - nums[i]
#         if complement in hashmap:
#             return [i, hashmap[complement]]
#         hashmap[nums[i]] = i


print(two_sum(nums, target))