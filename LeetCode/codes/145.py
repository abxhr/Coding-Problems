# Author: Abshar Mohammed Aslam, github: @abxhr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret_list = []
        ret_list.extend(self.postorderTraversal(root.left))
        ret_list.extend(self.postorderTraversal(root.right))
        ret_list.append(root.val)
        return ret_list
