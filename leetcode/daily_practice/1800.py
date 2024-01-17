class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]
        r = 1
        curr = nums[0]
        while r < len(nums):
            if nums[r] > curr:
                curr_sum += nums[r]
                max_sum = max(max_sum, curr_sum)
            else:
                curr_sum = nums[r]
            curr = nums[r]
            r += 1
        return max_sum
