def sortedSquares(nums):
    return sorted([x**2 for x in nums])

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))