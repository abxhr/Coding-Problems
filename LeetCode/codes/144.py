# Author: Abshar Mohammed Aslam,  github: @abxhr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        ret_list = []
        while stack:
            curr_node = stack.pop()
            if curr_node:
                stack.append(curr_node.right)
                stack.append(curr_node.left)
                ret_list.append(curr_node.val)
        return ret_list
