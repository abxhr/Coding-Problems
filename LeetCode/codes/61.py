# Author: Abshar Mohammed Aslam, github: @abxhr

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        curr = head
        l = 1
        while curr.next:
            curr = curr.next
            l += 1
        curr.next = head
        
        k = l - (k % l)
        
        while k > 0:
            curr = curr.next
            k -= 1
        
        ret_head = curr.next
        curr.next = None
        return ret_head
