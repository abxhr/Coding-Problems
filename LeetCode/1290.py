# Author: Abshar Mohammed Aslam, github.com/abxhr

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        finalnumber = 0
        lst = []
        temp = head
        while(temp):
            lst.append(temp.val)
            temp = temp.next
        p = len(lst)-1
        for i in lst:
            finalnumber += i * pow(2, p)
            p -= 1
        return finalnumber
        