from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        res = 0
        for i, char in enumerate(c.most_common()):
            char, occurance = char
            res += occurance * (i // 8 + 1)
        return res
   