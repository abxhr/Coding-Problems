# Author: Abshar Mohammed Aslam, github: @abxhr

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        if s[::-1] == s:
            return True
        return False
