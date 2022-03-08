# Author: Abshar Mohammed Aslam, github: @abxhr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            ret_list = []
            if root is None:
                return []
            if root.left:
                ret_list.extend(self.inorderTraversal(root.left))
            ret_list.append(root.val)
            if root.right:
                ret_list.extend(self.inorderTraversal(root.right))
            return ret_list