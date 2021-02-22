# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if len(words) == 0:
            return 0
        return len(words[-1])
