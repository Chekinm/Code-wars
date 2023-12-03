from math import inf


def maxSubarraySumCircular(nums: list) -> int:
    """Kadan's algorithm in circular array
        the Idea behind is to find max_sum subarray
        and subarray with max negtive value
        then we compare inner subarry with 
        rest from the start and end, which together 
        organaize an subarray in circualar array 
        made from the original one.
    """
    curr_sum = curr_sum_negative = 0
    max_sum = -inf
    min_sum_negative = inf
    total = 0

    for num in nums:
        total += num
        curr_sum += num
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum <= 0:
            curr_sum = 0
        curr_sum_negative += num
        if curr_sum_negative < min_sum_negative:
            min_sum_negative = curr_sum_negative
        if curr_sum_negative >= 0:
            curr_sum_negative = 0

    return max_sum if total == min_sum_negative else max(max_sum, total - min_sum_negative)
