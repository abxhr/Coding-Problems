# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        i = 0
        while (i < len(s)):
            if i % (2*k) == 0:
                sub_str = s[i:i+k]
                ans += sub_str[::-1]
                i += k
            else:
                ans += s[i]
                i += 1
        return ans
