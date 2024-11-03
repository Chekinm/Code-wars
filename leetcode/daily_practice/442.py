def findDuplicates(nums: list[int]) -> list[int]:
    i = 0
    res = []
    while i < len(nums):
        print(i, nums[i])
        n = int(str(nums[i])[0])
        nums[n-1] *= 10
        i += 1
    for i in range(len(nums)):
        if nums[i] >= 100:
            res.append(i+1)
    print(nums)
    return res


        
print(findDuplicates([8,1,2,6,4,3,6,8]))