def count2(num):
    count = 0
    while num > 0:
        num = num // 2
        count += num
    return count


def res(n, k):
    parity = count2(n) - count2(k) - count2(n-k)
    return 'EVEN' if parity > 0 else 'ODD'