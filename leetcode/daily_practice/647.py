class Solution:
    def countSubstrings(self, s: str) -> int:
        
        print(len(s))
        count = 1
        prev_palindorme_suff_list = [0]

        for i in range(1, len(s)):
            pol_suffix_list = []
            count += 1  
            for ind in prev_palindorme_suff_list:
                if ind and s[ind-1] == s[i]:
                    count += 1
                    if ind - 1 > 0:
                        pol_suffix_list.append(ind-1)
            if s[i] == s[i-1]:
                count += 1
                pol_suffix_list.append(i-1)
            pol_suffix_list.append(i)  # simbol is a polindrome itself
            prev_palindorme_suff_list = pol_suffix_list.copy() 
            #dp[i+1] = [count, pol_suffix_list.copy()]

        return count






#         def is_palindorme(s):
#             l = 0
#             r = len(s) - 1
#             while l < r:
#                 if s[l] != s[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             return True

#         dp = [0] * (len(s) + 1)
        

#         for i in range(len(s)):
#             count = 0
#             for k in range(0,i+1):
#                 if is_palindorme(s[k:i+1]):
#                     count += 1
#             dp[i+1] = dp[i] + count
#         print(dp)
#         return dp[-1]
    
sol = Solution()

from datetime import datetime

st = 'bbbb'*1250
start = datetime.now()
#st = 'b' * 5000
print(sol.countSubstrings(st))
print(datetime.now () -start)


'''
# Intuition
We will us DP

# Approach
If we add a next letter to prefix, it will form a palindorme of substring of prefix only if some suffix of previuse prefix is palindorme. 
If so, this new created polindrome will be a suffix in current prefix, and we can create a list of such suffixes.
We also need to count palindorm on each step.
Dont' forget letter itself and case when to last letter of prefix is equal.

# Complexity
- Time complexity:
It is O(num of sub_polindorme)
It can be 0(n^2) in unlucky case of string from one letter.

- Space complexity:

It can be 0(n^2) in unlucky case of string from one letter.


# Code
```
class Solution:
    def countSubstrings(self, s: str) -> int:

        dp = {0: [0,[]]} 
            # count of palindrom substring for curr prefix 
            # list of indexes of palindrome suffix for curr prefix (don't include prefix as a whole word!) 
        dp[1] = [1,[]]  
            
        for i in range(1, len(s)):
            pol_suffix_list = []  # will collect founded palindrome suffix here
            count = dp[i][0] + 1  # as added simbol is palindrom itself
            for ind in dp[i][1]:
                                  # check every suffix from prev step
                if ind and s[ind-1] == s[i]: 
                                  # skip case of whole prefix(ind == 0)
                    count += 1
                    pol_suffix_list.append(ind-1)
            if s[i] == s[i-1]:  # check if two last char is equal
                count += 1
                pol_suffix_list.append(i-1)
            pol_suffix_list.append(i)  # as simbol is a polindrome itself
            dp[i+1] = [count, pol_suffix_list.copy()]

        return dp[len(s)][0]

```

'''