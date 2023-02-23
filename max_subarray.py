def maxSubArray(nums):
    curSum = maxSum = nums[0]
    for num in nums[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)

    return maxSum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))