# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j = list(J)
        s = list(S)
        c = 0
        for i in s:
            if i in j:
                c += 1
        return(c)
