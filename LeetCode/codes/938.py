# Author: Abshar Mohammed Aslam, github.com/abxhr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def search(node):
            if node:
                if low <= node.val <= high:
                    self.val += node.val
                if low < node.val:
                    search(node.left)
                if high > node.val:
                    search(node.right)

        self.val = 0
        search(root)
        return self.val
