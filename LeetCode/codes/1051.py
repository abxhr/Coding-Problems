# Author: Abshar Mohammed Aslam, gitub.com/abxhr

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        c = 0
        for i in range(len(heights)):
            if s[i] != heights[i]:
                c += 1
        return c
