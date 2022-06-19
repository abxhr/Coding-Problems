# Author: Abshar Mohammed Aslam, github: @abxhr

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        aNode = headA
        bNode = headB
        while aNode!= bNode:
            aNode = headB if aNode is None else aNode.next
            bNode = headA if bNode is None else bNode.next
        return aNode
