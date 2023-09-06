def longest_sub(nums):


    set_nums = set(nums)
    max_res = 0
    while len(set_nums):
        current_elem = set_nums.pop() #pop random element
        left = current_elem - 1
        right = current_elem + 1
        while left in set_nums:
            set_nums.remove(left)
            left -= 1
        while right in set_nums:
            set_nums.remove(right)
            right += 1
        max_res = max(max_res, right - left - 1)
    
    return max_res
