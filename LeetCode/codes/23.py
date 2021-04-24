# Author: Abshar Mohammed Aslam, github.com/abxhr

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        all_nodes = []
        start = ans = ListNode(0)
        for each in lists:
            while each:
                all_nodes.append(each.val)
                each = each.next
        for val in sorted(all_nodes):
            ans.next = ListNode(val)
            ans = ans.next
        return start.next