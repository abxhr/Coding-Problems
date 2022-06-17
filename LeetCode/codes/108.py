# Author: Abshar Mohammed Aslam, github: @abxhr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.toBST(nums,0,len(nums)-1)
    
    def toBST(self,nums,start,end) -> Optional[TreeNode]:
        if end < start:
            return None
        mid = (start+end)//2
        curr = TreeNode(nums[mid])
        
        curr.left = self.toBST(nums,start,mid-1)
        curr.right = self.toBST(nums,mid+1,end)
        
        return curr