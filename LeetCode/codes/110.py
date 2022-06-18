# Author: Abshar Mohammed Aslam, github: @abxhr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfsCheck(self,root) -> bool:
        if root is None:
            return 0
        return max(self.dfsCheck(root.left),self.dfsCheck(root.right))+1
            
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if abs(self.dfsCheck(root.left)-self.dfsCheck(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
