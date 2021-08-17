# Author: Abshar Mohammed Aslam, github.com/abxhr

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not(head):
            return None
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        node = ListNode(stack.pop())
        head = node
        while stack:
            node.next = ListNode(stack.pop())
            node = node.next
        node.next = None
        return head
