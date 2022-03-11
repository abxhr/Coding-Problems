# Author: Abshar Mohammed Aslam, github: @abxhr

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_node = head = ListNode(0)
        carry = 0
        while (l1 is not None and l2 is not None):
            sum = ((l1.val + l2.val) + carry)
            digit = sum%10
            if sum > 9:
                carry = 1
            else:
                carry = 0
            new_node = ListNode(digit, None)
            sum_node.next = new_node
            sum_node = sum_node.next
            l1, l2 = l1.next, l2.next
        while l1:
            sum = l1.val + carry
            digit = sum%10
            if sum > 9:
                carry = 1
            else:
                carry = 0
            new_node = ListNode(digit, None)
            sum_node.next = new_node
            sum_node = sum_node.next
            l1 = l1.next
        while l2:
            sum = l2.val + carry
            digit = sum%10
            if sum > 9:
                carry = 1
            else:
                carry = 0
            new_node = ListNode(digit, None)
            sum_node.next = new_node
            sum_node = sum_node.next
            l2 = l2.next
            if sum > 9:
                carry = 1
            else:
                carry = 0
        if carry:
            sum_node.next = ListNode(1, None)
                
        return head.next
