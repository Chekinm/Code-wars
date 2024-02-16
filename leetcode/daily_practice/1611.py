import bisect
from math import inf
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        

        
        
        if n < 2:
            return n
        
        # dp3 = {3 * (2 ** (i - 1)): 2 ** i for i in range(1,30)}

        # l = sorted(list(dp3.keys()))
        # print(l)
        # r = bisect.bisect(l, n) 
        
        # r = l[r-1]
        

        dp = {}
        dp[0] = 0
        dp[1] = 1

        
        def first(n):  # first operation
            if n % 2:
                if (n - 1) not in dp:
                    dp[n - 1] = dp[n] + 1
                    return n - 1
            else:
                if (n + 1) not in dp:
                    dp[n + 1] = dp[n] + 1
                    return n + 1
            return False
        
        def second(n): # second opertation
            dummi = n
            count = 0
            while dummi % 2 == 0:
                count += 1
                dummi = dummi >> 1
            
            if (dummi >> 1) % 2 == 0:
                new_num = n + (1 << (count + 1))
            else:
                new_num = n - (1 << (count + 1))
            if new_num not in dp:
                dp[new_num] = dp[n] + 1
                return new_num
            return False
    
        # do BFS inside and build dp array, until we get dp[n]
        # dp[2048] = 4095
        # nums = [2048,]

        nums = [1,]
        # dp[r] = dp3[r]
        while nums and n not in dp:
            new_nums = []
            for i in nums:
                f = first(i)
                if f:
                    new_nums.append(f)
                s = second(i)
                if s:
                    new_nums.append(s)
            nums = new_nums
    
        #print(*list(sorted(dp.items())), sep='\n')
        return dp[n]

                
        

s = Solution()


# ns = [2 ** i for i in range(18, 20)]
for n in range(1, 50):
    print(n, s.minimumOneBitOperations(n))


# print(s.minimumOneBitOperations(657334))