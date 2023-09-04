from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        sliding_dict = {}

        left = 0
        right = 0

        while right < len(nums):
            if right - left > k:
                sliding_dict.pop(nums[left])
                left += 1
            if nums[right] in sliding_dict:
                return True
            else:
                sliding_dict[nums[right]] = right
            right += 1

        return False
