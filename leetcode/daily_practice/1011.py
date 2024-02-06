def shipWithinDays(weights: list[int], days: int) -> int:
    
    
    def can_shiping(load, weights, days):
        n = len(weights)
        i = 0
        pack = 0
        d = 0
        while i < n:
            if weights[i] > load:
                return False
            while i < n and pack + weights[i] <= load:
                pack += weights[i]
                i += 1
            d += 1
            if d > days:
                return False
            pack = 0
        return True
                    
    total_w = sum(weights)
    left = min(weights)
    right = total_w

    while left < right:
        m = (left + right) // 2
        if can_shiping(m, weights, days):
            right = m #
        else:
            left = m + 1  # ?
    return left

a = shipWithinDays([3,2,2,4,1,4], 3)
print(a)
