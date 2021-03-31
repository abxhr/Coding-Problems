# Author: Absahr Mohammed Aslam, github.com/abxhr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        values = []
        def dfs(node):
            values.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        min_diff = 100
        for i, n in enumerate(sorted(values)):
            if i == 0:
                p = n
            else:
                min_diff = min(min_diff, abs(p-n))
                p = n
        return min_diff