# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log10(n)/log10(4) % 1 == 0
