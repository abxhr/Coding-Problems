# Author: Abshar Mohammed Aslam, github.com/abxhr

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        curr = head
        forward = head.next
        while curr and forward:
            curr = curr.next
            forward = forward.next
            if forward:
                forward = forward.next
        return curr