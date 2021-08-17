# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s[::-1].split(" ")[::-1]
        return " ".join(words)
