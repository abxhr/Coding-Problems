# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
