# Author: Abshar Mohammed, github: @abxhr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfscheck(node,depth):
            if not node:
                return depth
            else:
                if node.left is None:
                    return dfscheck(node.right,depth+1)
                elif node.right is None:
                    return dfscheck(node.left,depth+1)
                return min(dfscheck(node.left,depth+1),dfscheck(node.right,depth+1))
        return dfscheck(root,0)

