from collections import deque, defaultdict
class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        window = defaultdict(deque)

        l = -1
        r = 0
        max_len = 0
        while r < len(nums):
            print(nums[l+1:r+1])
            window[nums[r]].append(r)
            if len(window[nums[r]]) <= k:
                max_len = max(max_len, r - l)
            else:
                ind = window[nums[r]][0]
                while l < ind:
                    window[nums[l+1]].popleft()
                    l += 1
            r += 1
        return max_len
            

        
s = Solution()

nums, k  = [1,2,3,1,2,3,1,2], 2
print(s.maxSubarrayLength(nums, k))