class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        # start from biggest
        # n1 % n2 get togehter
        # next we can look onlhy on slammer number as if n2 % n3 => n1 % 3
        #  
        # nums.sort(reverse=True)
        # print(nums)
        # arrs = []
        # arrs.append(deque([nums[0]]))
        # for i in range(1, len(nums)):
        #     placed = False
        #     new_arrs = []
        #     for arr in arrs:
        #         if arr[0] % nums[i] == 0:
        #             arr.appendleft(nums[i])
        #             placed = True
        #         else:
        #             for k in range(1, len(arr)):
        #                 if arr[k] % nums[i] == 0:
        #                     new_arrs.append(deque([nums[i]] + list(arr)[k:]))
        #                     placed = True
        #                     break
            
        #     if len(new_arrs) != 0:
        #         arrs.extend(new_arrs)
        #     if not placed:
        #         arrs.append(deque([nums[i]]))
            
            
        #     print(arrs)

        # return max(arrs, key=len)
        
        nums.sort()
        
        dp = [[] for i in range((len(nums) + 1))]
        dp[0] = []
        dp[1] = [nums[0]] 
        for i in range(1, len(nums)):
            
            num = nums[i]

            curr_max = 0
            ind_max = 0
            for k in range(0, i):
                print(num, nums[k])
                if num % nums[k] == 0:

                    if curr_max < len(dp[k+1]) + 1:
                        ind_max = k + 1
                        curr_max = len(dp[k+1]) + 1
                        print(f'found {ind_max=}, {curr_max=}')
                
            
            dp[i+1] = dp[ind_max] + [num]
            
            print(f'found {i=}, {dp=}')
        dp.sort(key=len)
            
        return dp[-1]


                
sol = Solution()
print(sol.largestDivisibleSubset([2,3,4,9,8]))