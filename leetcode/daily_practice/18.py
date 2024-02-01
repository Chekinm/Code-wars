class Solution:

    def __init__(self):
        self.ans = set()
        self.ans_set = set()

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        nums.sort()
        if len(nums) < 4 or target < nums[0] * 4 or target > nums[-1] * 4:
            return

        def two_sum(nums, target):
            left = 0
            r = len(nums) - 1
            ans = []
            while left < r:
                if nums[left] + nums[r] > target:
                    r -= 1
                elif nums[left] + nums[r] < target:
                    left += 1
                elif nums[left] + nums[r] == target:
                    ans.append([nums[left], nums[r]])
                    left += 1
                    r -= 1
            return ans

        def req_sum(nums, number=4, prefix=None, target=0):
            if prefix is None:
                prefix = []

            if number == 2:

                ans = two_sum(nums, target)
                for a2 in ans:
                    a = tuple(prefix + a2)
                    self.ans.add(a)
                return

            for i, num in enumerate(nums):
                prefix.append(num)
                req_sum(nums[i+1:], number - 1, prefix, target - num)
                prefix.pop()

        req_sum(nums, target=target)

        return self.ans
