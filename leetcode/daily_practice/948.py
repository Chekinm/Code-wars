from collections import deque
class Solution:
    

    def bagOfTokensScore(self, tokens: list[int], power: int, score=0) -> int:

        tokens.sort()
        tokens = deque(tokens)

        
        while tokens and (power > tokens[0]):
            while power >= tokens[0]:
                power -= tokens.popleft()
                score += 1
            if score > 0 and tokens[-1] > tokens[0]: # tokens[-1] > token[0] == True means  len(tokens) >= 2
                power += tokens.pop()
                score -= 1
        return score

s = Solution()

s.bagOfTokensScore([100,200,300,400],200)