# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def maxPower(self, s: str) -> int:
        c = s[0]
        v = 0
        m = 0
        for i in s:
            if i == c:
                v += 1
                if v > m:
                    m = v
            else:
                c = i
                v = 1
        return m