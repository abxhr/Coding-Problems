# Author: Abshar Mohammed Aslam, github: @abxhr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def search(node, depth):
            if not node:
                return depth
            return max(search(node.left, depth+1), search(node.right, depth+1))
        return search(root, 0)
