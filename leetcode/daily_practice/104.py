class Solution:
    max_depth = 0
    def maxDepth(self, root: Optional[TreeNode], depth=1) -> int:
        if root is None:
            return 0
        if root.left is not None:
            self.maxDepth(root.left, depth + 1)
        if root.right is not None:
            self.maxDepth(root.right, depth + 1)
        self.max_depth = max(self.max_depth, depth)
        return self.max_depth

