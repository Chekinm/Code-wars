class Solution:
    def minTimeToType(self, word: str) -> int:
        time = len(word)
        curr_ch = 'a'
        for ch in word:
            dist = abs(ord(curr_ch) - ord(ch))
            time += min(dist, 26 - dist)
            curr_ch = ch
        return time