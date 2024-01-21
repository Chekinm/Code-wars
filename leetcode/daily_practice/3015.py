from itertools import  combinations
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x, y = y, x
        pairs = list(combinations(range(1,n+1), 2))
        res = {i:0 for i in range(1,n+1)}
        for pair in pairs:
            l, r = pair
            direct_path = abs(r - l)
            indirect_path = abs(x - l) + min(1, abs(x - y)) + abs(y - r)
            path = min(direct_path, indirect_path)
            res[path] += 2
        return res.values()