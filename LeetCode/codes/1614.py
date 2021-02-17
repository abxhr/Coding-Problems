# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def maxDepth(self, s: str) -> int:
        max = 0
        chk = 0 
        for i in s:
            if i == '(':
                chk += 1
            elif i == ')':
                chk -= 1
            if chk > max:
                max = chk
        return max