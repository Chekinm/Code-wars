from math import inf
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n < 2:
            return n
        dp = {}
        dp[0] = 0
        for i in range(1, 31):
            dp[i] = 2 * dp[i-1] + 1
        
        b = bin(n).lstrip('0b')
        bit_l = n.bit_length()
        res = 2 * dp[bit_l-1] + 1  - self.minimumOneBitOperations(int(b[1:], 2))

        
        # bit_num = 0
        # res = 0
        # #print(bin(n))
        # while n:
        #     bit = n % 2
        #     #print(bit, dp[bit_num])
        #     res += dp[bit_num] * bit
        #     bit_num += 1
        #     n = n >> 1


        return res



s = Solution()



# for n in range(100,50000):
#     if abs(n - s.minimumOneBitOperations(n)) < 2:
#         print(n)
        


print(s.minimumOneBitOperations(6))
