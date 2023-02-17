# Author: Abshar Mohammed Aslam

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        for i, curr in enumerate(s):
            if char_map.get(curr):
                if char_map[curr] != t[i]:
                    return False
            elif t[i] not in char_map.values():
                char_map[curr] = t[i]
            else:
                return False
        return True
