def find_unique(nums: list[int]) -> int:
    
    res = 0
    for num in nums:
        res ^= num
    return res

print(find_unique([1,1,2,2,100]))

