from collections import defaultdict, deque

class Solution:
    def lastNonEmptyString(self, s: str) -> str:

        d = defaultdict(deque)
        for ind, char in enumerate(s):
            d[char].append(ind)
        
        flag = True
        while flag:
            flag = False
            res = defaultdict(int)
            to_del = []
            for char, indexes in d.items():
                if len(indexes) != 1:
                    flag = True
                    indexes.popleft()
                else:
                    res[char] = indexes.popleft()
                    to_del.append(char)
            
            for char in to_del:
                d.pop(char)
        res = sorted(res.items(), key=lambda x: x[1])
        res = [char[0] for char in res]
        
        res = ''.join(res)

        return res

s = Solution()
print(s.lastNonEmptyString('abcdabcaa'))




