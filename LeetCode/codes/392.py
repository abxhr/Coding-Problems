# Author: Abshar Mohammed Aslam, github: @abxhr

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        ind_s = 0
        
        for ch in t:
            if ind_s <= len(s) - 1:
                if s[ind_s] == ch:
                    ind_s += 1
            else:
                break
        
        return ind_s == len(s)