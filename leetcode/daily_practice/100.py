class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
                return all((
                    self.isSameTree(p.right, q.right),
                    self.isSameTree(p.left, q.left),
                ))