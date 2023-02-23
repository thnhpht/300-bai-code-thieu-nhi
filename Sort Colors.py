def sortColors(nums): 
    while True:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                tmp = nums[i]
                nums[i] = nums[i-1]
                nums[i-1] = tmp
                count += 1
        if count == 0:
                return nums


nums = [2,0,2,1,1,0]
print(sortColors(nums))