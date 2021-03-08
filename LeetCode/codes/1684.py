# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        n = 0
        for i in words:
            f = True
            for j in i:
                if j not in allowed:
                    f = False
                    break
            if f:
                n += 1
        return n