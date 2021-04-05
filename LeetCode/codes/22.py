# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def generateParenthesis(self, n):
        def gen(left, right, ans):
            if not 0 <= left <= right:
                return
            if not right:
                result.append(ans)
                return
            gen(left - 1, right, ans + '(')
            gen(left, right - 1, ans + ')')
        result = []
        gen(n, n, '')
        return result
