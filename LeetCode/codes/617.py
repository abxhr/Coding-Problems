# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None and root2 is None:
            return None
        
        if root1 is None:
            res = root2
        elif root2 is None:
            res = root1
        else:
            res = TreeNode(root1.val + root2.val)
            res.left = self.mergeTrees(root1.left, root2.left)
            res.right = self.mergeTrees(root1.right, root2.right)
            
        return res