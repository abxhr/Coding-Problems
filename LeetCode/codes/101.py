# Author: Abshar Mohammed Aslam, github: @abxhr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def DFSCheck(self, leftRoot, rightRoot) -> bool:
        if not leftRoot or not rightRoot:
            return leftRoot == rightRoot
        return (leftRoot.val == rightRoot.val) and (self.DFSCheck(leftRoot.right, rightRoot.left) and self.DFSCheck(leftRoot.left, rightRoot.right))
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.DFSCheck(root.left,root.right)