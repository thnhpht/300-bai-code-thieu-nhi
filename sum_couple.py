def sumCouple(nums):
    res = []
    n1 = []
    n2 = []
   
    for i in range(0, len(nums), 2):
        n1.append(nums[i])

    for i in range(1, len(nums), 2):
        n2.append(nums[i])

    if len(n1) != len(n2):
        n2.append(0)

    for i in range(len(n1)):
        res.append(n1[i] + n2[i])

    return res

nums = [1, 2, 6, 5, 2, 9, 5]
print(sumCouple(nums))