# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = ''
        lnt = 0
        for c in s:
            if c in chars:
                lnt = max(len(chars), lnt)
                chars = chars[chars.index(c)+1:]
            chars += c
        lnt = max(len(chars), lnt)
        return lnt
