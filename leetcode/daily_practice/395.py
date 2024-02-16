from collections import Counter
class Solution:
    
    def longestSubstring(self, s: str, k: int) -> int:
        def is_good(s):
            c = Counter(s)
            if min(c.values()) < k:
                return 0
            return len(s)

        if is_good(s):
            return len(s)
        
        c = Counter(s)

        to_split = set()
        for key, value in c.items():
            if value < k:
                to_split.add(key)
            
        max_len = 0
        r = 0
        l = 0
        while r < len(s):  
            if s[r] in to_split:
                if r > l:
                    max_len = max(max_len, self.longestSubstring(s[l:r], k))
                l = r + 1
            r += 1
        else:
            if r > l:
                max_len = max(max_len, self.longestSubstring(s[l:r], k))
        return max_len




        

    
s = Solution()
print(s.longestSubstring("bbaaacbd", 3))