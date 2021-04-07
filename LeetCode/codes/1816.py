# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])
