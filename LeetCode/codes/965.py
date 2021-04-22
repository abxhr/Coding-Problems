# Author: Abshar Mohammed Aslam, github.com/abxhr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.checker(root, root)
    
    
    def checker(self, root, prev):
        if root is None:
            return True
        left_traversal = self.checker(root.left, root)
        right_traversal = self.checker(root.right, root)
        if root.val == prev.val:
            return left_traversal and right_traversal
        return False
    
    