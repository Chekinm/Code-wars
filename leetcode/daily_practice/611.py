class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        i = len(nums) - 1
        while i >= 2:
            c = nums[i]
            print(c)
            r =  i - 1
            l = 0
            while r - l > 0:
                print(c, nums[r], nums[l])
                if nums[r] + nums[l] > c:
                    res += (r - l)
                    r -= 1
                else:
                    l += 1
            i -= 1
        return res 
    
s = Solution()
print(s.triangleNumber([2,2,3,4]))