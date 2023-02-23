def productExceptSelf(nums):
    length = len(nums)
    res = [1] * length
    pre, post = 1, 1

    for i in range(length):
        res[i] *= pre
        pre *= nums[i]
        res[-1-i] *= post
        post *= nums[-1-i]
    return res

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))