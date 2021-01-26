# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def freqAlphabets(self, s: str) -> str:
        x = ''
        i = len(s)-1
        while i > -1:
            if s[i] == '#':
                x = chr(96 + int(s[i-2:i])%27) + x
                i -= 3
            else:
                x = chr(96 + int(s[i])%26) + x
                i -= 1
        return x