# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def compare_simetrical(left, right):
    
    if left is not None and right is not None:
        if left.val != right.val:
            return False
        return all((
            compare_simetrical(left.left, right.right),
            compare_simetrical(left.right, right.left),
            ))
    if left is None and right is None:
        return True

    return False 

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return compare_simetrical(root.left, root.right)
        
            

    