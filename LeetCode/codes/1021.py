# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        c = 0
        new_s = ''
        for i in S:
            if i == '(':
                if c != 0:
                    new_s += i
                c += 1
            elif i == ')':
                if c != 1:
                    new_s += i
                c -= 1
        return new_s
