# Author: Abshar Mohammed Aslam, github: @abxhr

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        s_hash = {}
        t_hash = {}
        
        for l in s:
            if l in s_hash:
                s_hash[l]+=1
            else:
                s_hash[l] = 1
        
        for l in t:
            if l in t_hash:
                t_hash[l]+=1
            else:
                t_hash[l] = 1
        
        for k in s_hash:
            if k not in t_hash or t_hash[k] != s_hash[k]:
                return False
        
        return True
