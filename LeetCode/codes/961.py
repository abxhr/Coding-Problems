# Author: Abshar Mohammed Asla, github.com/abxhr

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in A:
            if A.count(i) > 1:
                return i