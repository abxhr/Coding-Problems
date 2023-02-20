# Author: Abshar Mohammed Aslam

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        lookup = {}
        if len(pattern) != len(s):
            return False
        for i, curr in enumerate(pattern):
            if s[i] not in lookup.values():
                if lookup.get(curr):
                    return False
                lookup[curr] = s[i]
            elif lookup.get(curr) != s[i]:
                print(lookup)
                return False
            else:
                continue
        print(lookup)
        return True
