# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = ''
        place = 1
        for i in str(n)[::-1]:
            if place == 4:
                place = 2
                res = i + '.' + res
            else:
                place += 1
                res = i + res
        return res
