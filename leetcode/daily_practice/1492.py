class Solution:         
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        count = 0
        while count < k and i <= n:
            if n % i == 0:
                count += 1
            i += 1
            
        return (i - 1) if count == k else -1

        