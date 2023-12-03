class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode], res=None) -> List[int]:
        # if res is None:
        #     res = []
        # if root is None:
        #     return []
        # if root.left is not None:
        #     self.inorderTraversal(root.left, res)
        # res.append(root.val)
        # if root.right is not None:
        #     self.inorderTraversal(root.right, res)
        
        # return res

        res = [root] if root else []
        
        def do_have_child(elem):
            return elem.left is not None or elem.right is not None
        
        have_child = True

        while have_child:
            have_child = False
            i = 0
            while i < len(res):
                if isinstance(res[i], int):
                    i += 1
                else:
                    have_child = have_child or do_have_child(res[i])

                    left = res[i].left
                    right = res[i].right
                    val = res[i].val

                    insert = [left, val] if left else [val]
                    if right: insert.append(right)  

                    res[i:i+1] = insert
                    i += len(insert)
                
        return res