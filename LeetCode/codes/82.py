# Author: Abshar Mohammed Aslam, github: @abxhr

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        act_node = ListNode(-1, head)
        ret_head = act_node
        while act_node:
            sub_node = act_node.next
            if sub_node and sub_node.next and sub_node.val == sub_node.next.val:
                check = sub_node.val
                while sub_node and sub_node.val == check:
                    sub_node = sub_node.next
                act_node.next = sub_node
            else:
                act_node = act_node.next
        return ret_head.next