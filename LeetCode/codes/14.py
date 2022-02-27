# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        end = 0
        till = min([len(s) for s in strs])
        for index in range(till):
            if all(s[index] == strs[0][index] for s in strs):
                end += 1
            else:
                break
        return strs[0][:end]