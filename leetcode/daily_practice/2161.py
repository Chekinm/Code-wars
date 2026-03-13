class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        start, middle, end  = [], [], []
        for num in nums:
            if num < pivot:
                start.append(num)
                continue
            if num > pivot:
                end.append(num)
                continue
            middle.append(num)
        return start + middle + end
        