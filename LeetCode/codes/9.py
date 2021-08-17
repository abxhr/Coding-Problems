# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
