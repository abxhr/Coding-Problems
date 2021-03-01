# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def reverse(self, x: int) -> int:
        res = []
        strx = list(str(x))
        if x < 0:
            res = strx[1:][::-1]
            res = ''.join(res)
            res = -1 * int(res)
        else:
            res = strx[::-1]
            res = ''.join(res)
            res = int(res)
        if -2**31 <= res <= 2**31 - 1:
            return res
        else:
            return 0