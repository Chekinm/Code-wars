# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        all_value = []
        heapify(all_value)
        
        
        def dfs(root, all_value):
            if not root:
                return
            dfs(root.left, all_value)
            heapq.heappush(all_value, root.val)
            dfs(root.right, all_value)
        
        dfs(root, all_value)
        
        min_dist = 1000000
        for i in range(1, len(all_value)):
            min_dist = min(all_value[i] - all_value[i-1], min_dist)

        return min_dist



        