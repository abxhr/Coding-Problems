# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and log10(n)/log10(2) % 1 == 0