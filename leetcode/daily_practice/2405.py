class Solution:
    def partitionString(self, s: str) -> int:
        ans = 1
        curr_set = set()
        r = 0
        while r < len(s):
            if s[r] not in curr_set:
                curr_set.add(s[r])
                r += 1
            else:
                ans += 1
                curr_set.clear()
        return ans
