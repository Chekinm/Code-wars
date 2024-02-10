class Solution:
    def __init__(self):
        self.ans = set()
    def combinationSum2(self, cand, target):
        cand.sort(reverse=True)
        def bt(cand, target, stack=[]):
            if stack is None:
                stack = []
            if not cand:
                return 
            k = 0
            while k < len(cand):
                if cand[k] > target:
                    k += 1
                elif cand[k] == target:
                    stack.append(cand[k])
                    self.ans.add(tuple(stack))
                    n = stack.pop()
                    if n == 1:
                        return 
                    k += 1
                else:
                    if target-cand[k] > 0:
                        stack.append(cand[k])
                        bt(cand[k + 1:], target-cand[k], stack)
                    n = stack.pop()
                    if n == 1:
                        return
                    k += 1
        bt(cand, target)
        return list(self.ans)
    
a = Solution()
print(a.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 30))