from functools import reduce


class Solution:

    def isHappy(self, n: int) -> bool:

        def sum_of_square(num):
            return reduce(lambda x, y: x + int(y) ** 2, str(num), 0)

        already_have_set = set()
        current_sum = sum_of_square(n)

        while current_sum != 1 and current_sum not in already_have_set:
            already_have_set.add(current_sum)
            current_sum = sum_of_square(current_sum)

        return current_sum == 1
