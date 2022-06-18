# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def removeDups(self, S):
        lst = []
        new_s = ''
        for i in S:
            if i not in lst:
                new_s += i
                lst.append(i)
        return new_s
