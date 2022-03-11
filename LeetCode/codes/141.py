# Author: Abshar Mohammed Aslam, github: @abxhr

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slower = head
        faster = head.next
        while faster.next and faster.next.next and slower != faster:
            slower = slower.next
            faster = faster.next.next
        return slower == faster