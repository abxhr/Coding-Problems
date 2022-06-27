# Author: Abshar Mohammed Aslam, github: @abxhr

class Solution:
    def firstUniqChar(self, s: str) -> int:
        htable = {}
        ind = []
        for i in range(len(s)):
            if s[i] in htable:
                htable[s[i]] = False
            else:
                htable[s[i]] = True
                ind.append(i)
        if not any(htable.values()):
            return -1
        return ind[list(htable.values()).index(True)]
