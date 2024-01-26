from functools import reduce
from operator import xor
from collections import deque
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]: 
        res = [reduce(xor, nums)^((1 << maximumBit) - 1)]
        for i in range(1, len(nums)):
            res.append(res[i-1]^nums[-1*i])
        return res
        