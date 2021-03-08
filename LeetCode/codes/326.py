# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: 
            return False
        return log10(n)/log10(3) % 1 == 0